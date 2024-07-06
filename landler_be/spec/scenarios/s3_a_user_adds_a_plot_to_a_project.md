Scenario: a-user-adds-a-plot-to-a-project



# The [:frontend] calls the [create_plot:api-view]

## The [create_plot:api-view] calls the [create_plot:action] with the [create_plot_-:form] to create a [my-plot@0+:plot] in the [my-project+:project]

The following actors are created in this step:

my-plot@0+:plot:
errors=[]
is_draft=False
name=my-plot
owner=my-org+:organization
plot_questionnaire=my-plot+:plot-questionnaire
polygon=+:polygon
sequence_number=1

The following actors are updated in this step:

The my-project+:project:
plot_lists=['default+:plotList'] (from [])

### The [create_plot:action] creates the [my-plot@0+:plot]

The following actors are created in this step:

my-plot@0+:plot:
errors=[]
is_draft=False
name=my-plot
owner=my-org+:organization
plot_questionnaire=my-plot+:plot-questionnaire
polygon=+:polygon
sequence_number=1

### The [create_plot:action] calls the [add_plot_to_project:action] to add the [my-plot@0+:plot] to the [my-project+:project]

The following actors are updated in this step:

The my-project+:project:
plot_lists=['default+:plotList'] (from [])


