from .config import get_url

class Navigation:
    """Веб-приложение КФ"""
    CIRCULAR_LOADER = '[id="loader"]'

    def __init__(self, page, env):
        self.page = page
        self.env = env
        self.loader = page.locator(Navigation.CIRCULAR_LOADER)

    def navigate(self, path=""):
        self.page.goto(
            "".join([get_url(self.env), path]),
            wait_until="domcontentloaded",
        )

        self.page.locator(Navigation.CIRCULAR_LOADER).wait_for(
            state='hidden', timeout=15_000
        )
        return self
