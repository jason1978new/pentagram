"""
editor: jason
time:22/09/2018
function: patagram chart
"""

import turtle as tt

def drawpentagram(T,size):
    '''
    绘制五角星
    :return:
    '''
    count = 0
    while count < 5:
        T.forward(size)
        T.right(144)
        count += 1


def main():
    T=tt.Turtle()
    T.penup()
    T.backward(10)
    T.pendown()
    T.pensize(1)
    T.pencolor('red')

    size = 50
    while size < 100:
        drawpentagram(T,size)
        size += 10

    T.exitonclick()


if __name__ == "__main__":
    main()
