from turtle import*
import colorsys

speed(0)
bgcolor('black')
hue=0.0

for i in range(160):
    color=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    hue+=0.005
    rt(i)
    circle(125,i)
    fd(i)
    rt(90)
done()
