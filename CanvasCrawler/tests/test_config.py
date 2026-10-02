from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from canvas_crawler.config import Settings
from canvas_crawler.exceptions import ConfigurationError


class SettingsTests(unittest.TestCase):
    @patch.dict(
        os.environ,
        {
            "CANVAS_BASE_URL": "https://canvas.example.edu/",
            "CANVAS_ACCESS_TOKEN": "secret",
            "CANVAS_PER_PAGE": "50",
            "CANVAS_REQUEST_TIMEOUT_SECONDS": "15",
        },
        clear=True,
    )
    def test_loads_and_normalizes_environment(self) -> None:
        settings = Settings.from_env(env_file="does-not-exist.env")

        self.assertEqual(settings.base_url, "https://canvas.example.edu")
        self.assertEqual(settings.per_page, 50)
        self.assertEqual(settings.timeout_seconds, 15.0)

    @patch.dict(
        os.environ,
        {"CANVAS_BASE_URL": "https://canvas.example.edu", "CANVAS_ACCESS_TOKEN": ""},
        clear=True,
    )
    def test_rejects_missing_token(self) -> None:
        with self.assertRaises(ConfigurationError):
            Settings.from_env(env_file="does-not-exist.env")


if __name__ == "__main__":
    unittest.main()
