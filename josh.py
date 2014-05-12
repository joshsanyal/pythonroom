# author: joshsanyal
import turtle

t = turtle.Turtle()

n = int (input("How many legs should this sprite have?"))
print n

t.shape("triangle")
angle = 352 / n
	
for j in range(0,n):
	t.right(angle)
	t.forward(100)
	t.stamp()
	for n in range(18):
		t.right(22)
		t.stamp()
	t.backward(100)
