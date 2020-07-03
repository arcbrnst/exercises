import random


class Pet(object):
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 100)

    def feed(self, points):
        self.hunger = self.hunger - points
        if self.hunger < 0:
            print('Error')

    def __str__(self):
        if self.hunger > 80:
            return '{} голодный'.format(self.name)
        else:
            return '{}'.format(self.name)


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Гав')


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
         print('Мяу')


rygik = Dog('RJ')
pushistik = Cat('PS')

rygik.speak()
pushistik.speak()