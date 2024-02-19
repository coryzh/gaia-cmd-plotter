# gaia-cmd-plotter

`gaia_cmd_plotter` is a Python package for creating customized Matplotlib axes that display a Gaia Color-Magnitude
Diagram (CMD) background. This package is useful for visualising astronomical data within the context of a Gaia CMD.

## Installation

You can install gaia_cmd_plotter using `pip`:

```bash
pip install gaia-cmd-plotter
```

## Usage

To use the package, first import the `GaiaCMDAxis` class from the `gaia_cmd_plotter.gaia_cmd_plotter` module.
```python
from gaia_cmd_plotter.gaia_cmd_axis import GaiaCMDAxis
```

Next, create a new `GaiaCMDAxis` object and add it to a Matplotlib figure.
```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 8))
ax = GaiaCMDAxis(fig)
```

You can then use the `GaiaCMDAxis` object like any other Matplotlib axis. For example, you can plot data on top of 
the Gaia CMD background, 
```python
bp_rp = 3.5
g_abs = 5.0
ax.plot(bp_rp, g_abs, "ko", ms=10, mec="k")
```
