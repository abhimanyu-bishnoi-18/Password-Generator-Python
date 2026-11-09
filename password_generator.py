print("password must contain at least one upper alphabetical character.\npassword must contain at least one middle alphabetical character.\npassword must contain at least one lower alphabetical character letter.\npassword must contain at least one digit.\npassword must contain at least one special character like !,@,#,$.%.^,&,*,etc.\npassword must contain at least one capital letter.")

print()
print()

password = input("Enter your password : ")

 
uppercase = "qwertyuiop"
middlecase = "asdfghjkl"
lowercase = "zxcvbnm"
special = "!@#$%^&*()_+"
digit = "1234567890"
capital = "QWERTYUIOPASDFGHJKLZXCVBNM"
found = False


for i in password:
    if i in uppercase:
        uppercase_found = True
        break
else:
    print("password must contain at least one upper alphabetical charcater.")
    uppercase_found = False
for i in password:
    if i in middlecase:
        middlecase_found = True
        break
else:
    print("password must contain at least one middle alphabetical charcater.")
    middlecase_found = False
for i in password:
    if i in lowercase:
        lowercase_found = True
        break
else:
    print("password must contain at least one lower alphabetical charcater.")
    lowercase_found = False
for i in password:
    if i in special:
        special_found = True
        break
else:
    print("password must contain at least one special charcater.")
    special_found = False
for i in password:
    if i in digit:
        digit_found = True
        break
else:
    print("password must contain at least one digit.")
    digit_found = False
for i in password:
    if i in capital:
        capital_found = True
        break
else:
    print("password must contain at least one capital letter.")
    capital_found = False

if len(password)>=8 and uppercase_found and middlecase_found and lowercase_found and special_found and digit_found and capital_found:
    confirm_password = input("re-enter your password : ")
    if password == confirm_password:
        print("password generated successfully.")
    else:
        print("passwords do not match, please try again.")
else:
    print("password do not meet the requirements, please try again.")

