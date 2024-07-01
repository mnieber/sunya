import pytest

from users.actions.create_user import (
    CreateUserForm,
    UserWithEmailAlreadyExistsError,
    create_user,
)
from users.tests.factories import UserFactory


class TestCreateUserAction:
    @pytest.mark.django_db
    def test_create_user_success(self):
        # Given
        create_user_form = CreateUserForm(email="me@example.org")

        # When
        user = create_user(create_user_form)

        # Then
        assert user.email == create_user_form.email

    @pytest.mark.django_db
    def test_create_user_with_existing_email(self):
        # Given
        UserFactory(email="me@example.org")
        create_user_form = CreateUserForm(email="me@example.org")

        # When
        with pytest.raises(UserWithEmailAlreadyExistsError):
            create_user(create_user_form)
