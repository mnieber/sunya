def delete_user(user, using=None):
    """
    a user can only be deleted, if he is not an organization owner
    """
    if user.memberships.filter(organization__owner_user=user).exists():
        raise ValueError("Cannot delete user. User is a organization owner.")
    user._delete(using=using)
