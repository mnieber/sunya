# Django models

The Models section of a module describes the Django models that are based on the entities in the roadmap. This section is declared implicitly in scenario specs by referencing `m.<Module>.DjangoModels.<ModelName>`.

# ApiViews

The ApiView section describes the api views. This section is declared implicitly in scenario specs by referencing `m.<Module>.ApiViews.<ViewName>`.

# Domain events

The DomainEvents section describes the domain events that would be interesting to send from the action functions.
The purpose of domain events is to inform external observers about what is going on in the system.
This section is declared implicitly in scenario specs by referencing `m.<Module>.DomainEvents.<EventName>`.
