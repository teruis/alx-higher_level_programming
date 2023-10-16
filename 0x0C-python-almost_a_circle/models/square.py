#!/usr/bin/python3
"""
define class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        define
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str function
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """
        size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update arg
        """
        if args and len(args) != 0:
            x = 1
            for a in args:
                if x == 1:
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif x == 2:
                    self.size = a
                elif x == 3:
                    self.x = a
                elif x == 4:
                    self.y = a
                x += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        to_dictionary
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
