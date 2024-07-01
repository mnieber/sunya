0 SPEC comments.

This module specification section contains comments that start with the 'SPEC' keyword.
These comments are meant to guide the source code generation process. They are not part of the actual spec.

1 Models

1.1 Model: User

A Django model that contains a user

Fields:
email: str

2 Actions

2.1 Action: create_user

Arguments:
create_user_form: Form

3 API Views

3.1 API View: RegisterUserApiView

An API view that registers a user

4 Scenarios

4.1 Scenario: A user registers

```
# The [:frontend] calls the [register_user_api_view:api-view]

## The [register_user_api_view:api-view] calls the [create_user:action] to create an [my-org-owner@example.com+:user]

The following actors are created in this step:

my-org-owner@example.com+:user:
email=my-org-owner@example.com

### The [create_user:action] validates the email of the [my-org-owner@example.com+:user]

## The [register_user_api_view:api-view] calls the [create_organization:action] to create a [my-org+:organization] with owner [my-org-owner@example.com+:user]

The following actors are created in this step:

[my-org+:organization]:
name=my-org
owner=[my-org-owner@example.com+:user]

## The [register_user_api_view:api-view] calls the [add_user_to_organization:action] to add the [my-org-owner@example.com+:user] to the [my-org+:organization]
```
