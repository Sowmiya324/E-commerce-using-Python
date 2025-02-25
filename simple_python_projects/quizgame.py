class quiz:
    def q1(self):
        print("-------------------------------------------------------------------------------")
        print("1.Who is the first Prime Minister of India?")
        ua_1=input("Ans:")
        a1="jawaharlal nehru"
        if ua_1.lower()==a1:
            s1=1
        else:
            s1=0
        return s1
    def q2(self):
        print("-------------------------------------------------------------------------------")
        print("2.Which is the capital of India?")
        ua_2=input("Ans:")
        a2="new delhi"
        if ua_2.lower()==a2:
            s2=1
        else:
            s2=0
        return s2
    def q3(self):
        print("-------------------------------------------------------------------------------")
        print("3.Who is the chief Minister of Tamil Nadu?")
        ua_3=input("Ans:")
        a3="stalin"
        if ua_3.lower()==a3:
            s3=1
        else:
            s3=0
        return s3
    def q4(self):
        print("-------------------------------------------------------------------------------")
        print("4.Who is the father of our Nation?")
        ua_4=input("Ans:")
        a4="mahatma gandhi"
        if ua_4.lower()==a4:
            s4=1
        else:
            s4=0
        return s4
    def q5(self):
        print("-------------------------------------------------------------------------------")
        print("5.How many districts are there in Tamil Nadu?")
        ua_5=input("Ans:")
        print("-------------------------------------------------------------------------------")
        a5='38'
        if ua_5==a5:
            s5=1
        else:
            s5=0
        return s5
print("\t\t\t\tQUIZ GAME")
print("\t\t\t\t---------")
name=input("Enter your name:")
age=int(input("Enter your age:"))
m_no=int(input("Enter your mobile number:"))
if age>18:
    print("\nGetting ready to start your quiz!!!!!!!")
    q=quiz()
    us1=q.q1()
    us2=q.q2()
    us3=q.q3()
    us4=q.q4()
    us5=q.q5()
    score=us1+us2+us3+us4+us5
    print("Name  :",name)
    print("Score :",score)
else:
    print("You are not eligible to attend the quiz")

