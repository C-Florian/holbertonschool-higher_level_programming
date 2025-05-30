#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self)
        """define the sound of the Animal"""
        pass

    class Dog(Animal):
        def sound(self):
            return "Bark"

        class Cat(Animal):
            def sound(self):
                return "Meow"

