#!/usr/bin/env python3
"""The Mystical Dragon - Mastering Mixins"""

class SwimMixin:
    """class that add swim method"""

    def swim(self):
        """define that the creature can swim"""
        print("The creature swims!")

class FlyMixin:
    """ class that add fly method"""

    def fly(self):
        """define that the creature can fly"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """class that represent dragon"""

    def roar(self):
        """define that dragon can roars"""
        print("The dragon roars!")

