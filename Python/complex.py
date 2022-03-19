from math import sqrt

class Complex:
        
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b
    
    def display(self):
        if self.imaginary < 0:
            print(str(self.real) + " - " + str(abs(self.imaginary)) + "i")
            return
        
        print(str(self.real) + " + " + str(self.imaginary) + "i")
        return
    
    def add(self, a):
        real = self.real + a.real
        imaginary = self.imaginary + a.imaginary
        return Complex(real, imaginary)
        
    def subtract(self, a):
        real = self.real - a.real
        imaginary = self.imaginary - a.imaginary
        return Complex(real, imaginary)
        
    def multiply(self, a):
        real = self.real*a.real - self.imaginary*a.imaginary
        imaginary = self.real*a.imaginary + self.imaginary*a.real
        return Complex(real, imaginary)
    
    def modulus(self):
        return sqrt(self.real*self.real + self.imaginary*self.imaginary)
    
    def conjugate(self):
        return Complex(self.real, -self.imaginary)
    
    def inverse(self):
        real = self.real / (self.modulus()*self.modulus())
        imaginary = -self.imaginary / (self.modulus()*self.modulus())
        return Complex(real, imaginary)