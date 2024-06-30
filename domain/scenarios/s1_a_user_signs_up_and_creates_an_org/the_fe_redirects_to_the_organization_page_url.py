from mock.app import *
from mock.datatypes import *
from sunya import add_step


def the_fe_redirects_to_the_organization_page_url(user, organization):
    with add_step(
        "The",
        user,
        "is redirected to url of the",
        organization_page,
        "which is: ",
        organization_page.url,
    ):
        pass

    request = Request(url="/api/session/set-active-organization")
    with add_step(
        "The",
        frontend,
        "makes a",
        request,
        "to the",
        set_active_organization_api_view,
        "to set",
        organization,
        "as the active organization",
    ):
        with add_step(
            "The",
            set_active_organization_api_view,
            "updates the",
            user_session,
            "to set the active",
            organization,
        ):
            user_session.active_organization = organization
