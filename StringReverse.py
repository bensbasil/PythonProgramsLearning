print("Enter a string:")
input_string = input()
reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)
if(input_string == reversed_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
print("Join String ",input_string + " " + reversed_string)