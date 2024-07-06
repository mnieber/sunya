1 Models

1.1 Model: User

id: UUID
email: str
password: str
is_authenticated: bool
is_active: bool

2 Enums

3 Actions

3.1 Action: create_user

Arguments:
create_user_form: Form

3.2 Action: sign_in_user

Arguments:
sign_in_user_form: Form

4 Api views

4.1 Api view: SignUpUserApiView


4.2 Api view: SignInUserApiView


4.3 Api view: SetActiveOrganizationApiView


