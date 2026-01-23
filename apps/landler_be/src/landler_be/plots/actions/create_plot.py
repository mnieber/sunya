import uuid
from dataclassy import dataclass
from django.db import transaction

from polygons.models import Polygon
from organizations.models import Organization
from plot_questionnaires.models import PlotQuestionnaire
from domain_events.rules.reconstruct_entity import reconstruct_entity
import plots.domain_events as domain_events


@dataclass
class CreatePlotForm:
    name: str
    polygon_id: str
    plot_questionnaire_id: str


def create_plot(
    create_plot_form: CreatePlotForm,
    polygon: Polygon,
    plot_questionnaire: PlotQuestionnaire,
    owner: Organization,
) -> str:
    # Generate a new plot ID
    plot_id = str(uuid.uuid4())

    # Create event for plot fields update
    with transaction.atomic():
        domain_events.create_update_plot_fields_event(plot_id, create_plot_form.name)
        domain_events.create_update_plot_owner_event(plot_id, owner.id)
        domain_events.create_update_plot_polygon_event(plot_id, polygon.id)
        domain_events.create_update_plot_questionnaire_event(
            plot_id, plot_questionnaire.id
        )

    # Reconstruct the plot entity from the domain events
    reconstructed_plot = reconstruct_entity(entity_id=plot_id)

    return reconstructed_plot
