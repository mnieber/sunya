from default.stack.namespace import Module
from default.frontend.entities import Route

from sunya import Entity, G as g


class Frames(Module):
    class Views:
        class HomePage(Entity):
            pass

    class Routes:
        class HomePageRoute(Route):
            pass


g.home_page_route = Frames.Routes.HomePageRoute()
