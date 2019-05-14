# polygonselector
A custom IPywidgets tool for graphically selecting shapely polygons inside a Jupyter notebook.

Installation:

```bash
pip install git+https://github.com/Ricyteach/polygonselector
```

Import into a Jupyter notebook:

```python
from polygonselector import nb_path
%run $nb_path  # imports PolygonSelector class
```

Usage:

```python
import shapely.geometry as geo

some_nodes = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]
some_boxes = []
some_boxes.append([some_nodes[0], some_nodes[3], some_nodes[4], some_nodes[1]])
some_boxes.append([some_nodes[1], some_nodes[4], some_nodes[5], some_nodes[2]])

m_polygon = geo.MultiPolygon(geo.Polygon(box) for box in some_boxes)
poly_selector = PolygonSelector(m_polygon._repr_svg_())
poly_selector  # display the selector below cell, use the tool
```

After using the tool, collect the results:

```python
polygon_indexes = poly_selector.groups_dict.copy()
polygon_indexes
```