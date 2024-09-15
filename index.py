class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person = Person("Purity", 24, "Female")

# Call the introduce method to display the person's information
person.introduce()
