# Module: polygons

## Polygons

```python
class Polygons(DjangoModule):
    class Models:
        class Polygon(Entity):
            polygon: JSON
            crc: str
            area: float

    class Actions:
        class CreatePolygon:
            class Args:
                create_polygon_form: Form
```

