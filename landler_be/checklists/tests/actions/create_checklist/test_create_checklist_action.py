import pytest
from checklists.actions.create_checklist import create_checklist
from checklists.models import Checklist, ChecklistItem
from users.tests.factories import UserFactory


class TestCreateChecklistAction:
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_create_checklist_action_success(self, user):
        # When
        checklist = create_checklist(user)

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
            assert item.title == expected_title
            assert (
                not item.is_completed
            )  # Check that items are not completed by default

    @pytest.mark.django_db
    def test_create_checklist_creates_only_one_checklist(self, user):
        # When
        create_checklist(user)
        create_checklist(user)

        # Then
        assert Checklist.objects.filter(owner=user).count() == 2

    @pytest.mark.django_db
    def test_create_checklist_for_different_users(self, user):
        # Given
        another_user = UserFactory()

        # When
        checklist1 = create_checklist(user)
        checklist2 = create_checklist(another_user)

        # Then
        assert checklist1.owner == user
        assert checklist2.owner == another_user
        assert Checklist.objects.count() == 2
