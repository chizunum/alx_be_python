# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Adds two numbers without needing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Multiplies two numbers and references class-level data."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
