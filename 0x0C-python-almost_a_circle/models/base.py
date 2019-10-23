#!/usr/bin/python3
""" Module class Base """

import json
import csv


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string save file """
        filename = cls.__name__ + ".json"
        l = []
        if list_objs is not None:
            for i in list_objs:
                l.append(cls.to_dictionary(i))
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ JSON string"""
        if cls.__name__ is "Rectangle":
            r = cls(1, 1)
        elif cls.__name__ is "Square":
            r = cls(1)
            r.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """ load from file"""
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
                for i, e in enumerate(l):
                    l[i] = cls.create(**l[i])
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to file csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as cs:
            cw = csv.writer(cs)
            if cls.__name__ is "Rectangle":
                for i in list_objs:
                    cw.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ is "Square":
                for j in list_objs:
                    cw.writerow([j.id, j.size, j.x, j.y])

    @classmethod
    def load_from_file_csv(cls):
        """ csv """
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as cf:
                cr = csv.reader(cf)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dic = {"id": int(args[0]), "width": int(args[1]),
                               "height": int(args[2]), "x": int(args[3]),
                               "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dic = {"id": int(args[0]), "size": int(args[1]),
                               "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dic)
                    l.append(obj)
        except:
            pass
        return l
