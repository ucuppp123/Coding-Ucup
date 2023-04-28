
#! variabeles in python

first_name = 'Arfan Amir'
last_name = 'Al-kharim'
country = 'Russia'
city = 'Moscow'
age = 23
is_married = False
skills = ['Soldering', 'Python']

person_info = {
    'first_name': first_name,      
    'last_name': last_name,
    'country': country,
    'city': city,
    'age': age,
    'skills': skills,
    'is_married': is_married, 
}   

#! Printing the values stored in the variables

print('first name:',first_name)
print('First name length:',len(first_name))
print('last name:',last_name)
print('Last name length:',len(last_name))
print('country:',country)
print('city:',city)
print('Age:',age)
print('Married:',is_married)
print('Skills:',skills)
print('Person_information:',person_info)

#! Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Arfan amir', 'Al-kharim', 'Russia', 23, False

print(first_name, last_name, country, age, is_married)
print('First name:',first_name)
print('Last name:',last_name)
print('Country:',country)
print('Age:',age)
print('Married:',is_married)

#! Different python data types
#! Let's declare variables with various data types

first_name = 'Arfan Amir'   #? string
last_name = 'Al-kharim'     #? string
country = 'Russia'          #? string
age = 23                    #? integer

#! Printing out types
print(type('Arfan Amir',))  #? string
print(type('Al-Kharim',))   #? string
print(type('Russia',))      #? string
print(type(23,))            #? integer
print(type(3.14,))          #? floating point
print(type(1 + 1j))         #? complex number
print(type(False))          #? boolean
print(type([1, 2, 3, 4]))   #? list 
print(type({first_name :'Arfan Amir', country :'Russia', age : '23'})) #? dictionary
print(type((2,1)))                                                     #? tuples
print(type(zip([1,2],[3,4])))                                          #? sets

#! int to float
num_int = 10
print('num_int',10)             #? 10
num_float = float(10)
print('num_float:', num_float)  #? 10.0

#! float to int
gravity = 9.81
print(int(9.81))                #?  9                                

#! int to string
num_int = 10
print('num_int',10)             #?  10
num_str = str(10)
print('num_str', num_str)       #? '10'

#! str to float
num_str = '10.6'                #? '10.6'
print(float('10.6'))            #?  10.6

#! float to int
num_str = '10'                  #? '10'
print(int('10'))                #?  10

#! str to list
first_name = 'Ucup'             #? 'Ucup'
print(list(first_name))         #? ['u', 'c', 'u', 'p']
