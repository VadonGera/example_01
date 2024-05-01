class Animal:
    def __init__(self, name):
        self.name = name

    def speek(self):
        print("Животное говорит")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speek(self):
        super().speek()
        print("Собака лает")


my_dog = Dog("Мася", "Белый кот")

my_dog.speek()
print(my_dog.name)
print(my_dog.breed)
