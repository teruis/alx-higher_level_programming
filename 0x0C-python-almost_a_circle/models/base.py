#!/usr/bin/python3
"""
define class named base
"""
import json
import csv
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        nameoffile = cls.__name__ + ".json"
        with open(nameoffile, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                x = []
                for i in list_objs:
                    x.append(i.to_dictionary())
                f.write(Base.to_json_string(x))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                s = cls(1, 1)
            else:
                s = cls(1)
            s.update(**dictionary)
            return s

    @classmethod
    def load_from_file(cls):
        nameoffile = str(cls.__name__) + ".json"
        try:
            with open(nameoffile, "r") as f:
                z = Base.from_json_string(f.read())
                return [cls.create(**d) for d in z]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        nameoffile = cls.__name__ + ".csv"
        with open(nameoffile, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    ele = ["id", "width", "height", "x", "y"]
                else:
                    ele = ["id", "size", "x", "y"]
                s = csv.DictWriter(f, fieldnames=ele)
                for i in list_objs:
                    s.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        nameoffile = cls.__name__ + ".csv"
        try:
            with open(nameoffile, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    ele = ["id", "width", "height", "x", "y"]
                else:
                    ele = ["id", "size", "x", "y"]
                d = csv.DictReader(f, fieldnames=ele)
                q = []
                for i in d:
                    for key, value in i.items():
                        i[key] = int(value)
                    q.append(cls.create(**i))
                return q
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        s = turtle.Turtle()
        s.hideturtle()
        s.screen.bgcolor("red")
        for i in list_rectangles:
            s.color("white")
            s.up()
            s.goto(i.x, i.y)
            s.down()
            s.forward(i.width)
            s.left(90)
            s.forward(i.height)
            s.left(90)
            s.forward(i.width)
            s.left(90)
            s.forward(i.height)
            s.left(90)
        for j in list_squares:
            s.color("black")
            s.up()
            s.goto(j.x, j.y)
            s.down()
            s.forward(j.width)
            s.left(90)
            s.forward(j.height)
            s.left(90)
            s.forward(j.width)
            s.left(90)
            s.forward(j.height)
            s.left(90)
        turtle.exitonclick()
