#!/usr/bin/env python
# coding: utf-8

# ### python programming practice

# ## TASK BLOCK 1: Print Statements (5 Variations)

# In[3]:


# task1: print your name
print('sravya')


# In[4]:


# task2: print with sentence
print('Hello, Iam learning datascience')


# In[46]:


# Print multiple values
print('my name is sravya, my city is hyderabad')


# In[8]:


# Multi-line print
print('my name is sravya')
print('iam from hyderabad')
print('iam learning data science')


# In[17]:


# Print with separator
print('sravya', 27, 'hyderabad', 2020, 'data science', sep='!')


# ### TASK BLOCK 2: Create 5 Variables

# ## Create these variables and printing output:

# In[19]:


your_name = 'sravya' #string
your_height = 5.5    #float
your_age = 27        #integar
is_learning_ds = True;  #boolean
your_city = 'hyderabad'  # string
print(your_name)
print(your_height)
print(your_age)
print(is_learning_ds)
print(your_city)


# ## TASK BLOCK 3: Use f-string Printing

# ### What is f-string?
# 
# - f-string is used to insert variables inside a string easily.

# In[22]:


#creating variables and inserting them inside a string
your_name='sravya'
your_age=27
your_city='hyderabad'
print(f"my name is {your_name},am {your_age}, I stay in {your_city}")


# ## TASK BLOCK 4: Practice Data Types

# In[25]:


#see the type of data types
your_name = "sravya"
your_age = 27
your_height = 5.5
is_learning_ds = True
print(type(your_name))
print(type(your_age))
print(type(your_height))
print(type(is_learning_ds))


# ## TASK BLOCK 5: Type Conversion Practice

# In[30]:


#type conversion from int to float
price = 25.5
print(type(price))
price_change = int(price)
print(price_change)
print(type(price_change))


# In[34]:


#type conversion from string to int
dress = "25"
print(type(dress))
dress_to_int = int(dress)
print(type(dress_to_int))


# In[37]:


#type conversion from integer to float
num_1 = 10
print(type(num_1))
num_2 = float(num_1)
print(type(num_2))
print(num_2)


# ## TASK BLOCK 6: Practice input() Function

# In[45]:


# input is used to give the input and also here am usinf f-string
name = input("Enter your name:")
age = int(input("enter your age:"))
city = input("enter your city:")
print(f"Hai my name is {name} , my age is {age}, am from {city}")


# In[ ]:




