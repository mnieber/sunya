import pytest
from checklists.actions.update_checklist_item import update_checklist_item
from checklists.models import Checklist, ChecklistItem
from checklists.enums import ChecklistItemNames
from users.tests.factories import UserFactory


class TestUpdateChecklistItemAction:
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def checklist(self, user):
        return Checklist.objects.create(owner=user)

    @pytest.fixture
    def checklist_item(self, checklist):
        return ChecklistItem.objects.create(
            checklist=checklist, title=ChecklistItemNames.WELCOME, is_completed=False
        )

    @pytest.mark.django_db
    def test_update_checklist_item_action_success(self, user, checklist_item):
        # Given
        assert not checklist_item.is_completed

        # When
        updated_item = update_checklist_item(
            user=user, checklist_item_name=ChecklistItemNames.WELCOME, is_completed=True
        )

        # Then
        assert updated_item.is_completed
        assert updated_item.id == checklist_item.id

        # Verify the item is updated in the database
        refreshed_item = ChecklistItem.objects.get(id=checklist_item.id)
        assert refreshed_item.is_completed

    @pytest.mark.django_db
    def test_update_checklist_item_action_wrong_user(self, checklist_item):
        # Given
        another_user = UserFactory()

        # When / Then
        with pytest.raises(ChecklistItem.DoesNotExist):
            update_checklist_item(
                user=another_user,
                checklist_item_name=ChecklistItemNames.WELCOME,
                is_completed=True,
            )
