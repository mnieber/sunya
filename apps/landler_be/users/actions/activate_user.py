from checklists.actions.get_or_create_checklist import get_or_create_checklist


def activate_user(user, get_or_create_checklist_cb=get_or_create_checklist):
    user.is_active = True
    user.save()

    get_or_create_checklist_cb(user)
