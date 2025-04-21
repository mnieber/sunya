from sunya import actor_to_str, str_to_uuid
from mock.darshana.frontend.impl.namespace import Actors, Projects, Scenarios, Steps, Users

@actor_to_str.method((Actors.Types.Actor,))
def actor_to_str(actor):
    name = actor.key.replace(":", "-").replace("+", "-")
    return f"{name}+:actor"


@actor_to_str.method((Projects.Types.Project,))
def project_to_str(project):
    return f"{project.name}+:project"


@actor_to_str.method((Scenarios.Types.Scenario,))
def scenario_to_str(scenario):
    return f"{scenario.name}+:scenario"


@actor_to_str.method((Steps.Types.Step,))
def step_to_str(step):
    id = str_to_uuid("-".join(step.fact))
    return f"{"-".join(step.fact)}:step"

@actor_to_str.method((Users.Types.User,))
def user_to_str(user):
    return f"{user.email}+:user"
