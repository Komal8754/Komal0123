#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#1_ Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. "
name=(input("enter your name "))
age=int(input("enter your age "))
year=2020
age_1=100-age
age_2=year+age_1
print("it will be ",age_2)


# In[ ]:


#2_ Write a Python program which accepts the radius of a circle from the user and compute the area
pi=3.142;
r=float(input("enter radius"))
A=pi*(r*r)
print("area is=",A)


# In[ ]:


#3_ Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
num=int(input("enter any no. and we will tell its even or odd nature"))
if num%2==0:
    print("no. is even in nature")
elif num%2==1:
    print("no. is odd in nature")


# In[ ]:


#4_ Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color='green'
alien_color1=(input("enter the color of alien you want to hit"))


if alien_color==alien_color1:
    print("you earned 5 points")
else:
    print("no points for this selesction")


# In[ ]:


#5_ Choose a color for an alien as you did in Exercise 3, and write an if-else chain.
alien_color='green'
alien_color1=(input("enter the color of alien you want to hit"))


if alien_color==alien_color1:
    print("you earned 5 points")
else:
    print("you saved alien and earned 10")


# In[ ]:


age=int(input("enter your age to identify the stage of life"))
if age <=2:
    print("person is a baby")
elif age<4:
    print("the person is a toddler")
elif age<13:
    print("the person is a kid")
elif age<20:
    print("the person is a teenager")   
elif age<65:
    print("the person is a adult")
elif age>=65:
    print("the person is a elder")
else:
    print("wrong data entry")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




