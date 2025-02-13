class Fraction:
    def __init__(self, numinator, denuminator):
        self.numinator = numinator
        self.denuminator = denuminator

    def multiply(self, other):
        new_numinator = self.numinator * other.numinator
        new_denuminator = self.denuminator * other.denuminator
        return Fraction(new_numinator, new_denuminator)
    
    def divide(self, other):
        new_numinator = self.numinator * other.denuminator
        new_denuminator = self.denuminator * other.numinator
        return Fraction(new_numinator, new_denuminator)
    
    def add(self, other):
        if self.denuminator == other.denuminator:
            new_numinator = self.numinator + other.numinator
            return Fraction(new_numinator, self.denuminator)
        new_numinator = self.numinator * other.denuminator + other.numinator * self.denuminator
        new_denuminator = self.denuminator * other.denuminator
        return Fraction(new_numinator, new_denuminator)
    
    def subtract(self, other):
        if self.denuminator == other.denuminator:
            new_numinator = self.numinator - other.numinator
            return Fraction(new_numinator, self.denuminator)
        new_numinator = self.numinator * other.denuminator - other.numinator * self.denuminator
        new_denuminator = self.denuminator * other.denuminator
        return Fraction(new_numinator, new_denuminator)
            
    def __str__(self):
        return f"{self.numinator} / {self.denuminator}"
    
dec1 = Fraction(2, 5)
dec2 = Fraction(3, 5)

print(dec1.multiply(dec1))
print(dec1.divide(dec2))
print(dec1.add(dec2))
print(dec1.subtract(dec2))