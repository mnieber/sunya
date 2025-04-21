from sunya import actor_to_str

from mock.tlg_regression_testing.backend.impl.namespace import IO, Run, Selectors


@actor_to_str.method((IO.Models.S3Client,))
def s3_client_to_str(client):
    return f"{client.bucket_name}+:s3_client"


@actor_to_str.method((Run.Models.TestResult,))
def test_result_to_str(result):
    return f"{result.selector}-{result.input_id}+:test_result"


@actor_to_str.method((Selectors.Models.Selector,))
def selector_to_str(selector):
    return f"{selector.name}+:selector"


@actor_to_str.method((Selectors.Models.SelectorsRepository,))
def selectors_repository_to_str(repo):
    return "selectors_repository+:selectors_repository"
