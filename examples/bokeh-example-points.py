from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5, 1]
y = [6, 7, 2, 4, 5, 6]

# output to static HTML file
output_file("bokeh-example-points.html")

# create a new plot with a title and axis labels
p = figure(title="simple point example",
           plot_height=400,
           plot_width=700,
           x_axis_label='x',
           y_axis_label='y')

# add a circle renderer with size 10
p.circle(x, y, size=10)

# show the results
show(p)
