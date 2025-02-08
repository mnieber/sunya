import pytest

from checklists.actions.update_checklist_item import update_checklist_item
from checklists.enums import ChecklistItemNames
from checklists.models import ChecklistItem
from users.tests.factories import UserFactory


class TestUpdateChecklistItemAction:
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.mark.django_db
    def test_update_checklist_item_action_success(self, user):
        # Given
        checklist_item = ChecklistItem.objects.get(
            checklist__owner=user, name=ChecklistItemNames.WELCOME
        )
        assert not checklist_item.is_completed

        # When
        updated_item = update_checklist_item(
            user=user, checklist_item_name=ChecklistItemNames.WELCOME, is_completed=True
        )

        # Then
        assert updated_item.is_completed
        assert updated_item.id == checklist_item.id

        # Verify the item is updated in the database
        checklist_item.refresh_from_db()
        assert checklist_item.is_completed
