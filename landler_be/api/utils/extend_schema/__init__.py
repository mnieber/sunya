from drf_spectacular.utils import extend_schema as drf_extend_schema
from rest_framework.response import Response

from api.utils.extend_schema.data_spec import get_data_kwargs, resolve_data_spec
from api.utils.extend_schema.permissions import (  # noqa: F401
    PermissionResult,
    allow,
    check_permission_spec,
    deny,
    get_permissions_description,
    parse_permission_spec,
)


def extend_schema(
    *args,
    data=None,
    permissions=None,
    data_args_not_passed=None,
    request_arg_pos=1,
    **kwargs,
):
    serializer_class = kwargs.get("request")

    def wrapper(f):
        def wrapped_f(*args, **kwargs):
            request = (
                args[request_arg_pos] if request_arg_pos != -1 else kwargs["request"]
            )
            initial_resolved_data = kwargs.copy()
            if request:
                initial_resolved_data["user"] = request.user
                if serializer_class:
                    serializer = serializer_class(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    request_data = serializer.validated_data
                    initial_resolved_data.update(request_data.__dict__)
                else:
                    request_data = None

            resolved_data = resolve_data_spec(data or {}, initial_resolved_data)
            for permission_spec in permissions or []:
                error_code, permission_fn, reason = parse_permission_spec(
                    permission_spec
                )
                permission_result = check_permission_spec(permission_fn, resolved_data)
                assert isinstance(permission_result, PermissionResult)
                if not permission_result.permission_allowed:
                    return Response(
                        dict(detail=reason or permission_result.reason),
                        status=error_code,
                    )

            data_kwargs = get_data_kwargs(
                f.__code__.co_varnames,
                resolved_data,
                data_args_not_passed or [],
                ["serializer", "user"],
            )

            return f(
                *args,
                request_data=request_data,
                **data_kwargs,
                **({k: v for k, v in kwargs.items() if k not in data_kwargs}),
            )

        wrapped_f.permissions = permissions

        return drf_extend_schema(**kwargs)(wrapped_f)

    return wrapper
