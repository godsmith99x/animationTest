import turtle
import time

# Create a Screen object
wn = turtle.Screen()
wn.title("Test Window")
wn.bgcolor('#387c6d')

player = turtle.Turtle()
player.shape("square")
player.color('#e9896a')


def player_animate():
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)


while True:
    player_animate()

wn.mainloop()
