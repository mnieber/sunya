import pytest

from checklists.actions.get_or_create_checklist import get_or_create_checklist
from checklists.models import Checklist, ChecklistItem
from users.tests.factories import UserFactory


class TestGetOrCreateChecklistAction:
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_get_or_create_checklist_action_success(self, user):
        # When
        checklist = get_or_create_checklist(user)

        # Then
        assert isinstance(checklist, Checklist)
        assert checklist.owner == user

        # Verify that the correct number of default items were created
        checklist_items = ChecklistItem.objects.filter(checklist=checklist)
        assert checklist_items.count() == 6

        # Verify the content of the default items
        expected_titles = [
            "Welcome",
            "Join the demo org",
            "Add your organization",
            "Create a project",
            "Add a plot",
            "Trigger a project analysis",
        ]
        for item, expected_title in zip(checklist_items, expected_titles):
            assert item.name == expected_title
            assert (
                not item.is_completed
            )  # Check that items are not completed by default

    @pytest.mark.django_db
    def test_get_or_create_checklist_creates_only_one_checklist(self, user):
        # When
        get_or_create_checklist(user)
        get_or_create_checklist(user)

        # Then
        assert Checklist.objects.filter(owner=user).count() == 1

    @pytest.mark.django_db
    def test_get_or_create_checklist_for_different_users(self, user):
        # Given
        another_user = UserFactory()

        # When
        checklist1 = get_or_create_checklist(user)
        checklist2 = get_or_create_checklist(another_user)

        # Then
        assert checklist1.owner == user
        assert checklist2.owner == another_user
        assert Checklist.objects.count() == 2
