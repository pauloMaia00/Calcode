# Your name: Paulo Maia

# Create function called main()
# This function controls the flow of the program
def main():
  # Calls the function
  # Assign the function to variables InputNum1 and InputNum2
  InputNum1, InputNum2 = userInput()
  # Calls the function, passes the variable IntputNum1 and InputNum2
  # Return a new variable
  answerSum = add(InputNum1, InputNum2)
  # Calls the function, passes the variable IntputNum1 and InputNum2
  # Return a new variable
  answerSub = subtract(InputNum1, InputNum2)
  # Calls the function, passes the variable IntputNum1 and InputNum2
  # Return a new variable
  answerMult = multiply(InputNum1, InputNum2)
  # Calls the function, passes the variable IntputNum1 and InputNum2
  # Return a new variable
  answerDiv = divide(InputNum1, InputNum2)
  # Calls the function, passes the variable IntputNum1 and InputNum2
  # Return a new variable
  answerMon = modulo(InputNum1, InputNum2)
  # Calls the function, passes the variable IntputNum1 and InputNum2
  # Return a new variable
  answerExo = exponent(InputNum1, InputNum2)
  # Calls the function, passes the nine variables to function userOutput()
  userOutput(InputNum1, InputNum2, answerSum, answerSub, answerMult, answerDiv,
             answerMon, answerExo)


#Create function called user-input
# This function will ask the user to enter two numbers.
def userInput():
  # Display on a screen
  # Accept input from input, convert the input to float
  # Assign float to variable Num1
  Num1 = float(input('Enter your first number: '))
  # Display on a screen
  # Accept input from input, convert the input to float
  # Assign float to variable Num2
  Num2 = float(input('Enter your second number: '))
  # return the
  return Num1, Num2


# Create a function called add()
# This function will accept the two numbers and return the sum
def add(n1, n2):
  # Take the two numbers and add them
  # Assign the sum to the variable Sum
  Sum = n1 + n2
  # Convert the integer to a float
  # Assign float to variable An1
  An1 = float(Sum)
  # Return the sum
  return An1


# Create a function called subtract()
# This function will accept the two numbers and return the difference between them
def subtract(n1, n2):
  # Take the two integers and subtract them
  # Assign integer to diff
  diff = n1 - n2
  # Convert integer to float
  # Assign float to variable An2
  An2 = float(diff)
  # Return the difference
  return An2


# Create a function called multiply()
# This function will accept the two numbers and return the product
def multiply(n1, n2):
  # Take the two integers and multiply them
  # Assign integer to Mult
  Mult = n1 * n2
  # Convert integer to float
  # Assign float to variable An3
  An3 = float(Mult)
  # Return the product
  return (An3)
  # Create a function called divide()


# This function will accept the two numbers and return the quotient
def divide(n1, n2):
  # Use try to watch code for errors
  try:
    # Take the two integers and divide them
    # Assign float to variable Div
    Div = n1 / n2
    # Return the quotient
    return Div
    # Expection to run if code blocks throws an error
  except:
    # Error is shown to the user
    return ('cannot divide by zero')


# Create a function called modulo()
# This function will accept the two numbers and return the modulo
def modulo(n1, n2):
  # Use try to watch code for errors
  try:
    # Take the two integers and divide them, use % to calculate the remainder
    Mon = n1 % n2
    # Convert the integer to float
    # Assign the float to variable An5
    An5 = float(Mon)
    # return the modulo
    return An5
    # Expection to run if code blocks throws an error
  except:
    # Error is shown to the user
    return ('cannot divide by zero')


# Create a function called exponent()
# This function will accept the two numbers and return the first number raised to the power of the second number
def exponent(n1, n2):
  # Take the first integer and raise it to the power of the second integer
  # Assign the integer to variable Exo
  Exo = n1**n2
  # Convert integer to float
  # Assign float to variable An6
  An6 = float(Exo)
  # Return the exponent
  return An6


# Create a function called userOutput()
# This function will print all of the calculations
def userOutput(num1, num2, a1, a2, a3, a4, a5, a6):
  # Print the two numbers with the sum
  print(num1, '+', num2, '=', a1)
  # Print the two numbers with the difference
  print(num1, '-', num2, '=', a2)
  # Print the two numbers with the product
  print(num1, '*', num2, '=', a3)
  # Print the two numbers with the quotient
  print(num1, '/', num2, '=', a4)
  # Print the two numbers with the modulo
  print(num1, '%', num2, '=', a5)
  # Print the two numbers with the exponent
  print(num1, '**', num2, '=', a6)



if __name__ == '__main__':
  main()
