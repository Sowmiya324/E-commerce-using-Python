#get mail id from the user as input and divide the username and domain name
def mail():
    user=input("Enter your e-mail id:")
    if '@' in user:
        n=user.find('@')
        user_n=user[:n]
        domain_n=user[n+1:]
        print("User name  :",user_n)
        print("Domain name:",domain_n)
    else:
        print("Invalid mail id")
        mail()
print("\t\t\tEMAIL SLICER")
print("\t\t\t------------")
mail()
