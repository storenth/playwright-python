from .navigation import Navigation
from .config import get_url

def test_should_allow_navigation(page, env):
    nav = Navigation(page, env)
    nav.navigate()
    nav.page.goto(get_url(env))
    
    page.goto(get_url(env))
    nav.navigate()
    page.goto(get_url(env))
