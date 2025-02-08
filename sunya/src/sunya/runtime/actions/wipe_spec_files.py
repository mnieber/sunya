def wipe_spec_files(file_writer):
    for prefix in ["backend", "frontend"]:
        for pattern in ["scenarios"]:
            for file in (file_writer.output_dir / prefix / pattern).rglob("*.yaml"):
                file.unlink()
