#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random


# ### Helper functions

# In[2]:


def higher_power(base, exponent):
    """
    computes a^b in O(logn) time.
    Input Parameter(s):
    -----------------------------
    base, exponent- int ; for base^(exponent) e.g. 2^5 =32
    Returns
    -----------------------------
    power_output- int
    """
    power_output = 1 # output initialized at 1
    while (exponent):# Keep iterating till exponent becomes 0 
        if ((exponent & 1) == 1) :# if exponent is odd
            power_output =power_output * base # then multiply "power_output" with base number
        exponent = exponent >> 1 # right shift bitwise operator i.e. equivalent to divide by 2
        base = base * base # base number is multiplied by itself
    return power_output

# Testing the above function 
print('testing higher_power()')
a ,b =2, 5
print(higher_power(a, b))
a ,b =3, 4
print(higher_power(a, b))
# In[3]:


def modulo_higher_power(base, exponent, n):
    """
    computes a^b modulo n in O(logn) time following the property - (m*n) modulo x = ((m modulo x)*(n modulo x))modulo x
    Input Parameter(s):
    -----------------------------
    base, exponent- int ; for base^(exponent) e.g. 2^5 =32
    Returns
    -----------------------------
    power_output- int
    """
    power_output = 1 # output initialized at 1
    while (exponent):# Keep iterating till exponent becomes 0 
        if ((exponent & 1) == 1) :# if exponent is odd
            power_output =(power_output * base)% n # then multiply "power_output" with base number
        exponent = exponent >> 1 # right shift bitwise operator i.e. equivalent to divide by 2
        base = (base * base)%n # base number is multiplied by itself
    return power_output

# Testing the above function 
a ,b =2, 5
print('testing modulo_higher_power()')
print(modulo_higher_power(a, b, 30))
a ,b =3, 4
print(modulo_higher_power(a, b,80))
# In[4]:


def two_factorize(input_num):
    """ factorizes a given number input_num = 2^(power_of_2) *z where z is an odd number and
    Returns power_of_2 ->  the exponent of 2
    Input Parameters
    ----------------
    input_num - int
    Returns 
    -------------------
    power_of_2 -int
    """
    odd_factor =  input_num ;# initialize 
    power_of_2 = 0
    while (odd_factor % 2 == 0):# i.e divisible by 2
        odd_factor = int(np.floor(odd_factor/2))
        power_of_2 = power_of_2+1# if divisible by 2, increase the power_of_2 by 1 
        #print(d, power_of_2)
    # at the end of the loop , odd_factor has the biggest odd (composite or prime) factor of input_num
    return power_of_2

print('testing two_factorize()')
print(two_factorize(32))#testing the function
print(two_factorize(54))
print(two_factorize(80))
print(two_factorize(100))
# ### Miller Rabin test core 2 functions 

# In[5]:


def Miller_Rabin_Test(odd_factor, input_num):
    """
    For a single iteration, checks if divisible by a random value in the range (2, input_num - 4)
    Returns False, if not Prime.
    input Parameters :
    -----------------
    odd_factor : int
    an old number such that input_num-1 = 2^x * odd_factor
    Returns: Boolean
    ------------------------
    True - if prime, False if not Prime
    """
    random_val = 2 + random.randint(1, input_num - 4);#any random number between 2 to input_num-2 
    modulo_power = modulo_higher_power(random_val, odd_factor, input_num);# calculate random_val^(odd_factor)% input_num
    if ( modulo_power == input_num - 1 or modulo_power == 1 ):# we finished checking all values
        return True # it is likely to be prime

    while (odd_factor != input_num - 1):# keep squaring modulo_power & doubling odd_factor till odd_factor is input_num - 1
        modulo_power = (modulo_power * modulo_power) % input_num;
        odd_factor = odd_factor * 2
        
        if (modulo_power == input_num - 1):
            return True

        if (modulo_power == 1): 
            return False
        

    return False # the input number is a composite


# In[6]:


def get_Miller_Rabin_results_all_iterations( input_num , r):
        """
        Repeats the Primality Testing r times by calling Miller_Rabin_Test r times
        Input Parameters:
        --------------------------
        input_num : int
        r : no of rounds/ iterations we will check for primality with different random numbers
        -----------------------------------------
        Returns: Boolean
        True - if prime, False if not Prime
        """
        #BASE CASES 1& 2 --- n =1, 2, 3, or 4
        if (input_num <= 3):# because 2 & 3 are  prime
            return True;
        if (input_num <= 1 or input_num == 4):# because 1 & 4 are not prime
            return False;
        

        odd_factor = input_num - 1;# initialized 
        # next, we factorize odd_factor = 2^(power_of_2) *z where z is an odd number and assign odd_factor =z
        while (odd_factor % 2 == 0):## at the end of the while loop , odd_factor has the biggest odd  factor of input_num
            odd_factor = int(np.floor(odd_factor/2)) # divide by 2, apply floor(), convert to integer data type

        for i in range(r):# check r times; the higher the value of r, better the confidence that input_num is prime
            if (Miller_Rabin_Test(odd_factor, input_num) == False):# each iteration
                return False #not prime if any iteration returns False

        return True


# ### the below cell takes the inputs from the user & calls get_Miller_Rabin_results_all_iterations()

# In[7]:


if  __name__ == "__main__":
    print('Enter the number you want to test for Primality i.e. n and then hit the Enter key')
    input_num=input()
    print('Enter the no. of iterations , r ')
    r = input();# No of repeated check
    if (get_Miller_Rabin_results_all_iterations(int(input_num), int(r))):
      print(input_num ," is a prime number")
    else : 
      print(input_num ," is a composite number")


# In[ ]:




