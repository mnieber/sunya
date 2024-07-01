0 SPEC comments.

This module specification section contains comments that start with the 'SPEC' keyword.
These comments are meant to guide the source code generation process. They are not part of the actual spec.

1 Models

1.1 Model: Organization

A Django model that contains a organization

Fields:
name: str
owner: User

2 Actions

2.1 Action: create_organization

Arguments:
create_organization_form: Form

2.2 Action: add_user_to_organization

Arguments:
organization: Organization
user: User
