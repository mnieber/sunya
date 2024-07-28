import yaml


class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def dict2yaml(x):
    return yaml.dump(
        x, Dumper=MyDumper, default_flow_style=False, sort_keys=False, width=1000
    )
