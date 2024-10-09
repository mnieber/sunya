from default.stack.namespace import Module
from default.backend.namespace import Action
from sunya import EntityWithId, actor_to_str, G as g, use_spec
import sunya.spec as spec


class IO(Module):
    @use_spec(spec.backend_model)
    class Models:
        class S3Client(EntityWithId):
            bucket_name: str

        class ExampleRepository(EntityWithId):
            examples: list["IO.Models.Example"] = []

        class Example(EntityWithId):
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

        class UploadExample(Action):
            pass


g.example_repository = IO.Models.ExampleRepository()
g.s3_client = IO.Models.S3Client(bucket_name="geomodel-regression-tests")
g.clear_examples_action = IO.Actions.ClearExamples()
g.download_examples_action = IO.Actions.DownloadExamples()
g.download_example_repository_action = IO.Actions.DownloadExampleRepository()
g.upload_example_action = IO.Actions.UploadExample()


@actor_to_str.method((IO.Models.S3Client,))
def s3_client_to_str(client):
    return f"{client.bucket_name}+:s3_client"
