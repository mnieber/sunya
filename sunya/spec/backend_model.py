from sunya.utils import extract_field_types


def backend_model(model_class):
    return dict(
        name=model_class.__name__,
        fields=[
            dict(name=field_name, type=field_type)
            for field_name, field_type in extract_field_types(model_class).items()
        ],
    )
