from sunya import Entity, Fn, Value, actor_to_str
from sunya.utils.case import get_type_name


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
        infix = "" if self.host.endswith("/") or self.path.startswith("/") else "/"
        return f"{self.host}{infix}{self.path}"


@actor_to_str.method((Module,))
def module_to_str(module):
    return f"{get_type_name(module)}:module"


@actor_to_str.method((Form,))
def form_to_str(form):
    return f"{form.name}:form"


@actor_to_str.method((Enum,))
def enum_to_str(enum):
    return f"{get_type_name(enum)}:enum"


@actor_to_str.method((Action,))
def action_to_str(action):
    return f"{get_type_name(action)}:action"


@actor_to_str.method((ApiView,))
def api_view_to_str(api_view):
    return f"{get_type_name(api_view)}:api-view"


@actor_to_str.method((Page,))
def page_to_str(page):
    return f"{page.url}+:page"


@actor_to_str.method((Request,))
def request_to_str(request):
    return f"{request.url}:request"
