from checklists.actions.create_checklist import create_checklist


def activate_user(user, create_checklist_cb=create_checklist):
    user.is_active = True
    user.save()

    create_checklist_cb(user)
