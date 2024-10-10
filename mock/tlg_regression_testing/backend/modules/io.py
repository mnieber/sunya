from default.stack.namespace import Module
from default.backend.namespace import Action, Model
from sunya import actor_to_str, G as g, use_spec
import sunya.spec as spec


class IO(Module):
    @use_spec(spec.backend_model)
    class Models:
        class S3Client(Model):
            bucket_name: str

        class ExampleRepository(Model):
            geomodel_name: str
            examples: list["IO.Models.Example"] = []

        class ExampleRepositoryStat(Model):
            nr_of_stored_examples_by_selector_name: dict[str, int]

        class Example(Model):
            selector_name: str
            hash: str
            slot_nr: int
            input_json: str
            output_json: str

    @use_spec(spec.backend_action)
    class Actions:
        class ClearExamples(Action):
            pass

        class DownloadExamples(Action):
            pass

        class DownloadExampleRepository(Action):
            pass

        class DownloadExampleRepositoryStat(Action):
            pass

        class UploadExample(Action):
            pass


g.s3_client = IO.Models.S3Client(bucket_name="geomodel-regression-tests")
g.clear_examples_action = IO.Actions.ClearExamples()
g.download_examples_action = IO.Actions.DownloadExamples()
g.download_example_repository_action = IO.Actions.DownloadExampleRepository()
g.download_example_repository_stat_action = IO.Actions.DownloadExampleRepositoryStat()
g.upload_example_action = IO.Actions.UploadExample()


@actor_to_str.method((IO.Models.S3Client,))
def s3_client_to_str(client):
    return f"{client.bucket_name}+:s3_client"
