class Animal:
    def __init__(self, name):
        self.name = name

    def speek(self):
        return "говорит"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speek(self):
        print(f"{self.breed} {self.name} {super().speek()} Мяу")


my_dog = Dog("Мася", "Белый кот")

my_dog.speek()
print(my_dog.name)
print(my_dog.breed)
