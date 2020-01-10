# -*- coding: utf-8 -*-
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
length = input("How long you want your password to be? :" )
print(int(length));
 
passlen = int(length)
p =  "".join(random.sample(s,passlen ))
 
print ("Your password is: {}" .format(p))

