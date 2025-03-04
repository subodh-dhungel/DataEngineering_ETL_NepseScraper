# 3. Your code for interacting with the latest web authentication scheme has encountered a
# singularity and your only solution is to go around it in the complex plane. Or maybe
# you just need to perform some calculations using complex numbers. like conjugate, exploring real parts
# and imaginary parts, addition, subtraction, and converting into polar form.

import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def magnitude(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def phase(self):
        """Return angle (θ) in radians."""
        return math.atan2(self.imag, self.real)

    def to_polar(self):
        """Return polar form (r, θ) of the complex number."""
        return (self.magnitude(), self.phase())

    def __str__(self):
        """String representation of complex number."""
        return f"({self.real} + {self.imag}i)"

z1 = ComplexNumber(3, 4)
z2 = ComplexNumber(1, -2)

print(f"Conjugate of {z1}: {z1.conjugate()}")
print(f"Addition: {z1} + {z2} = {z1.add(z2)}")
print(f"Subtraction: {z1} - {z2} = {z1.subtract(z2)}")
print(f"Multiplication: {z1} * {z2} = {z1.multiply(z2)}")
print(f"Division: {z1} / {z2} = {z1.divide(z2)}")
print(f"Polar form of {z1}: {z1.to_polar()}")
