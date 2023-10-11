#!/usr/bin/env python
# coding: utf-8

# In[2]:


str1 = "Hello"
str2 = "World"
concatenated_string = str1 + " " + str2 
print(concatenated_string)


# In[4]:


repeated_string = "abc" * 3
print(repeated_string)


# In[5]:


my_string = "Hello, World!"
print(my_string[0])      # Output: "H"
print(my_string[7:12])   # Output: "World"


# In[6]:


my_string = "   Hello, World!   "
print(my_string.strip())                # Output: "Hello, World!"
print(my_string.lower())                # Output: "   hello, world!   "
print(my_string.replace("Hello", "Hi")) # Output: "   Hi, World!   "


# In[7]:


name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is Alice and I am 30 years old."


# In[ ]:




