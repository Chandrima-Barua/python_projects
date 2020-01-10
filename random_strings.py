# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:18:38 2019

@author: User
"""

import string
# =============================================================================
# print(string)
# =============================================================================
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
# =============================================================================
# print(random.sample(string.ascii_letters,8))
# =============================================================================
generated_string = random.sample(string.ascii_letters,8)
print("".join(generated_string))
