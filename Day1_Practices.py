#Printing
#Question: Use what you learnt to print out the words "Hello world!" with Python code.
print("Hello world!")

#StringManipulation
#Learn to use string concatenation and the new line escape sequence to format strings in Python.
#Question: PAUSE 1. Use \n to add another line of "Hello world".
print("Hello world!\nHello world!\nHello world!")
#Question: PAUSE 2. Add a space between the strings
#So there is a space between the string Hello and Arvind when the print statement runs.
#The output should look like this:
#Hello Arvind
print("Hello" + " " + "Arvind")

#Inputs
#Learn to use the Python input() function to collect user input and use it within your code.
#PAUSE 1. Update the code to add an exclamation mark Using what you have learnt in this lesson and previous, can you figure out how take user input and slot it in between 2 strings?
#You are looking to print a sentence like this:
#Hello Name!
print("Hello " + input("My name is:") + "!")

#Variables
#Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.
#PAUSE 1. Check the length of the user input
#Using what you have learnt about the len() function and the input() function. Try to print out the number of characters in the user input. Write everything in just 1 line of code.
print(len(input("Enter name:")))
#PAUSE 2. Split everything into variables.
#Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation.
username = (input("What is your name?"))
length = (len(username))
print(length)

#Variable Naming
#Learn the rules of variable naming in Python.
#Rules
#Make sure your variable names are descriptive
#Don't have spaces between words
#Don't start with numbers
#Don't use special words like print or input
#Choose simple words that are less likely to become typos
#Check the company style guidelines if you start work at a company
username_of_this_person = "Arvind"
length = len(username_of_this_person)
print(length)
