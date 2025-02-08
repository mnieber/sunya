@actor_to_str.method((Actors.Models.Actor,))
def actor_to_str(actor):
    name = actor.key.replace(":", "-").replace("+", "-")
    return f"{name}+:actor"


@actor_to_str.method((Projects.Models.Project,))
def project_to_str(project):
    return f"{project.name}+:project"


@actor_to_str.method((Scenarios.Models.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}+:scenario"


@actor_to_str.method((Steps.Models.Step,))
def step_to_str(step):
    return f"{'-'.join(step.fact)}:step"
