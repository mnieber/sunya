g.create_actor_action = Actors.Actions.CreateActor()

g.create_project_action = Projects.Actions.CreateProject()
g.update_project_action = Projects.Actions.UpdateProject()
g.delete_projects_action = Projects.Actions.DeleteProjects()
g.import_spec_files_action = Projects.Actions.ImportSpecFiles()
g.import_scenario_spec_action = Projects.Actions.ImportScenarioSpec()
g.import_module_spec_action = Projects.Actions.ImportModuleSpec()
g.create_project_api_view = Projects.ApiViews.CreateProject()
g.update_project_api_view = Projects.ApiViews.UpdateProject()
g.delete_projects_api_view = Projects.ApiViews.DeleteProjects()
g.upload_spec_files_api_view = Projects.ApiViews.ImportSpecFiles()
g.get_project_api_view = Projects.ApiViews.GetProject()
g.get_project_leads_api_view = Projects.ApiViews.GetProjectLeads()

g.create_scenario_action = Scenarios.Actions.CreateScenario()

g.create_step_action = Steps.Actions.CreateStep()
