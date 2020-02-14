# polygonselector
A custom plotly tool for graphically selecting shapely polygons.

Installation:

```bash
pip install git+https://github.com/Ricyteach/polygonselector
```

Usage:

```python
import shapely.geometry as geo

some_nodes = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]
some_boxes = []
some_boxes.append([some_nodes[0], some_nodes[3], some_nodes[4], some_nodes[1]])
some_boxes.append([some_nodes[1], some_nodes[4], some_nodes[5], some_nodes[2]])

```

API TBD