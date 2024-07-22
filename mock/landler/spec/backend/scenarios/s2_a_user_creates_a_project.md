Scenario: a-user-creates-a-project (s2_a_user_creates_a_project.md)



# The [:frontend] calls the [create_project:api-view]

## The [create_project:api-view] calls the [create_project:action] with the [create_project_-:form] to create a [my-project+:project] with admin [my-org+:organization]

After this step, the following actors will have been created with the following values:

my-project+:project:
memberships=['(my-project)-(my-org)-(admin)+:project-membership']
name=my-project
plot_lists=[]

### The [create_project:action] creates the [my-project+:project]

After this step, the following actors will have been created with the following values:

my-project+:project:
memberships=[]
name=my-project
plot_lists=[]

### The [create_project:action] calls the [add_organization_to_project:action] to add the [my-org+:organization] to the [my-project+:project]

After this step, the following actors will have been updated to the following values:

The my-project+:project:
memberships=['(my-project)-(my-org)-(admin)+:project-membership'] (from [])


