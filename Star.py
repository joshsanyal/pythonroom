# author: joshsanyal
import turtle
t1 = turtle.Turtle()
world=turtle.Screen()
world.bgcolor("pink")
t1.color("purple")
t1.hideturtle()
t2 = turtle.Turtle()
t2.color("purple")
t2.hideturtle()
t1.left(30)
t2.left(150)
for i in range(22):
	t1.left(i)
	t1.forward(12)
for j in range(22):
	t2.right(j)
	t2.forward(12)

t3 = turtle.Turtle()
t3.color("blue")
t3.hideturtle()
t3.setpos(-60, -60)
t3.write("Happy Mother's Day, mom!!!")
t3.setpos(-60, -80)
t3.write("Your son, Josh")
