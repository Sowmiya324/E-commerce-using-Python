#e-commerce management
print("SUPER MART")
print()
print("-----------------------------------------------------------------------WELCOME TO OUR SUPER MART-----------------------------------------------------------------------")
print("Product List:")
print()
#product list
product={"1":"Mobiles","2":"TV","3":"Laptop","4":"Watch"}
#mobile list
product_m={"1":"VIVO","2":"OPPO","3":"SAMSUNG","4":"REDMI"}
vivo={"v_name":"VIVO",
         "v_model":"Y56",
         "v_id":"0001",
         "v_price":17000,
         "v_disc":5
          }
oppo={"o_name":"OPPO",
         "o_model":"R13",
         "o_id":"0002",
         "o_price":19000,
         "o_disc":4
          }
sam={"s_name":"SAMSUNG",
         "s_model":"A20S",
         "s_id":"0003",
         "s_price":15000,
         "s_disc":3
         }
red={"r_name":"REDMI",
         "r_model":"F11",
         "r_id":"0004",
         "r_price":13000,
         "r_disc":6
         }
#tv list
product_t={"1":"SAMSUNG","2":"LG","3":"SONY","4":"TCL"}
sam1={"s1_name":"SAMSUNG",
         "s1_model":"S34",
         "s1_id":"0011",
         "s1_price":30000,
         "s1_disc":2
         }
lg={"l_name":"LG",
         "l_model":"L34",
         "l_id":"0012",
         "l_price":35000,
         "l_disc":1
        }
sony={"so_name":"SONY",
         "so_model":"PS4",
         "so_id":"0013",
         "so_price":33000,
         "so_disc":4
        }
tcl={"t_name":"TCL",
         "t_model":"P306",
         "t_id":"0014",
         "t_price":38000,
         "t_disc":2
        }
#laptop list
product_l={"1":"ACER","2":"DELL","3":"HCL","4":"MSI"}
acer={"a_name":"ACER",
               "a_model":"SFG14",
               "a_id":"0201",
               "a_price":28000,
              "a_disc":1
         }
dell={"d_name":"DELL",
               "d_model":"XPS16",
               "d_id":"0202",
               "d_price":32000,
              "d_disc":4
         }
hcl={"h_name":"HCL",
               "h_model":"AE3V",
               "h_id":"0203",
               "h_price":26000,
              "h_disc":2
         }
msi={"m_name":"MSI",
               "m_model":"P16",
               "m_id":"0204",
               "m_price":30000,
              "m_disc":1
         }
#watch list
product_w={"1":"CITIZEN","2":"TITAN","3":"WELLINGTON","4":"FOSSIL"}
cit={"c_name":"CITIZEN",
               "c_model":"X16",
               "c_id":"3001",
               "c_price":3000,
              "c_disc":2
         }
tit={"ti_name":"TITAN",
               "ti_model":"S16",
               "ti_id":"3002",
               "ti_price":3500,
              "ti_disc":1
         }
we={"w_name":"WLLINGTON",
               "w_model":"S316",
               "w_id":"3003",
               "w_price":3800,
              "w_disc":3
         }
fos={"f_name":"FOSSIL",
               "f_model":"F36",
               "f_id":"3004",
               "f_price":3200,
              "f_disc":4
         }
for x,y in product.items():
    print("(",x,")",y,end="\t\t\t\t")
