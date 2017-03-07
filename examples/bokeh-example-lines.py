from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("bokeh-example-lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example",
           plot_height=400,
           plot_width=700,
           x_axis_label='x',
           y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)
