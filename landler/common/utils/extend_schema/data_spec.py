def resolve_data_spec(data_spec, initial_resolved_data):
    resolved_data = initial_resolved_data.copy()
    unresolved_entries = data_spec.copy()

    def resolve_entry(key, lambda_func):
        var_names = lambda_func.__code__.co_varnames
        args = {
            arg_name: resolved_data[arg_name]
            for arg_name in var_names
            if arg_name in resolved_data
        }
        has_result = len(args) == len(var_names)
        result = lambda_func(**args) if has_result else None
        return result, has_result

    while unresolved_entries:
        resolved_any = False
        for key, lambda_func in list(unresolved_entries.items()):
            result, has_result = resolve_entry(key, lambda_func)
            if has_result:
                resolved_any = True
                resolved_data[key] = result
                del unresolved_entries[key]

        if not resolved_any:
            raise ValueError("Cannot resolve dependencies among data entries")

    return resolved_data


def get_data_kwargs(
    kwarg_names, resolved_data, data_args_not_passed, data_args_never_passed
):
    return {
        arg_name: resolved_data[arg_name]
        for arg_name in kwarg_names
        if arg_name in resolved_data
        and arg_name not in data_args_not_passed
        and arg_name not in data_args_never_passed
    }
