import sunya
from sunya import M as m
from sunya import R as r
from sunya import goal, it, the

scenario = sunya.add_scenario(f"mrd1_a_user_signs_up")


def run_scenario():
    r.user = m.External.Actors.User
    r.frontend = m.External.Actors.Frontend
    r.sign_up_user_api_view = m.Users.ApiViews.SignUpUserApiView
    r.create_user_action = m.Users.Actions.CreateUser
    r.activate_user_account_action = m.Users.Actions.ActivateUserAccount
    r.sign_in_user_api_view = m.Users.ApiViews.SignInUserApiView
    r.sign_in_user_action = m.Users.Actions.SignInUser

    with goal().sign_up_and_sign_in(r.user):
        # Sign up
        with the(r.frontend).calls(r.sign_up_user_api_view):
            with it().calls(r.create_user_action).with_the(r.create_user_form):
                it().creates(r.user)

            # Activate user account
            with it().calls(r.activate_user_account_action).with_the(r.user):
                it().activates(r.user)

        # Sign in
        with the(r.frontend).calls(r.sign_in_user_api_view):
            with it().calls(r.sign_in_user_action).with_the(r.sign_in_user_form):
                it().sets_the_current_user_in_the_session_to(r.user)
                it().marks(r.user).as_authenticated()


markdown_node = sunya.add_markdown_node(scenario, "A user signs up")

markdown_node.markdown = """
A user signs up by creating an account, activating it, and signing in. The system creates a new user, activates their account, and signs them in.

### Steps

#### It signs up the user

The frontend calls the sign-up API view.</br>
The API view calls the `CreateUser` action with the `create_user_form`.</br>
The action creates the user.</br>

#### It activates the user account

The sign-up API view calls the `ActivateUserAccount` action with the user.</br>
The action activates the user.</br>

#### It signs in the user

The frontend calls the sign-in API view.</br>
The API view calls the `SignInUser` action with the `sign_in_user_form`.</br>
The action sets the current user in the user session and marks the user as authenticated.</br>

### Diagram

```mermaid
sequenceDiagram
    actor User
    participant Frontend as Frontend
    participant SignUpUserApiView as SignUpUserApiView
    participant CreateUser as CreateUser (action)
    participant ActivateUserAccount as ActivateUserAccount (action)
    participant SignInUserApiView as SignInUserApiView
    participant SignInUser as SignInUser (action)

    Note over Frontend,CreateUser: Sign up
    User->>Frontend: sign up
    Frontend->>SignUpUserApiView: calls
    SignUpUserApiView->>CreateUser: create_user(create_user_form)
    CreateUser->>CreateUser: create user
    CreateUser-->>SignUpUserApiView: user

    Note over SignUpUserApiView,ActivateUserAccount: Activate user
    SignUpUserApiView->>ActivateUserAccount: activate_user_account(user)
    ActivateUserAccount->>ActivateUserAccount: activate user
    ActivateUserAccount-->>SignUpUserApiView:

    Note over Frontend,SignInUser: Sign in
    User->>Frontend: sign in
    Frontend->>SignInUserApiView: calls
    SignInUserApiView->>SignInUser: sign_in_user(sign_in_user_form)
    SignInUser->>SignInUser: set current user in session
    SignInUser->>SignInUser: mark user as authenticated
    SignInUser-->>SignInUserApiView:
```
"""
