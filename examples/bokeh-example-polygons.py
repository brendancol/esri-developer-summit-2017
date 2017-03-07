from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 10, 7, 5]

# output to static HTML file
output_file("bokeh-example-polygon.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example",
           plot_height=400,
           plot_width=700,
           x_axis_label='x',
           y_axis_label='y')

# add a line renderer with legend and line thickness
p.patch(x, y, legend="Land Area",
        line_width=3, fill_color="#336699", fill_alpha=.6)

# show the results
show(p)
