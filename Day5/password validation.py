password="123456"
for i in range(3):
    user_input=input("Enter the password: ")
    if(user_input==password):
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")
        print("you have ",2-i,"attempts left")
