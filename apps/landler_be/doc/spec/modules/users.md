# Module: users

## Users

```python
class Users(DjangoModule):
    class Models:
        class User(Entity):
            email: str
            password: str
            is_authenticated: bool = False
            is_active: bool = False

    class Forms:
        class CreateUserForm:
            email: str
            password: str
            password_confirmation: str

        class SignInUserForm:
            email: str
            password: str

    class DomainEvents:
        class UserCreated:
            user: 'Users.Models.User'

    class ApiViews:
        class SignUpUserApiView:
            pass

        class SignInUserApiView:
            pass

    class Actions:
        class CreateUser:
            pass

        class ActivateUserAccount:
            pass

        class SignInUser:
            pass
```

