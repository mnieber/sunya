from landler.backend.app import *
from sunya import add_step, register


def the_fe_posts_to_sign_up_a_user(p_user):
    request = Request(url="/api/accounts/sign-up/")

    with add_step(
        "The",
        sign_up_page,
        "makes a",
        request,
        "to the",
        sign_up_user_api_view,
    ):
        create_user_form = Form(name="CreateUserForm", data=request.data)
        with add_step(
            "The",
            sign_up_user_api_view,
            "calls the",
            create_user_action,
            "with the",
            create_user_form,
            "to create a",
            p_user,
        ):
            with add_step(
                "The",
                create_user_action,
                "validates the email and password of the",
                create_user_form,
            ):
                pass

            with add_step("The", create_user_action, "creates the", p_user):
                user = register(
                    Users.Models.User(
                        email="my-org-owner@example.com",
                        password="my-password",
                    ),
                    p_user,
                )

        with add_step(
            "The",
            sign_up_user_api_view,
            "activates the account of the",
            user,
        ):
            user.is_active = True

    return user
