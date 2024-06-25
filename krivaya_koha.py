import turtle

_radius = 300
n = 2

def f(_radius, n):
    if n == 0:
        turtle.forward(_radius)
    else:
        f(_radius / 3, n - 1)
        turtle.left(60)
        f(_radius / 3, n - 1)
        turtle.right(120)
        f(_radius / 3, n - 1)
        turtle.left(60)
        f(_radius / 3, n - 1)

f(_radius, n)