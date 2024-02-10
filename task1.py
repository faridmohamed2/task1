dict={
"name":{"Ahmed","Ali","Amr"},
"password":{1394,6078,9345}       
}
x= str(input("enter your name "))
y= int (input("enter ypur password "))
if x in dict["name"] and y in dict["password"] :
    print("welcome")
else :
    print("incorrect entry") 