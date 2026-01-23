from domain_events.actions.create_domain_event import create_domain_event

SCHEMA_VERSION = "1.0.0"


def create_update_plot_questionnaire_event(plot_id, plot_questionnaire_id):
    return create_domain_event(
        type_name="update_plot_questionnaire",
        schema_version=SCHEMA_VERSION,
        payload={
            "plot_id": plot_id,
            "plot_questionnaire_id": str(plot_questionnaire_id),
        },
        entity_ids=[plot_id],
    )


def create_update_plot_polygon_event(plot_id, polygon_id):
    return create_domain_event(
        type_name="update_plot_polygon",
        schema_version=SCHEMA_VERSION,
        payload={
            "plot_id": plot_id,
            "polygon_id": str(polygon_id),
        },
        entity_ids=[plot_id],
    )


def create_update_plot_owner_event(plot_id, owner_id):
    return create_domain_event(
        type_name="update_plot_owner",
        schema_version=SCHEMA_VERSION,
        payload={
            "plot_id": plot_id,
            "owner_id": str(owner_id),
        },
        entity_ids=[plot_id],
    )


def create_update_plot_fields_event(plot_id, name):
    return create_domain_event(
        type_name="update_plot_fields",
        schema_version=SCHEMA_VERSION,
        payload={
            "plot_id": plot_id,
            "name": name,
            "is_draft": True,  # New plots are created as drafts by default
        },
        entity_ids=[plot_id],
    )
