# 1

# Function uses for loop to run traversal through the given input; however, it uses a return statement at each iteration, which means that the loop will not return to the starting point.

def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
print("\nany_lowercase1 function output for:")
print("123 - ", any_lowercase1("123")) # output: False
print("a - ", any_lowercase1("a")) # output: True
print("A - ", any_lowercase1("A")) # output: False
print("aA - ", any_lowercase1("aA")) # output: True
print("Aa - ", any_lowercase1("Aa")) # output: False

# 2
# Function uses for loop to run traversal through the given input; however, it has a semantic error, or we can assume that the post-condition is violated. Instead of looking for the 'c' temporary variable in the input, it checks for 'c' which is a string literal. As 'c' is lowercased, the function alway returns true from the first iteration, and the function ends.
def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'
print("\nany_lowercase2 function output for:")
print("123 - ", any_lowercase2("123")) # output: True
print("a - ", any_lowercase2("a")) # output: True
print("A - ", any_lowercase2("A")) # output: True
print("aA - ", any_lowercase2("aA")) # output: True
print("Aa - ", any_lowercase2("Aa")) # output: True


# 3
# Function uses for loop to run traversal through the given input; however, at each iteration it initializes a 'flag' temporary variable and assigns it the result of the 'islower' method. As the temp variable is local per each iteration, the function returns the result of the last iteration only. That's why the output for 'aA' is False, but 'Aa' input results in True.
def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag

print("\nany_lowercase3 function output for:")
print("123 - ", any_lowercase3("123")) # output: False
print("a - ", any_lowercase3("a")) # output: True
print("A - ", any_lowercase3("A")) # output: False
print("aA - ", any_lowercase3("aA")) # output: False
print("Aa - ", any_lowercase3("Aa")) # output: True

# 4
# Function uses for loop to run traversal through the given input; at the entry of the function it declares a 'flag' local variable for the scope of the function. At each iteration, it checks whether the character is lowercased or not, and uses 'or' keyword to compare the previous/initial and current result. The 'or' keyword ensures that if there is a positive value for previous or current checks, the 'flag' local variable will keep it. As a result, if there is any lowercase in the input, the function will return it after the full cycle of iterations through the input.

def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag
print("\nany_lowercase4 function output for:")
print("123 - ", any_lowercase4("123")) # output: False
print("a - ", any_lowercase4("a")) # output: True
print("A - ", any_lowercase4("A")) # output: False
print("aA - ", any_lowercase4("aA")) # output: True
print("Aa - ", any_lowercase4("Aa")) # output: True

# 5
# Function checks whether there is any non-lowercased character in the input, and when it is found, returns false. This function implements the opposite operation related to its naming, hence carries a semantic error, or we may assume that the post-condition is violated.

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True
print("\nany_lowercase5 function output for:")
print("123 - ", any_lowercase5("123")) # output: False
print("a - ", any_lowercase5("a")) # output: True
print("A - ", any_lowercase5("A")) # output: False
print("aA - ", any_lowercase5("aA")) # output: False
print("Aa - ", any_lowercase5("Aa")) # output: False