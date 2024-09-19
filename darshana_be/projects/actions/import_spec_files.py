import yaml
import typing as T
from dataclassy import dataclass

from django.db import transaction
from projects.models import Project
from scenarios.models import Scenario
from projects.actions.import_scenario_spec import (
    import_scenario_spec,
    ImportScenarioSpecForm,
)


@dataclass
class ImportSpecFilesForm:
    files: T.List[T.Any]


def import_spec_files(import_spec_files_form: ImportSpecFilesForm, project: Project):
    with transaction.atomic():
        _delete_project_data(project)

        for file in import_spec_files_form.files:
            content = file.read().decode("utf-8")
            data = yaml.safe_load(content)

            if "scenario_name" in data:
                _process_scenario_spec(data, project)
            elif "name" in data:
                _process_module_spec(data, project)
            else:
                raise UnknownSpecFileTypeError(file.name)


def _delete_project_data(project: Project):
    Scenario.objects.filter(project=project).delete()


def _process_scenario_spec(data: dict, project: Project):
    import_scenario_spec_form = ImportScenarioSpecForm(scenario_data=data)
    import_scenario_spec(import_scenario_spec_form, project)


def _process_module_spec(data: dict, project: Project):
    # TODO: Implement actual module spec processing
    pass


class UnknownSpecFileTypeError(ValueError):
    pass
