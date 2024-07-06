# Step 2: The scenario description step

The application must support the following scenarios:

# a-user-schedules-a-project-analysis

# the [:frontend] call the [create_project_analysis_job:api-view] to create a [my-project+:project-analysis-job]

The following actors are created in this step:

my-project+:project-analysis-job:
is_active=True
project=my-project+:project
project_analyses=[]
repeats_every=None
scheduled_at=2024-07-07 15:55:34.312478



## The [create_project_analysis_job:api-view] calls the [create_project_analysis_job:action] to create a [my-project+:project-analysis-job]

The following actors are created in this step:

my-project+:project-analysis-job:
is_active=True
project=my-project+:project
project_analyses=[]
repeats_every=None
scheduled_at=2024-07-07 15:55:34.312478



### The [create_project_analysis_job:action] creates the [my-project+:project-analysis-job]

The following actors are created in this step:

my-project+:project-analysis-job:
is_active=True
project=my-project+:project
project_analyses=[]
repeats_every=None
scheduled_at=2024-07-07 15:55:34.312478



# the [:project-analysis-queue] finds [jobs_to_run+:list]

The following actors are created in this step:

jobs_to_run+:list:
items=['my-project+:project-analysis-job']
name=jobs_to_run



# the [:project-analysis-queue] runs the first [my-project+:project-analysis-job]


The following actors are updated in this step:

The my-project+:project-analysis-job:
project_analyses=['my-project+:project-analysis'] (from [])


## The [:project-analysis-queue] calls the [create_project_analysis:action] to create a [my-project+:project-analysis] from a [my-project+:project-analysis-job]

The following actors are created in this step:

my-project+:project-analysis:
id=98a05401-e76e-5e9c-bd3f-d15b567d1dce
job=my-project+:project-analysis-job
now=2024-07-07 15:55:34.312478
plot_analyses=['my-plot@2024-07-07 15:55:34.312478+:plot-analysis']
project=my-project+:project
status=running


The following actors are updated in this step:

The my-project+:project-analysis-job:
project_analyses=['my-project+:project-analysis'] (from [])


### the [create_project_analysis:action] gets the [my-project+:project] at the now ts of the [my-project+:project-analysis]



### the [create_project_analysis:action] loops over all plots in the [my-project+:project]



#### the [create_project_analysis:action] creates a [my-plot@2024-07-07 15:55:34.312478+:plot-analysis] for the [my-plot@0+:plot]

The following actors are created in this step:

my-plot@2024-07-07 15:55:34.312478+:plot-analysis:
id=dcb93e006561463c8fc18d4e3278a9e2
now=2024-07-07 15:55:34.312478
plot=my-plot@0+:plot
project_analysis=my-project+:project-analysis
status=running



## the [:project-analysis-queue] calls the [run_project_analysis:action]



### the [run_project_analysis:action] calls the [run_plot_analysis:action] on a [my-plot@2024-07-07 15:55:34.312478+:plot-analysis] in the [my-project+:project-analysis]



#### the [run_plot_analysis:action] creates a [dcb93e006561463c8fc18d4e3278a9e2+:calcium-plot-analysis-job] for the [my-plot@0+:plot] at the now timestamp of the [my-plot@2024-07-07 15:55:34.312478+:plot-analysis]

The following actors are created in this step:

dcb93e006561463c8fc18d4e3278a9e2+:calcium-plot-analysis-job:
id=dcb93e006561463c8fc18d4e3278a9e2
polygon=+:polygon



