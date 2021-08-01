import socket
import pyaes
import random
import mysql.connector
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
from time import time



####################################################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host=socket.gethostname()

port=12345

s.bind((host,port))

s.listen(5)

######################################################################################

print('hello')

user=input("Enter the user id : ")

password=input("Enter the password ")

text=input("Enter your message : ")

itext = text

######################################################################################

conn = mysql.connector.connect(user = 'root',
password='hemant',host = '127.0.0.1',database='message')

cursor = conn.cursor()

print("Connection established to the message database: ")

insert_stmt = ("INSERT INTO usermsg(part1, part2, part3, pass)" 
   "VALUES (%s,%s,%s,%s)")

#######################################################################################

start_time = time()
count=0
passw = password
for i in range(0,32-len(password)):
    password=password+"x"
pas=list(password)

l=len(text)
text1=list(text)

text2=[]
for i in range(0,int(l/3)):
    text2.append(text1[i])
textf=''.join(text2) #first part of text == textf

text4=[]
for i in range(int(l/3),int(2*l/3)):
    text4.append(text1[i])
textff=''.join(text4) #second part of text == textff

text6=[]
for i in range(int(2*l/3),int(l)):
    text6.append(text1[i])
textfff=''.join(text6) #third part of text == textfff
print("\n")
print("##################################################\n")
print("We have splitted the message into the following parts ")
print(textf)
print(textff)
print(textfff,"\n")

########################################################################################

k=[]
for i in pas:
   if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
       k.append(int(i))
       count=count+1
   if count==3:
       break
print("The digits in the password are ")
print(k)
x1=k[0]%3
x2=k[1]%3
x3=k[2]%3
print("\n\n")

#########################################################################################

#-----------------for encryption---------------------------------------
print("##################################################\n")
print("Encryption of those parts of message on the basis of key \n")
final_encrypt = []
# algorithm for first part
count1=len(textf)
if x1==0:
 plaintext =textf
 key=password
 key = key.encode('utf-8')
 aes = pyaes.AESModeOfOperationCTR(key)
 ciphertextf = aes.encrypt(plaintext)
 print("Encrypted with AES algorithm")
 final_encrypt.append(ciphertextf)
 print(ciphertextf,"\n")
 
elif x1==1:
 key= bytes(password, 'utf-8')
 cipher = blowfish.Cipher(key)
 if len(textf)%8!=0:
     for i in range(0,8-len(textf)%8):
         textf=textf+"#"
 plaintext =bytes(textf, 'utf-8')
 encrypted_data1 = b"".join(cipher.encrypt_ecb(plaintext))
 print("Encrypted with Blowfish algorithm")
 final_encrypt.append(encrypted_data1)
 print(encrypted_data1,"\n")
 
elif x1==2:
 p1=[]
 if len(textf)%8!=0:
     for i in range(0,8-len(textf)%8):
         textf=textf+"#"
 
 for i in range(0,8):
     p1.append(pas[i])
 pa1=''.join(p1)
 key=pa1
 key = key.encode('utf-8')
 d = des(key)
 ciphertexta1 = d.encrypt(textf)
 final_encrypt.append(ciphertexta1)
 print("Encrypted with DES algorithm")
 print(ciphertexta1,"\n")
 
###################################################################################### 
#for second part
count2=len(textff)
if x2==0:
 plaintext =textff
 key=password
 key = key.encode('utf-8')
 aes = pyaes.AESModeOfOperationCTR(key)
 ciphertextff = aes.encrypt(plaintext)
 final_encrypt.append(ciphertextff)
 print("Encrypted with AES algorithm")
 
 print(ciphertextff,"\n")
 
elif x2==1:
 key= bytes(password, 'utf-8')
 cipher = blowfish.Cipher(key)
 if len(textff)%8!=0:
     for i in range(0,8-len(textff)%8):
         textff=textff+"#"
 plaintext =bytes(textff, 'utf-8')
 encrypted_data2 = b"".join(cipher.encrypt_ecb(plaintext))
 print("Encrypted with Blowfish algorithm")
 final_encrypt.append(encrypted_data2)
 print(encrypted_data2,"\n")
 
elif x2==2:
 p2=[]
 if len(textff)%8!=0:
     for i in range(0,8-len(textff)%8):
         textff=textff+"#"

 for i in range(0,8):
     p2.append(pas[i])
 pa2=''.join(p2)
 key=pa2
 key = key.encode('utf-8')
 d = des(key)
 ciphertexta2 = d.encrypt(textff)
 print("Encrypted with DES algorithm")
 final_encrypt.append(ciphertexta2)
 print(ciphertexta2,"\n")

############################################################################################ 
#for third part
count3=len(textfff)
if x3==0:
 plaintext =textfff
 key=password
 key = key.encode('utf-8')
 aes = pyaes.AESModeOfOperationCTR(key)
 ciphertextfff = aes.encrypt(plaintext)
 final_encrypt.append(ciphertextfff)
 print("Encrypted with AES algorithm")
 print(ciphertextfff,"\n")

elif x3==1:
 key= bytes(password, 'utf-8')
 cipher = blowfish.Cipher(key)
 if len(textfff)%8!=0:
     for i in range(0,8-len(textfff)%8):
         textfff=textfff+"#"
 plaintext =bytes(textfff, 'utf-8')
 encrypted_data3 = b"".join(cipher.encrypt_ecb(plaintext))
 final_encrypt.append(encrypted_data3)
 print("Encrypted with Blowfish algorithm")
 print(encrypted_data3,"\n")
 
elif x3==2:
 p3=[]
 if len(textfff)%8!=0:
     for i in range(0,8-len(textfff)%8):
         textfff=textfff+"#"

 for i in range(0,8):
     p3.append(pas[i])
 pa3=''.join(p3)
 key=pa3
 key = key.encode('utf-8')
 d = des(key)
 ciphertexta3 = d.encrypt(textfff)
 print("Encrypted with DES algorithm")
 final_encrypt.append(ciphertexta3)
 print(ciphertexta3,"\n")
print("\n\n")

enc_time = time()
print("Time taken for encryption " + str(enc_time-start_time)+"\n")

#####################################################################################

data = (final_encrypt[0],final_encrypt[1],final_encrypt[2],passw);
cursor.execute(insert_stmt,data)
conn.commit()
print("Data inserted into message database")
conn.close()

######################################################################################

print("Time taken for database entry " + str(time() - enc_time)+"\n")
while True:
	c,addr=s.accept()

	print("got the connection from",addr)



	c.send(str(len(itext)).encode())

	print(c.recv(1024).decode())

	c.close()

########################################################################################