print()
value_1=input("Pick any one:")
#if the user give the input as mobiles or 1
if(value_1.lower()=="mobiles" or value_1=="1"):
     print()
     print("-------------------------------------------------------------------------------Mobiles---------------------------------------------------------------------------------")
     for x1,y1 in product_m.items():
        print("(",x1,")",y1,end="\t\t\t\t")
     print()
     value_m=input("Pick any one:")
     if(value_m.lower()=="vivo" or value_m=="1"):
         print()
         print("----------VIVO-----------")
         v_dprice=(vivo["v_disc"]/100)*vivo["v_price"]
         v_fprice=vivo["v_price"]-v_dprice
         print("Brand Name :",vivo["v_name"])
         print("Model Name :",vivo["v_model"])
         print("Product id :",vivo["v_id"])
         print("Price      :",vivo["v_price"])
         print("Discount   :",vivo["v_disc"],"%")
         print("-------------------------")
         print("Fixed Price:",v_fprice)
         print("-------------------------")
         print("Buy now                                                                                                                                                       Close")
         value_b=input("Pick any one:")
         if value_b.lower()=="buy now":
             print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
             name=input("Full Name:")
             no=input("Mobile Number:")
             addr=input("Address:")
             print("Product ID:",vivo["v_id"])
             quantity=int(input("Quantity:"))
             t_price=quantity*v_fprice
             p_details=vivo["v_name"]+" "+vivo["v_model"]
             print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
             print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
             print()
             print(name,no,addr,vivo["v_id"],p_details,quantity,t_price,sep="\t\t\t")
             print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         elif value_b.lower()=="close":
             print("Thank you for visiting")
         else:
             print("Invalid operations!!!")
     elif(value_m.lower()=="oppo" or value_m=="2"): 
        print()
        print("----------OPPO-----------")
        o_dprice=(oppo["o_disc"]/100)*oppo["o_price"]
        o_fprice=oppo["o_price"]-o_dprice
        print("Brand Name :",oppo["o_name"])
        print("Model Name :",oppo["o_model"])
        print("Product id :",oppo["o_id"])
        print("Price      :",oppo["o_price"])
        print("Discount   :",oppo["o_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",o_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",oppo["o_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*o_fprice
            p_details=oppo["o_name"]+" "+oppo["o_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,oppo["o_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
     elif(value_m.lower()=="samsung" or value_m=="3"):
         print()
         print("---------SAMSUNG---------")
         s_dprice=(sam["s_disc"]/100)*sam["s_price"]
         s_fprice=sam["s_price"]-s_dprice
         print("Brand Name :",sam["s_name"])
         print("Model Name :",sam["s_model"])
         print("Product id :",sam["s_id"])
         print("Price      :",sam["s_price"])
         print("Discount   :",sam["s_disc"],"%")
         print("-------------------------")
         print("Fixed Price:",s_fprice)
         print("-------------------------")
         print("Buy now                                                                                                                                                       Close")
         value_b=input("Pick any one:")
         if value_b.lower()=="buy now":
             print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
             name=input("Full Name:")
             no=input("Mobile Number:")
             addr=input("Address:")
             print("Product ID:",sam["s_id"])
             quantity=int(input("Quantity:"))
             t_price=quantity*s_fprice
             p_details=sam["s_name"]+" "+sam["s_model"]
             print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
             print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
             print()
             print(name,no,addr,sam["s_id"],p_details,quantity,t_price,sep="\t\t\t")
             print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         elif value_b.lower()=="close":
             print("Thank you for visiting")
         else:
             print("Invalid operations!!!")
     elif(value_m.lower()=="redmi" or value_m=="4"):
         print()
         print("----------REDMI----------")
         r_dprice=(red["r_disc"]/100)*red["r_price"]
         r_fprice=red["r_price"]-r_dprice
         print("Brand Name :",red["r_name"])
         print("Model Name :",red["r_model"])
         print("Product id :",red["r_id"])
         print("Price      :",red["r_price"])
         print("Discount   :",red["r_disc"],"%")
         print("-------------------------")
         print("Fixed Price:",r_fprice)
         print("-------------------------")
         print("Buy now                                                                                                                                                       Close")
         value_b=input("Pick any one:")
         if value_b.lower()=="buy now":
             
             print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
             name=input("Full Name:")
             no=input("Mobile Number:")
             addr=input("Address:")
             print("Product ID:",red["r_id"])
             quantity=int(input("Quantity:"))
             t_price=quantity*r_fprice
             p_details=red["r_name"]+" "+red["r_model"]
             print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
             print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
             print()
             print(name,no,addr,red["r_id"],p_details,quantity,t_price,sep="\t\t\t")
             print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         elif value_b.lower()=="close":
             print("Thank you for visiting")
         else:
             print("Invalid operations!!!")
     else:
        print("Please enter valid mobile name or number!!!!")
#if the user give the input as tv or 2
elif(value_1.lower()=="tv" or value_1=="2"):
    print()
    print("----------------------------------------------------------------------------------TV-----------------------------------------------------------------------------------")
    for x2,y2 in product_t.items():
        print("(",x2,")",y2,end="\t\t\t\t")
    print()
    value_t=input("Pick any one:")
    if(value_t.lower()=="samsung" or value_t=="1"):
         print()
         print("--------SAMSUNG---------")
         s1_dprice=(sam1["s1_disc"]/100)*sam1["s1_price"]
         s1_fprice=sam1["s1_price"]-s1_dprice
         print("Brand Name :",sam1["s1_name"])
         print("Model Name :",sam1["s1_model"])
         print("Product id :",sam1["s1_id"])
         print("Price      :",sam1["s1_price"])
         print("Discount   :",sam1["s1_disc"],"%")
         print("-------------------------")
         print("Fixed Price:",s1_fprice)
         print("-------------------------")
         print("Buy now                                                                                                                                                       Close")
         value_b=input("Pick any one:")
         if value_b.lower()=="buy now":
             print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
             name=input("Full Name:")
             no=input("Mobile Number:")
             addr=input("Address:")
             print("Product ID:",sam1["s1_id"])
             quantity=int(input("Quantity:"))
             t_price=quantity*s1_fprice
             p_details=sam1["s1_name"]+" "+sam1["s1_model"]
             print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
             print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
             print()
             print(name,no,addr,sam1["s1_id"],p_details,quantity,t_price,sep="\t\t\t")
             print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         elif value_b.lower()=="close":
             print("Thank you for visiting")
         else:
             print("Invalid operations!!!")
    elif(value_t.lower()=="lg" or value_t=="2"):
        print()
        print("-----------LG------------")
        l_dprice=(lg["l_disc"]/100)*lg["l_price"]
        l_fprice=lg["l_price"]-l_dprice
        print("Brand Name :",lg["l_name"])
        print("Model Name :",lg["l_model"])
        print("Product id :",lg["l_id"])
        print("Price      :",lg["l_price"])
        print("Discount   :",lg["l_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",l_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",lg["l_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*l_fprice
            p_details=lg["l_name"]+" "+lg["l_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,lg["l_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_t.lower()=="sony" or value_t=="3"):
        print()
        print("----------SONY-----------")
        so_dprice=(sony["so_disc"]/100)*sony["so_price"]
        so_fprice=sony["so_price"]-so_dprice
        print("Brand Name :",sony["so_name"])
        print("Model Name :",sony["so_model"])
        print("Product id :",sony["so_id"])
        print("Price      :",sony["so_price"])
        print("Discount   :",sony["so_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",so_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",sony["so_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*so_fprice
            p_details=sony["so_name"]+" "+sony["so_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,sony["so_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_t.lower()=="tcl" or value_t=="4"):
        print()
        print("----------TCL-----------")
        t_dprice=(tcl["t_disc"]/100)*tcl["t_price"]
        t_fprice=tcl["t_price"]-t_dprice
        print("Brand Name :",tcl["t_name"])
        print("Model Name :",tcl["t_model"])
        print("Product id :",tcl["t_id"])
        print("Price      :",tcl["t_price"])
        print("Discount   :",tcl["t_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",t_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",tcl["t_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*t_fprice
            p_details=tcl["t_name"]+" "+tcl["t_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,tcl["t_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    else:
        print("Please enter valid TV name or number!!!")
#if the user give the input as laptop or 3
elif(value_1.lower()=="laptop" or value_1=="3"):
    print()
    print("-------------------------------------------------------------------------------Laptop---------------------------------------------------------------------------------")
    for x3,y3 in product_l.items():
        print("(",x3,")",y3,end="\t\t\t\t")
    print()
    value_l=input("Pick any one:")
    if(value_l.lower()=="acer" or value_l=="1"):
        print()
        print("-----------ACER----------")
        a_dprice=(acer["a_disc"]/100)*acer["a_price"]
        a_fprice=acer["a_price"]-a_dprice
        print("Brand Name :",acer["a_name"])
        print("Model Name :",acer["a_model"])
        print("Product id :",acer["a_id"])
        print("Price      :",acer["a_price"])
        print("Discount   :",acer["a_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",a_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",acer["a_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*a_fprice
            p_details=acer["a_name"]+" "+acer["a_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,acer["a_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_l.lower()=="dell" or value_l=="2"):
        print()
        print("----------DELL-----------")
        d_dprice=(dell["d_disc"]/100)*dell["d_price"]
        d_fprice=dell["d_price"]-d_dprice
        print("Brand Name :",dell["d_name"])
        print("Model Name :",dell["d_model"])
        print("Product id :",dell["d_id"])
        print("Price      :",dell["d_price"])
        print("Discount   :",dell["d_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",d_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",dell["d_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*d_fprice
            p_details=dell["d_name"]+" "+dell["d_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,dell["d_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_l.lower()=="hcl" or value_l=="3"):
        print()
        print("-----------HCL-----------")
        h_dprice=(hcl["h_disc"]/100)*hcl["h_price"]
        h_fprice=hcl["h_price"]-h_dprice
        print("Brand Name :",hcl["h_name"])
        print("Model Name :",hcl["h_model"])
        print("Product id :",hcl["h_id"])
        print("Price      :",hcl["h_price"])
        print("Discount   :",hcl["h_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",h_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",hcl["h_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*h_fprice
            p_details=hcl["h_name"]+" "+hcl["h_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,hcl["h_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_l.lower()=="msi" or value_l=="4"):
        print()
        print("-----------MSI-----------")
        m_dprice=(msi["m_disc"]/100)*msi["m_price"]
        m_fprice=msi["m_price"]-m_dprice
        print("Brand Name :",msi["m_name"])
        print("Model Name :",msi["m_model"])
        print("Product id :",msi["m_id"])
        print("Price      :",msi["m_price"])
        print("Discount   :",msi["m_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",m_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",msi["m_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*m_fprice
            p_details=msi["m_name"]+" "+msi["m_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,msi["m_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    else:
        print("Please enter valid laptop name or number!!!")
#if the user give the input as watch or 4
elif(value_1.lower()=="watch" or value_1=="4"):
    print()
    print("------------------------------------------------------------------------------Watch---------------------------------------------------------------------------------")
    for x4,y4 in product_w.items():
        print("(",x4,")",y4,end="\t\t\t\t")
    print()
    value_w=input("Pick any one:")
    if(value_w.lower()=="citizen" or value_w=="1"):
        print()
        print("---------CITIZEN---------")
        c_dprice=(cit["c_disc"]/100)*cit["c_price"]
        c_fprice=cit["c_price"]-c_dprice
        print("Brand Name :",cit["c_name"])
        print("Model Name :",cit["c_model"])
        print("Product id :",cit["c_id"])
        print("Price      :",cit["c_price"])
        print("Discount   :",cit["c_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",c_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",cit["c_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*c_fprice
            p_details=cit["c_name"]+" "+cit["c_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,cit["c_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_w.lower()=="titan" or value_w=="2"):
        print()
        print("----------TITAN----------")
        ti_dprice=(tit["ti_disc"]/100)*tit["ti_price"]
        ti_fprice=tit["ti_price"]-ti_dprice
        print("Brand Name :",tit["ti_name"])
        print("Model Name :",tit["ti_model"])
        print("Product id :",tit["ti_id"])
        print("Price      :",tit["ti_price"])
        print("Discount   :",tit["ti_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",ti_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",tit["ti_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*ti_fprice
            p_details=tit["ti_name"]+" "+tit["ti_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,tit["ti_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_w.lower()=="wellington" or value_w=="3"):
        print()
        print("--------WELLINGTON--------")
        w_dprice=(we["w_disc"]/100)*we["w_price"]
        w_fprice=we["w_price"]-w_dprice
        print("Brand Name :",we["w_name"])
        print("Model Name :",we["w_model"])
        print("Product id :",we["w_id"])
        print("Price      :",we["w_price"])
        print("Discount   :",we["w_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",w_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",we["w_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*w_fprice
            p_details=we["w_name"]+" "+we["w_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,we["w_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    elif(value_w.lower()=="fossil" or value_w=="4"):
        print()
        print("----------FOSSIL----------")
        f_dprice=(fos["f_disc"]/100)*fos["f_price"]
        f_fprice=fos["f_price"]-f_dprice
        print("Brand Name :",fos["f_name"])
        print("Model Name :",fos["f_model"])
        print("Product id :",fos["f_id"])
        print("Price      :",fos["f_price"])
        print("Discount   :",fos["f_disc"],"%")
        print("-------------------------")
        print("Fixed Price:",f_fprice)
        print("-------------------------")
        print("Buy now                                                                                                                                                       Close")
        value_b=input("Pick any one:")
        if value_b.lower()=="buy now":
            print("--------------------------------------------------------------------------------BUY NOW--------------------------------------------------------------------------------")
            name=input("Full Name:")
            no=input("Mobile Number:")
            addr=input("Address:")
            print("Product ID:",fos["f_id"])
            quantity=int(input("Quantity:"))
            t_price=quantity*f_fprice
            p_details=fos["f_name"]+" "+fos["f_model"]
            print("----------------------------------------------------------------------------------BILL---------------------------------------------------------------------------------")
            print("Full Name","Mobile Number","\tAddress","     Product ID","    Product Details","    Quantity","    Total Price",sep="\t\t")
            print()
            print(name,no,addr,fos["f_id"],p_details,quantity,t_price,sep="\t\t\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif value_b.lower()=="close":
            print("Thank you for visiting")
        else:
            print("Invalid operations!!!")
    else:
        print(" Please enter valid watch name or number!!!")
else:
    print("Please enter valid product name or number!!!")
