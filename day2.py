#this looks like variable but its an object
name_of_var = 13
print(name_of_var,id(name_of_var))
name_of_var = 69
print(name_of_var,id(name_of_var))




x = 7
print(x,id(x))
y =x
print(y+1,id(y))





#object referance
new_name = "ram"
print(new_name,id(new_name))
old_name = new_name
print(new_name,id(new_name), old_name, id(old_name))




#if statement
age = 18

if age >= 18:
    print("u can vote")




#authenticate useer
saved_name=input("enter a username:")
saved_pass=input("enter a password:")
saved_mobile=input("enter your mobile number:")
print("account created")
while True:
    user_name=input("enter your username:")
    user_pass=input("enter your password:")
    if user_name==saved_name and user_pass==saved_pass:
        print("logged in successfully")
        otp="1234"
        print("your otp is:",otp)
        attempts=0
        while attempts<3:
            entered_otp=input("enter otp:")
            if entered_otp==otp:
                print("login verified successfully")
                break
            else:
                attempts+=1
                print("wrong otp, attempts left:",3-attempts)
        if attempts==3:
            print("account blocked")
        break
    else:
        print("invalid username or password")



# int to str
a = 123
b = str(a)

# str to int
x = "456"
y = int(x)



#q1
while True:
    user_input = input("You: ")
    if user_input.lower() == "stop":
        print("Bot: by")
        break
    else:
        print("Bot: ur soo intresting tell me something more about u...")


# q2

while True:
    response = input("submitted your assignment? ").strip().lower()
    if response == "done":
        print("nice")
        break
    else:
        print("doo it fast stupid ")
