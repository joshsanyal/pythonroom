# author: joshsanyal
import turtle

t = turtle.Turtle()

n = int (input("How many legs should this sprite have?"))
print n

t.shape("circle")
angle = 360 / n
	
for j in range(0,n):
	t.right(angle)
	t.forward(100)
	t.stamp()
	t.backward(100)
