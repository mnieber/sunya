from django.core.management.base import BaseCommand, CommandError
from projects.models import Project
from projects.actions.import_spec_files import (
    import_spec_files,
    ImportSpecFilesForm,
    UnknownSpecFileTypeError,
)
import os
import glob


class Command(BaseCommand):
    help = "Import spec files from a specified directory"

    def add_arguments(self, parser):
        parser.add_argument(
            "--spec-files-dir",
            type=str,
            required=True,
            help="Directory containing spec files",
        )
        parser.add_argument(
            "--project-key",
            type=str,
            required=True,
            help="ID of the project to import spec files into",
        )

    def handle(self, *args, **options):
        spec_files_dir = options["spec_files_dir"]
        project_key = options["project_key"]

        if not os.path.isdir(spec_files_dir):
            raise CommandError(
                f"The specified directory does not exist: {spec_files_dir}"
            )

        try:
            project = (
                Project.objects.filter(name=project_key).first()
                or Project.objects.filter(id=project_key).first()
            )
        except Project.DoesNotExist:
            raise CommandError(f"Project with ID or name {project_key} does not exist")

        scenario_files = glob.glob(os.path.join(spec_files_dir, "scenarios", "*.yaml"))
        module_files = glob.glob(os.path.join(spec_files_dir, "modules", "*.yaml"))
        all_files = scenario_files + module_files

        if not all_files:
            self.stdout.write(
                self.style.WARNING("No spec files found in the specified directories.")
            )
            return

        file_objects = []
        for file_path in all_files:
            file_objects.append(open(file_path, "rb"))

        try:
            import_spec_files_form = ImportSpecFilesForm(files=file_objects)
            import_spec_files(import_spec_files_form, project)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully imported {len(all_files)} spec files."
                )
            )
        except UnknownSpecFileTypeError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Failed to import spec files. Unknown file type: {str(e)}"
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Failed to import spec files. Error: {str(e)}")
            )
        finally:
            for f in file_objects:
                f.close()
