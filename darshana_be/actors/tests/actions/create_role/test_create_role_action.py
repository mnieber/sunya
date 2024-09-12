import pytest
from actors.tests.factories import RoleFactory

from actors.actions.create_role import (
    RoleWithNameAlreadyExistsError,
    CreateRoleForm,
    create_role,
)


class TestCreateRoleAction:
    @pytest.mark.django_db
    def test_create_role_action_success(self):
        # Given
        create_role_form = CreateRoleForm(name="test_role")

        # When
        role = create_role(create_role_form)

        # Then
        assert role.name == "test_role"

    @pytest.mark.django_db
    def test_create_role_action_with_existing_name(self):
        # Given
        RoleFactory(name="existing_role")

        create_role_form = CreateRoleForm(name="existing_role")

        # When / Then
        with pytest.raises(RoleWithNameAlreadyExistsError):
            create_role(create_role_form)
