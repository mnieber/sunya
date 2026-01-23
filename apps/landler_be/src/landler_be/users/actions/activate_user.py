def activate_user(user):
    user.is_active = True
    user.save()
