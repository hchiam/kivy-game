# https://kivy.org/docs/tutorials/firstwidget.html

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from random import random


# create custom widget, but still inherit from Widget
class MyPaintWidget(Widget):

    # on_touch_down() is built-in to detect touch down events!
    def on_touch_down(self, touch):
        myRandomColor = (random(), 1., 1.) # if use HSV, then Sat=1., Val=1.
        # create shape at touch coordinates
        with self.canvas:
            Color(*myRandomColor, mode='hsv') # use HSV color model (Hue,Sat,Val)
            d = 30. # diameter
            Ellipse(pos=(touch.x-d/2,touch.y-d/2), size=(d,d))
            # create a new line for every touch down
            # touch.ud is a python dictionary that can store custom attributes for a touch
            # store initial touch position
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            # also store colour :)
            touch.ud['colour'] = myRandomColor

    # on_touch_move() is built-in to detect touch move events!
    def on_touch_move(self, touch):
        # also create shapes with stored colour
        with self.canvas:
            currentColour = touch.ud['colour']
            Color(*currentColour, mode='hsv')
            d = 30. # diameter
            Ellipse(pos=(touch.x-d/2,touch.y-d/2), size=(d,d))

        # continue the same line while touch move (start new one at touch down)
        # add points to that custom 'line' attribute we made
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    # build an app with widgets packaged into the parent widget to be returned
    def build(self):
        parent = Widget()

        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)

        clearBtn = Button(text='Clear')
        clearBtn.bind(on_release=self.clear_canvas) # bind button release event to function
        parent.add_widget(clearBtn)

        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
