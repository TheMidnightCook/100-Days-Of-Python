#Calculator
from art import logo

#Add
def add(n1, n2):
  """This will add given numbers to each other"""
  return n1 + n2

#Substract
def substract(n1, n2):
  """This will substract given numbers from each other"""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """This will multiply given numbers to each other"""
  return n1 * n2

#Divide
def divide(n1, n2):
  """This will divide given numbers by each other"""
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for symbols in operations:
    print(symbols)
  should_continue = True

  while should_continue: 
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") 
    if continue_calc == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()



 
  