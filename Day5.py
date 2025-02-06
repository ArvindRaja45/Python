#Password Generator Project
#Easy Version
#Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
#4 letters 2 symbols and 3 numbers then the password might look like this:
#fgdx$*924
#You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

#Hard Version
#When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
#x$d24g*f9
#And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.
#The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, check the hint below for what to Google.
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
