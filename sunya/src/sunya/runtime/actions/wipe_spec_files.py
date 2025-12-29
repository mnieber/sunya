from sunya.runtime.rules.get_markdown_signature import get_markdown_signature


def wipe_spec_files(file_writer, package):
    for pattern in ["scenarios", "modules"]:
        for file in (file_writer.output_dir / package / pattern).rglob("*.md"):
            # Check whether the first line contains the signature
            with open(file, "r") as f:
                first_line = f.readline().strip()
                if get_markdown_signature().strip() in first_line:
                    file.unlink()
