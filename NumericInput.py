#A user interface contains two types of user input controls: TextInput, which accepts all characters and NumericInput, which accepts only digits.

#Implement the class TextInput that contains:
#    Method add(self, character) - adds the given character to the current value
#    Method get_value(self) - returns the current value

#Implement the class NumericInput that:
#    Inherits TextInput
#    Overrides the add method so that each non-numeric character is ignored

#For example, the following code should output "10":

#    input = NumericInput()
#    input.add("1")
#    input.add("a")
#    input.add("0")
#    print(input.get_value())

#class TextInput:
#    pass
  
#class NumericInput:
#    pass

class TextInput():
    str = ""
    
    def add(self, text):
        TextInput.str += text
        
    def get_value(self):
        return TextInput.str
        
class NumericInput(TextInput):
    
    def add(self, text):
        if text.isnumeric():
            NumericInput.str = super(NumericInput, self).add(text)

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())