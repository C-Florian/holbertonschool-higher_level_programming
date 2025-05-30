#!/usr/bin/env python3
"""The Enigmatic FlyingFish - Exploring Multiple Inheritance"""

class Fish:
    """class that represent fish"""

    def swim(self):
        """define that fish can swim"""
        print("The fish is swimming")

    def habitat(self):
        """define that fish live in water"""
        print("The fish lives in water")

class Bird:
    """class that represent bird"""

    def fly(self):
        """define that bird can fly"""
        print("The bird is flying")

    def habitat(self):
        """define that bird live in the sky"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """class that represent flyingfish"""

    def swim(self):
        """define that flyingfish can swim"""
        print("The flying fish is swimming!")

    def fly(self):
        """define that flyingfish can fly"""
        print("The flying fish is soaring!")

    def habitat(self):
        """define that flyingfish can live both in water and in the sky"""
        print("The flying fish lives both in water and the sky!")

