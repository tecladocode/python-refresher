# Functions vs. Methods

A function that lives inside a class is called a method.

So, methods are functions, but not all functions are methods.

## Function

```python
def average(sequence):
    return sum(sequence) / len(sequence)
```

## Method

```python
class Student:
    def __init__(self):  # method
        self.name = "Rolf"
        self.grades = (79, 90, 95, 99)
    
    def average(self):  # method
        return sum(self.grades) / len(self.grades)
```