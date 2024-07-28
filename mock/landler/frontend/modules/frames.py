from landler.stack.entities import Module
from blogs.frontend.entities import Route

from sunya import Entity


class Frames(Module):
    class Views:
        class HomePage(Entity):
            pass

    class Routes:
        class HomePageRoute(Route):
            pass


home_page_route = Frames.Routes.HomePageRoute()
