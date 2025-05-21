# This program asks the user for their name and age, then prints out the responses.
# Step 1: Ask the user for their name 
print ('What is your name?')
# Step 2: Get the user's name
# and store it in a variable
name= input()
# Step 3: Print a message using the variable name
print ('Hi, ' + name + '.')
# Step 4: Ask the user for the age they started programming
print ('At what age did you start programming?')
# Step 5: Get the user's age
age = int(input())
# Step 6: Print a message using the variable age
print ('You started programming at the age of ' + str(age) + '.')
# Step 7: Take the user's age and divide it by 2
print ('Half of that age is ' + str(age/2) + '.')