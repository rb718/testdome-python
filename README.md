# testdome-python

## find_roots

Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.

The roots of the quadratic equation can be found with the following formula: A quadratic equation.

For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.

## NumericInput
A user interface contains two types of user input controls: TextInput, which accepts all characters and NumericInput, which accepts only digits.

Implement the class TextInput that contains:
    Method add(self, character) - adds the given character to the current value
    Method get_value(self) - returns the current value

Implement the class NumericInput that:
    Inherits TextInput
    Overrides the add method so that each non-numeric character is ignored

For example, the following code should output "10":

    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())

class TextInput:
    pass
  
class NumericInput:
    pass