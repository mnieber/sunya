from mock.entities.react_app.namespace import Route, ReactModule

from sunya import Entity


class Frames(ReactModule):
    class Views:
        class HomePage(Entity):
            pass

    class Routes:
        class HomePageRoute(Route):
            pass
