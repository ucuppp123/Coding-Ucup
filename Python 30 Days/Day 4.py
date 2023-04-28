
#*------------------------------Creating String------------------------------#*

letter = 'P'       #? A String could be a single character or a bunch of texts
print(letter)      #? P
print(len(letter)) #? 1

letter = 'Ucup' 
print(letter)
print(len(letter))

sentence = "u deserve batter than me"
print(sentence)

multiline_string = '''I.
LOVE.
YOU.'''
print(multiline_string)

#! Another way of doing same thing
multiline_string = """I.
LOVE.
YOU."""
print(multiline_string)

#*------------------------------String Concatenation------------------------------#*

first_name = 'Mohamad'
last_name = 'Yusuf'
space = ' '
full_name = first_name + space + last_name
print(full_name)

#! Checking the length of a string using len() built-in function
print(len(first_name))                  #? 7
print(len(last_name))                   #? 5
print(len(first_name) > len(last_name)) #? True
print(len(full_name))                   #? 13

#*------------------------------Escape Sequence in String------------------------------#*

#TODO               \n: new line
#TODO               \t: Tab means(8 spaces)
#TODO               \\: Back slash
#TODO               \': Single quote (')
#TODO               \": Double quote (")

print('Daily Activity Ucup')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') #? To write a backslash
print('In every programming language it starts with \"Hello, World!\"') #? to write a double quote inside a single quote

#*------------------------------String formatting-------------------------------#*

#! Old Style String Formatting (% Operator)
#TODO               %s - String (or any object with a string representation, like numbers)
#TODO               %d - Integers
#TODO               %f - Floating point numbers
#TODO              "%.number of digitsf" - Floating point numbers with fixed precision

#! Strings Only
first_name = 'Mohamad'
last_name = 'Yusuf'
languange = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, languange)
print(formated_string)

#! Strings and Numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)

#*------------------------------New Style String Formatting (str.format)-------------------------------#*

first_name = 'Mohamad'
last_name = 'Yusuf'
languange = 'Python'
formated_string = 'I am {} {}. I teach  {}'.format(first_name, last_name, languange)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a,b, a + b ))
print('{} - {} = {}'.format(a, b, a - b ))
print('{} * {} = {}'.format(a, b, a * b ))
print('{} / {} = {:.2f}'.format(a, b, a / b ))

