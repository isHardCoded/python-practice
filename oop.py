class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
    def set_salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError(f"{new_salary} < 0")
        else:
            self.salary = new_salary
            print(f"Сотруднику {self.name} была назначена новая зарплата в размере: {new_salary} рублей.")

    def birthday(self):
        self.age += 1
        print(f"У сотрудника {self.name} день рождения! Теперь его возраст: {self.age}")

    def give_raise(self, percent):
        if percent < 0:
            raise ValueError(f"{percent} < 0")
        self.salary += self.salary * (percent / 100)
        print(f"Зарплата сотрудника {self.name} была увеличена. Теперь она составляет {self.salary} рублей")

    def promote(self, new_pos):
        return f"Сотрудник {self.name} был повышен до '{new_pos}'"

    def is_retirement_ready(self) -> bool:
        return self.age >= 65

emp1 = Employee("Tom", 37, 35000)
print(emp1.get_details())

emp2 = Employee("Bob", 66, 45000)
print(emp2.get_details())

try:
    emp1.set_salary(40000)

except ValueError as e:
    print(f"Ошибка: {e}")


try:
    emp1.give_raise(100)
except ValueError as e:
    print(f"Ошибка: {e}")

print(emp2.is_retirement_ready())
