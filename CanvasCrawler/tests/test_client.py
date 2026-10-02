from __future__ import annotations

import unittest

import httpx

from canvas_crawler.canvas import CanvasClient
from canvas_crawler.config import Settings
from canvas_crawler.exceptions import AuthenticationError, CanvasApiError


class CanvasClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self.settings = Settings(
            base_url="https://canvas.example.edu",
            access_token="test-token",
            per_page=100,
            timeout_seconds=5,
        )

    def build_client(self, handler: httpx.MockTransport) -> CanvasClient:
        http_client = httpx.Client(
            base_url=self.settings.base_url,
            transport=handler,
            headers={"Authorization": "Bearer test-token"},
        )
        self.addCleanup(http_client.close)
        return CanvasClient(self.settings, http_client=http_client)

    def test_lists_and_sorts_courses(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(request.url.path, "/api/v1/courses")
            self.assertEqual(request.url.params.get("enrollment_state[]"), "active")
            return httpx.Response(
                200,
                json=[
                    {
                        "id": 2,
                        "name": "Visão Computacional",
                        "course_code": "IA02",
                        "workflow_state": "available",
                        "term": {"name": "2026/2"},
                    },
                    {
                        "id": 1,
                        "name": "Aprendizado de Máquina",
                        "course_code": "IA01",
                        "workflow_state": "available",
                    },
                ],
            )

        courses = self.build_client(httpx.MockTransport(handler)).list_courses()

        self.assertEqual([course.id for course in courses], [1, 2])
        self.assertEqual(courses[1].term_name, "2026/2")

    def test_follows_canvas_pagination(self) -> None:
        requests: list[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(str(request.url))
            if request.url.params.get("page") == "2":
                return httpx.Response(
                    200,
                    json=[{"id": 2, "name": "Curso B", "course_code": "B"}],
                )
            return httpx.Response(
                200,
                headers={
                    "Link": '<https://canvas.example.edu/api/v1/courses?page=2>; rel="next"'
                },
                json=[{"id": 1, "name": "Curso A", "course_code": "A"}],
            )

        courses = self.build_client(httpx.MockTransport(handler)).list_courses()

        self.assertEqual(len(requests), 2)
        self.assertEqual([course.id for course in courses], [1, 2])

    def test_rejects_pagination_to_another_domain(self) -> None:
        def handler(_: httpx.Request) -> httpx.Response:
            return httpx.Response(
                200,
                headers={"Link": '<https://attacker.example/courses?page=2>; rel="next"'},
                json=[{"id": 1, "name": "Curso", "course_code": "C"}],
            )

        with self.assertRaises(CanvasApiError):
            self.build_client(httpx.MockTransport(handler)).list_courses()

    def test_reports_invalid_token_without_exposing_it(self) -> None:
        def handler(_: httpx.Request) -> httpx.Response:
            return httpx.Response(401, json={"errors": [{"message": "Invalid access token."}]})

        with self.assertRaises(AuthenticationError) as context:
            self.build_client(httpx.MockTransport(handler)).get_current_user()

        self.assertNotIn("test-token", str(context.exception))

    def test_lists_modules_in_canvas_order(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(request.url.path, "/api/v1/courses/10/modules")
            return httpx.Response(
                200,
                json=[
                    {"id": 2, "name": "Segundo", "position": 2, "items_count": 1},
                    {"id": 1, "name": "Primeiro", "position": 1, "items_count": 3},
                ],
            )

        modules = self.build_client(httpx.MockTransport(handler)).list_modules(10)

        self.assertEqual([module.id for module in modules], [1, 2])
        self.assertEqual(modules[0].items_count, 3)

    def test_lists_module_items_without_fetching_content(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(request.url.path, "/api/v1/courses/10/modules/20/items")
            return httpx.Response(
                200,
                json=[
                    {
                        "id": 30,
                        "module_id": 20,
                        "title": "Apresentação",
                        "type": "Page",
                        "position": 1,
                        "completion_requirement": {"type": "must_view", "completed": True},
                    }
                ],
            )

        items = self.build_client(httpx.MockTransport(handler)).list_module_items(10, 20)

        self.assertEqual(items[0].title, "Apresentação")
        self.assertEqual(items[0].type, "Page")
        self.assertEqual(items[0].completion_requirement, "must_view")
        self.assertTrue(items[0].completion_requirement_met)

    def test_marks_module_item_done_with_put(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(request.method, "PUT")
            self.assertEqual(
                request.url.path,
                "/api/v1/courses/10/modules/20/items/30/done",
            )
            return httpx.Response(204)

        client = self.build_client(httpx.MockTransport(handler))
        client.mark_module_item_done(10, 20, 30)

    def test_gets_sessionless_launch_url_from_canvas(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(
                request.url.path,
                "/api/v1/courses/10/external_tools/sessionless_launch",
            )
            self.assertEqual(request.url.params["url"], "https://media.example/lti/launch")
            return httpx.Response(200, json={"url": "https://media.example/signed-launch"})

        client = self.build_client(httpx.MockTransport(handler))
        launch = client.get_sessionless_launch_url(10, "https://media.example/lti/launch")

        self.assertEqual(launch, "https://media.example/signed-launch")


if __name__ == "__main__":
    unittest.main()
