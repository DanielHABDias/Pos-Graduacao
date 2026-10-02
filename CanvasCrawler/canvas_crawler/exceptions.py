"""Exceções de domínio do CanvasCrawler."""


class CanvasCrawlerError(Exception):
    """Erro esperado que pode ser apresentado diretamente ao usuário."""


class ConfigurationError(CanvasCrawlerError):
    """Configuração local ausente ou inválida."""


class AuthenticationError(CanvasCrawlerError):
    """O Canvas recusou as credenciais informadas."""


class CanvasApiError(CanvasCrawlerError):
    """A API do Canvas respondeu com erro ou não pôde ser acessada."""
