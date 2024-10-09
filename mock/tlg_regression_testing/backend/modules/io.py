from default.stack.namespace import Module, Function
from sunya import EntityWithId, actor_to_str, G as g


class IO(Module):
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

    class Classes:
        class IO:
            clear_examples_function = Function(name="clear_examples", container="io")
            download_examples_function = Function(
                name="download_examples", container="io"
            )
            download_summary_function = Function(
                name="download_summary", container="io"
            )
            upload_example_function = Function(name="upload_example", container="io")


g.io = IO.Classes.IO()
g.example_repository = IO.Models.ExampleRepository()
g.s3_client = IO.Models.S3Client(bucket_name="geomodel-regression-tests")


@actor_to_str.method((IO.Models.S3Client,))
def s3_client_to_str(client):
    return f"{client.bucket_name}+:s3_client"
