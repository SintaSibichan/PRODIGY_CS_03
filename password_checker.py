import re
password = input("enter your password")
if len(password)<8:
    print("password must be atleast 8 character long")
elif not re.search("[A-Z]",password):
    print("password must contain atleast one uppercase character")
elif not re.search("[a-z]",password):
    print("password must contain atleast one lowercase character")
elif not re.search("[0-9]",password):
    print("password muct contain atleast one digit")
elif not re.search("[@#!$%^&*()_,.{}<>?`]",password):
    print("password must contain atleast one special character")
else:
    print("password is strong")
