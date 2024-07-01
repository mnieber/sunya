def create_superuser(email=None, password=None, **extra_fields):
    from users.models import User

    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    extra_fields.setdefault("is_active", True)

    if not email:
        raise ValueError("The given email must be set")
    email = User.objects.normalize_email(email)

    user = User(email=email, **extra_fields)

    if not password:
        user.set_unusable_password()
    else:
        user.set_password(password)

    user.save(using=User.objects._db)
    return user
