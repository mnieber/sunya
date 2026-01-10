# Module: calculations

## Calculations

```python
class Calculations(DjangoModule):
    class Models:
        class Calculation(Entity):
            name: 'Calculations.Enums.CalculationNames'
            source_id: str
            required_fact_names: list[str] = []
            provided_fact_names: list[str] = []

        class CoolfarmToolCO2Calculation(Calculation):
            geomodel_version: str

    class Enums:
        class CalculationNames(Enum):
            CoolfarmToolCO2: Any = 'coolfarm_tool_co2'
```

