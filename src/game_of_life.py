import random
import copy
from threading import Lock

class SingletonMeta(type):

    _instances = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances = instance
        return cls._instances

class GameOfLife(metaclass=SingletonMeta):

    _instance = None
    flag_first = True
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.flag_first = False
        else:
            cls.flag_first = True
        return cls._instance

    def __init__(self, width=6, height=6, counter=0, system_type="periodic"):

            self.__width = width
            self.__height = height
            self.world = self.generate_universe()
            self.old_world = copy.deepcopy(self.world)
            self.counter = counter
            self.system_type = system_type

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def form_new_generation_box(self):
        self.old_world = copy.deepcopy(self.world)
        universe = self.world
        new_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(universe)):
            for j in range(len(universe[0])):

                if universe[i][j]:
                    if self.__get_near_box(universe, [i, j]) not in (2, 3):
                        new_world[i][j] = 0
                        continue
                    new_world[i][j] = 1
                    continue

                if self.__get_near_box(universe, [i, j]) == 3:
                    new_world[i][j] = 1
                    continue
                new_world[i][j] = 0
        self.world = new_world

    def form_new_generation_periodic(self):
        self.old_world = copy.deepcopy(self.world)
        universe = self.world
        new_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(universe)):
            for j in range(len(universe[0])):

                if universe[i][j]:
                    if self.__get_near_periodic(universe, [i, j]) not in (2, 3):
                        new_world[i][j] = 0
                        continue
                    new_world[i][j] = 1
                    continue

                if self.__get_near_periodic(universe, [i, j]) == 3:
                    new_world[i][j] = 1
                    continue
                new_world[i][j] = 0
        self.world = new_world

    def generate_universe(self):
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    @staticmethod
    def __get_near_periodic(universe, pos, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        count = 0
        for i in system:
            if universe[(pos[0] + i[0]) % len(universe)][(pos[1] + i[1]) % len(universe[0])]:
                count += 1
        return count

    @staticmethod
    def __get_near_box(universe, pos, system=None):
        height = len(universe)
        width = len(universe[0])
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        count = 0
        for i in system:
            if ((pos[0] + i[0])>=0) and ((pos[0] + i[0]) < height):
                if ((pos[1] + i[1]) >= 0) and ((pos[1] + i[1]) < width):
                    if universe[(pos[0] + i[0])][(pos[1] + i[1])]:
                        count += 1
        return count