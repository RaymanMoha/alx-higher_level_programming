#!/usr/bin/python3
"""Defines a class Base
This is the "base" class of all other classes in this project.
Implementing this helps manage the id attribute in all future classes to
avoid duplicating code (and bugs).
"""

import json
import turtle

class Base:
    """Module implementation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization

        Args:
            param id = id of the instace
            If id is not None,id is set to the id passed in.
            If id is None, id is set to the no. of objects
            created so far, plus one.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """
        This function converts a list of dictionaries to a JSON string.
        param list_dictionaries: a list of dictionaries
        return: A JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a list of dictionaries to a json file
        param cls: the class to call the method from
        param list_objs: list of instances which inherits of Base
        """
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for lst in list_objs:
                text.append(lst.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        """Transforms a JSON string representation `json_string` to a list
        Takes a json string and returns a python object.
        param json_string: the string to be converted
        return: A list of JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new object from dictionary
        If the dictionary is not empty, create
        a new instance of the class, update
        the attributes of the new instance, and return
        the new instance.

        param cls: the class calling the function
        return: A new instance of the class with the attributes updated"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        elif cls.__name__ == "Square":
            new = cls(10, 10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads from file
        If the file exists, read it and return a list of
        instances created from the file's JSON string.
        Else, return an empty list.

        The first line creates the filename from the class name.
        The try/except block attempts to open the file and read it.
        If the file doesn't exist, the
        except block returns an empty list

        param cls: the class we're calling the method on
        return: A list of instances
        """
        filename = cls.__name__ + ".json"
        object_created = []
        with open(filename, 'r') as f:
            file_string = f.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for el in data:
                object_created.append(cls.create(**el))

        return object_created

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file
        If the list of objects is empty, write an empty string to the file.
        Else, convert the list of objects to a list of dictionaries,
        write the keys of the first dictionary as the header, and
        write the dictionaries as rows.

        param cls: the class we're calling the method on
        param list_objs: list of objects to be saved
        """
        filename = cls.__name__ + ".csv"
        content = ""
        text = []
        if list_objs is not None:
            content += ','.join(list_objs[0].to_dictionary().keys())
            content += '\n'
            for lst in list_objs:
                content += ','.join(
                    map(str, lst.to_dictionary().values())
                )
                content += '\n'

        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv
        It reads a csv file, creates a list of dictionaries,
        then creates a list of objects

        param cls: the class that we're calling the method on
        return: A list of objects
        """
        filename = cls.__name__ + ".csv"
        object_created = []

        with open(filename, 'r') as f:
            header = f.readline().replace('\n', '').split(',')
            for el in f.readlines():
                values = map(int, el.replace('\n', '').split(','))
                data = dict(zip(header, values))
                object_created.append(cls.create(**data))

        return object_created

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Draws the figure(Rectangles and Squares) using the turtle
        module.
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
