# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:04:21 2022

@author: sahel
"""

alphabet = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' , 'i', 'j', 'k' ,'l' ,'m' ,'n','o','p','q','r','s','t','u','v' ,'w','x','y','z']



end_code = False

def encript (text , shift):
    c=[]
    
    for letter in text:
        if letter in alphabet:
            for i in range(0 , len(alphabet)):
                if alphabet[i] == letter :
                    new_position = i+shift
                    if new_position >25:
                        new_position = new_position-26
           
            c+= alphabet[new_position]
        else:
            c += letter
          
    print(f"{''.join(c)}")
#encript(text, shift)

def decript (text , shift):
    c=[]
    
    for letter in text:
        if letter in alphabet:
            for i in range(0 , len(alphabet)):
                if alphabet[i] == letter :
                    new_position = i-shift
                    if new_position <0:
                        new_position = new_position+26
    
            c += alphabet[new_position]
        else:
            c += letter
    print(f"{''.join(c)}")
#decript(text, shift)


while end_code == False :
    direction = input("type encode to encode and decode to decode:\n")
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number\n"))
    if direction == "decode" :
       decript(text, shift)
    elif direction =="encode":
       encript(text, shift)
    else :
        print("invalid")
    continuee = input("do u want to continue(Yes or No):")
    if continuee == "No":
      end_code = True
    