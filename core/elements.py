import turtle

from core.drawer import Drawer


class Elements(Drawer):
    def __init__(self, **kwargs):
        super(Elements, self).__init__(**kwargs)

    def wire(self, length):
        pass