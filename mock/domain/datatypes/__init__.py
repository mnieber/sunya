from sunya import Entity, Fn, Value, actor_to_str, shorten_term_str
from sunya.utils.case import camel_to_snake, l0, snake_name_from_instance


class Module(Entity):
    pass


class Form(Entity):
    name: str
    data: dict


class Enum(Value):
    name: str


class JSON(Value):
    data: str = ""


class Action(Fn):
    pass


class ApiView(Entity):
    pass


class Request(Entity):
    url: str
    data: dict = {}


class Page(Entity):
    host: str
    path: str

    @property
    def url(self):
        return f"{self.host}/{self.path}"


@actor_to_str.method((Module,))
def module_to_str(module):
    return f"{snake_name_from_instance(module)}:module"


@actor_to_str.method((Form,))
def form_to_str(form):
    return shorten_term_str(f"{l0(camel_to_snake(form.name))}:form")


@actor_to_str.method((Enum,))
def enum_to_str(enum):
    return f"{snake_name_from_instance(enum)}:enum"


@actor_to_str.method((Action,))
def action_to_str(action):
    return shorten_term_str(f"{snake_name_from_instance(action)}:action")


@actor_to_str.method((ApiView,))
def api_view_to_str(api_view):
    return shorten_term_str(f"{snake_name_from_instance(api_view)}:api-view")


@actor_to_str.method((Page,))
def page_to_str(page):
    return f"{page.url}:page"


@actor_to_str.method((Request,))
def request_to_str(request):
    return f"{request.url}:request"
