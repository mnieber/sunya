g.s3_client = IO.Models.S3Client(bucket_name="geomodel-regression-tests")
g.clear_examples_action = IO.Actions.ClearExamples()
g.download_examples_action = IO.Actions.DownloadExamples()
g.download_example_repository_action = IO.Actions.DownloadExampleRepository()
g.download_example_repository_stat_action = IO.Actions.DownloadExampleRepositoryStat()
g.upload_example_action = IO.Actions.UploadExample()

g.run_regression_tests_action = Run.Actions.RunRegressionTests()
g.generate_html_report_action = Run.Actions.GenerateHtmlReport()

g.selectors_repository = Selectors.Models.SelectorsRepository()
g.register_selector_action = Selectors.Actions.RegisterSelector()
