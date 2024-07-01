from domain.app import *
from domain.datatypes import *
from sunya import add_step


def the_create_project_view_creates_a_project(user, project):
    add_step(
        "The",
        create_project_api_view,
        "calls the",
        create_project_action,
        "to create a",
        project,
        "with owner",
        user,
    )
