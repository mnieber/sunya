from landler.backend.app import *
from landler.frontend.app import *
from sunya import register


def set_active_organization_request_():
    return register(
        Request(endpoint="set-active-organization"),
        name="set_active_organization_request",
    )


def admin_membership_(e):
    return Organizations.Models.OrganizationMembership(
        organization=e.organization,
        user=user_session.user,
        role=Organizations.Enums.UserInOrganizationRoles.ADMIN,
    )


def organization_(e):
    return register(
        Organizations.Models.Organization(name="my-org"),
        e.organization,
    )


def create_organization_form_(e):
    return register(
        Form(name="CreateOrganizationForm", data=e.request.data),
        name="create_organization_form",
    )


def create_organization_request_():
    return register(
        Request(endpoint="create-organization"), name="create_organization_request"
    )


def sign_in_request_():
    return register(Request(endpoint="sign-in"), "sign_in_request")


def sign_up_request_():
    return register(Request(endpoint="sign-up"), name="sign_up_request")


def create_user_form_(e):
    return register(
        Form(name="CreateUserForm", data=e.request.data),
        name="create_user_form",
    )


def user_(e):
    return register(
        Users.Models.User(
            email="my-org-owner@example.com",
            password="my-password",
        ),
        e.user,
    )
