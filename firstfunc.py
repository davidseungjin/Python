def print_pizza_area():
	pi_val = 3.14159265

	pizza_diameter = 12.0
	pizza_radius = pizza_diameter / 2.0
	pizza_area = pi_val * pizza_radius * pizza_radius
	print('%.1f inch pizza is %.3f inches squared' % (pizza_diameter, pizza_area))

print_pizza_area()
