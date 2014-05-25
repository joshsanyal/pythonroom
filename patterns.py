import turtle

t = turtle.Turtle()
colors = ["red", "green", "blue", "pink"]
distances = range(10,100)
for distance in distances:
	t.left(15)
	for c in colors:
		t.color(c)
		t.forward(distance)
		t.left(90)
		
t.speed(0)