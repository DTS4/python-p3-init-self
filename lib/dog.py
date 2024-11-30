#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def talk(self):
        print("Woof!")

    def walk(self):
        print("The dog is walking.")
     