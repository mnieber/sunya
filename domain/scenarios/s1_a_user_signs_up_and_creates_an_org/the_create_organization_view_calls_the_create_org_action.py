from mock.app import *
from mock.datatypes import *
from sunya import add_step, register


def the_fe_posts_to_create_an_org(p_organization):
    request = Request(url="/api/organizations/create-organization/")
    with add_step(
        "The",
        user_account_page,
        "makes a",
        request,
        "to the",
        create_organization_api_view,
        "to create an",
        p_organization,
    ):
        create_organization_form = Form(
            name="CreateOrganizationForm", data=request.data
        )

        with add_step(
            "The",
            create_organization_api_view,
            "calls the",
            create_organization_action,
            "with the",
            create_organization_form,
            "to create a",
            p_organization,
            "with admin",
            user_session.user,
        ):
            with add_step(
                "The", create_organization_action, "creates the", p_organization
            ):
                organization = register(
                    Organizations.Models.Organization(
                        id="4b3d6a69-7653-5dcd-bbce-0ed03d1ce2b0", name="my-org"
                    ),
                    p_organization,
                )

            with add_step(
                "The",
                create_organization_action,
                "calls the",
                add_user_to_organization_action,
                "to add the",
                user_session.user,
                "to the",
                organization,
            ):
                organization.memberships = [
                    Organizations.Models.OrganizationMembership(
                        organization=organization,
                        user=user_session.user,
                        role=Users.Enums.UserRoles.ADMIN,
                    )
                ]

    return organization
