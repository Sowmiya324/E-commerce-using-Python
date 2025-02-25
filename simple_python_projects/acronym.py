#convert the given string as acronym format
print("\t\t\tACRONYM")
print("\t\t\t-------")
print("Enter any string as input to view its acronym!!")
str=input("\nEnter a input:")
str1=str.title()
str3=''
for i in str1:
    if i.isupper()==1:
        str3+=i
print("Acronym:",str3)
