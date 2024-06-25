import turtle

n = list(map(int, input().split()))
_radius = 20
for m in n:
    if m > 200:
        turtle.color("blue")
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(_radius)
        turtle.end_fill()
    else:
        turtle.color("black")
        turtle.circle(m)
turtle.done()