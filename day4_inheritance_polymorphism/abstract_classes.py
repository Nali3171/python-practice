from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def areas(self):
        pass

class Circle(Shape):
    