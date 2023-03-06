from playwright.sync_api import Page
import pytest
import logging

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """Parse cmd for test instance"""
    parser.addoption(
        "--env",
        action="append",
        default=[],
        help="Execute tests against the specified area. By default on all.",
        choices=("test", "stage", "prod"),
        dest="ENV",
    )


def pytest_generate_tests(metafunc):
    if "env" in metafunc.fixturenames:
        env_area = metafunc.config.option.ENV or ["test", "stage"]
        metafunc.parametrize("env", env_area, scope="session")


@pytest.fixture
def page(page: Page):
    page.route(
        "https://rs.mail.ru/*",
        lambda route: route.abort()
    )
    page.on(
        "request",
        lambda request: logger.critical(
            f"▶ {request.method}, {request.url}"
        ),
    )
    page.on(
        "response",
        lambda response: logger.critical(
            f"◀ {response.status}, {response.url}"
        ),
    )
    yield page
