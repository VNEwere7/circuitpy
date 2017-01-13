from turtle import Turtle

from core.errors import InvalidAngleError, InvalidShapeError


# class Shape(Drawer):

class Drawer(Turtle):
    def __init__(self, **kwargs):
        super(Drawer, self).__init__()
        self.drawer = Turtle()
        self.drawer.shape(kwargs.get('shape', 'arrow'))

    def line(self, length, direction=None, angle=None):
        """

        :param length:
        :param direction:
        :param angle:
        :return:
        """
        if not direction or direction == "right":
            self.drawer.forward(length)
        elif direction == "left":
            self.drawer.backward(length)
        elif direction == "up" and not angle:
            self.up(90, length=length)

    def up(self, angle, length=None):
        """

        :param angle:
        :param length:
        :return:
        """
        self.drawer.setheading(angle)
        self.forward(length)

    def down(self, angle, length=None):
        """

        :param angle:
        :param length:
        :return:
        """
        if not angle < 0:
            raise InvalidAngleError("The angle for moving the drawer down should be negative")
        self.drawer.setheading(angle)
        self.forward(length)

    def shape(self, name=None):
        """

        :param name:
        :return:
        """
        supported_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        if name not in supported_shapes:
            raise InvalidShapeError("The shape {0} is not part of the supported shapes. \ "
                                    "The supported shapes are {1}"
                                    "As a \n fix, you can consider \
                                    creating the shape by calling the register_shape method.".format(name,

                                                                                                     supported_shapes))

    def register_shape_gif(self, gif):
        """

        :param gif:
        :return:
        """
        pass

    def register_shape_custom(self):
        pass
