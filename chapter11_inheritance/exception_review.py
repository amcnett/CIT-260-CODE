# Exception Inheritance
# Demonstrates how to create a custom exception

class DivisionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message}"

def divide(a,b):
    if b == 0:
        raise DivisionError("Division by zero not allowed")
    return a/b

print(divide(4,0))