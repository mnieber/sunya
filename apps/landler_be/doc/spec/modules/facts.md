# Module: facts

## Facts

```python
class Facts(DjangoModule):
    class Models:
        class Fact(Entity):
            name: 'Facts.Enums.FactNames'
            value: JSON
            created_at: datetime
            source_id: str

    class Enums:
        class FactNames(Enum):
            CARBON_BG: Any = 'carbon_bg'
            WHC: Any = 'whc'
            TEMPERATURE: Any = 'temperature'
```

