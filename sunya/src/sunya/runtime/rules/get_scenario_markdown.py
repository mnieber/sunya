import re


def get_scenario_markdown(scenario):
    markdown = f"# Scenario: {scenario.name}\n\n"

    for node in scenario.nodes:
        markdown_lines = []
        for line in node.markdown.strip().splitlines():
            # skip lines with <remove_line/>
            if "<remove_line/>" in line:
                continue

            # replace <white_space><remove_whitespace/><white_space> with nothing
            regex = r"\s*<remove_whitespace/>\s*"
            line = re.sub(regex, "", line)

            # Update markdown lines
            markdown_lines.append(line)

        markdown_delta = "\n".join(markdown_lines)
        markdown += f"## {node.title}\n\n{markdown_delta}\n\n"

        # Add legend if it exists and is not empty
        if hasattr(node, "legend") and node.legend:
            markdown += "**Legend:**\n\n"
            for role_name, module_path in node.legend.items():
                markdown += f"- {role_name} → {module_path}\n"
            markdown += "\n"

    return markdown
