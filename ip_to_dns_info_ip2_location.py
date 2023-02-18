import mysql.connector 
import requests   
import urllib.parse

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "", database = "ip_address")   
#printing the connection object   
#print(myconn)  
cur = myconn.cursor()  
#print(cur)
try:  
    #Reading the Employee data      
    cur.execute("SELECT fld_ip_address FROM tbl_ip_address")  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
    #printing the result   
    list_1 = []  
    for x in result:  
        list_1.append(list(x)[0])
   # print(list_1)
    for x in result:
        reponse = requests.get("http://ip-api.com/json/"+list(x)[0]).json()
        print(reponse)
except:  
    myconn.rollback()  

  
#myconn.close()    