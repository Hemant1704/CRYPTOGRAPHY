import random
import string
import socket
import hashlib
import base64
import pyaes
import blowfish
from pyDes import *
import random
import string
import mysql.connector
from time import time

#####################################################################

s=socket.socket()

host=socket.gethostname()

port=12345

s.connect((host,port))



text=(s.recv(1024).decode())

count1 = (int)((int)(text)/3)
count2 = (int)((int)((2*(int)(text))/3) - (int)((int)(text)/3))
count3 = (int)(text) - (count1+count2)


######################################################################

start_time = time()
conn = mysql.connector.connect(user = 'root',password='hemant',host = '127.0.0.1',database='message')
cursor = conn.cursor()

sql = '''SELECT * from usermsg'''

#Executing the query
cursor.execute(sql)

result = cursor.fetchall()[-1];

print("\n")
print("The encrypted part1 from database is ")
print(bytes(result[0]))
print("\n")
print("The encrypted part2 from database is ")
print(bytes(result[1]))
print("\n")
print("The encrypted part3 from database is ")
print(bytes(result[2]))
print("\n")

password = result[3];
encrypted_data1 = bytes(result[0])
encrypted_data2 = bytes(result[1])
encrypted_data3 = bytes(result[2])
conn.close()

db_time = time()
print("Time to load data from database "+str(db_time-start_time)+"\n")
##################################################################################33
count=0
for i in range(0,32-len(password)):
    password=password+"x"
pas=list(password)

k=[]
for i in pas:
   if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
       k.append(int(i))
       count=count+1
   if count==3:
       break

x1=k[0]%3
x2=k[1]%3
x3=k[2]%3



print("##################################################\n")
choice="yes"
final_decrypt = "";
if choice=="yes":

############################################################################################
 if x1==0:
     key=password
     key = key.encode('utf-8')
     aes = pyaes.AESModeOfOperationCTR(key)
     decryptedf = aes.decrypt(encrypted_data1)
     print("Decrypted with AES algorithm")
     final_decrypt = final_decrypt + str(decryptedf.decode('utf-8'))
     #finalMessage += str(decryptedf.decode('utf-8'))
     print(decryptedf.decode('utf-8'),"\n")

     
 elif x1==1:
     key= bytes(password, 'utf-8')
     cipher = blowfish.Cipher(key)
     print("Decrypted with Blowfish algorithm")
     dec1 = (b"".join(cipher.decrypt_ecb(encrypted_data1)))
     final_decrypt = final_decrypt + dec1[0:count1].decode('utf-8')
     #inalMessage+=str(dec1[0:count1].decode('utf-8'))
     print(dec1[0:count1].decode('utf-8'),"\n")

     
 elif x1==2:
     p3= []
     for i in range(0,8):
         p3.append(pas[i])
     pa3=''.join(p3)
     key=pa3
     key = key.encode('utf-8')
     d = des(key)
     decrypted1 = d.decrypt(encrypted_data1)
     print("Decrypted with DES algorithm")
     final_decrypt = final_decrypt + str(decrypted1[0:count1].decode('utf-8'))
     print(decrypted1[0:count1].decode('utf-8'),"\n")

###############################################################################################
 if x2==0:
     key=password
     key = key.encode('utf-8')
     aes = pyaes.AESModeOfOperationCTR(key)
     decryptedff = aes.decrypt(encrypted_data2)
     print("Decrypted with AES algorithm")
     final_decrypt = final_decrypt + str(decryptedff.decode('utf-8'))
     print(decryptedff.decode('utf-8'),"\n")
 elif x2==1:
     key= bytes(password, 'utf-8')
     cipher = blowfish.Cipher(key) 
     print("Decrypted with Blowfish algorithm")
     dec2 = (b"".join(cipher.decrypt_ecb(encrypted_data2)))
     final_decrypt = final_decrypt + str(dec2[0:count2].decode('utf-8'))
     print(dec2[0:count2].decode('utf-8'),"\n")
 elif x2==2:
     p3= []
     for i in range(0,8):
         p3.append(pas[i])
     pa3=''.join(p3)
     key=pa3
     key = key.encode('utf-8')
     d = des(key)
     decrypted2 = d.decrypt(encrypted_data2)
     print("Decrypted with DES algorithm")
     final_decrypt = final_decrypt + str(decrypted2[0:count2].decode('utf-8'))
     print(decrypted2[0:count2].decode('utf-8'),"\n")

##############################################################################################3
 if x3==0:
     key=password
     key = key.encode('utf-8')
     aes = pyaes.AESModeOfOperationCTR(key)
     decryptedfff = aes.decrypt(encrypted_data3)
     print("Decrypted with AES algorithm")
     final_decrypt = final_decrypt + str(decryptedfff.decode('utf-8'))
     print(decryptedfff.decode('utf-8'),"\n")
 elif x3==1:
     key= bytes(password, 'utf-8')
     cipher = blowfish.Cipher(key)
     print("Decrypted with Blowfish algorithm")
     dec3 = (b"".join(cipher.decrypt_ecb(encrypted_data3)))
     final_decrypt = final_decrypt + str(dec3[0:count3].decode('utf-8'))
     print(dec3[0:count3].decode('utf-8'),"\n")
 elif x3==2:
     p3= []
     for i in range(0,8):
         p3.append(pas[i])
     pa3=''.join(p3)
     key=pa3
     key = key.encode('utf-8')
     d = des(key)
     decrypted3 = d.decrypt(encrypted_data3)
     final_decrypt = final_decrypt + str(decrypted3[0:count3].decode('utf-8'))
     print("Decrypted with DES algorithm")
     print(decrypted3[0:count3].decode('utf-8'),"\n")

################################################################################################
print("##################################################\n")

print("The complete decrypted message is : ")     
print(final_decrypt)
print("\n")

print("Time taken for decryption " + str(time() - db_time) + "\n")

print("##################################################\n")
s.send(bytes("Thankyou we securely recieved and encrypted your message",'utf-8'))
s.close()
