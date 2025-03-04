class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def showInfo(self):
        return f"Car: {self.brand}{self.model}"
    
car1 = Car("Polo", "GT")
car2 = Car("Tesla", "X")

print(car1.name,car1.model)
print(car2.name,car2.model)