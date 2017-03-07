from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Blues7
import numpy as np

N = 200000
x_range = (int(-20e6), int(20e6))
y_range = (int(-20e6), int(20e6))

xs = np.random.uniform(x_range[0], x_range[1], N)
ys = np.random.uniform(y_range[0], y_range[1], N)

output_file("bokeh-example-points-webgl.html")

p = figure(title="simple point example",
           x_range=x_range,
           y_range=y_range,
           plot_height=400,
           plot_width=700,
           webgl=True)

p.circle(xs, ys, size=2, alpha=.5)

show(p)
