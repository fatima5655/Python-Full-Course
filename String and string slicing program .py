#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define a string
my_string = "Hello, World!"

# Extract a substring from index 0 to 4 (exclusive)
substring1 = my_string[0:5]  # Output: "Hello"

# Omitting start index (implicitly starts from 0)
substring2 = my_string[:5]   # Output: "Hello"

# Extract a substring from index 7 to the end of the string
substring3 = my_string[7:]   # Output: "World!"

# Use negative indices to slice from the end of the string
substring4 = my_string[-6:-1]  # Output: "World"

# Slice with a step value (every second character)
substring5 = my_string[::2]  # Output: "Hlo ol!"

# Reverse the string using slicing
reversed_string = my_string[::-1]  # Output: "!dlroW ,olleH"

print(substring1)
print(substring2)
print(substring3)
print(substring4)
print(substring5)
print(reversed_string)


# In[ ]:


# Get user input for a string
user_input = input("Enter a sentence: ")

# Print the original string
print("Original String:", user_input)

# Print the length of the string
print("Length of the String:", len(user_input))

# Extract the first word using string slicing
first_word = user_input.split()[0]
print("First Word:", first_word)

# Extract the last word using string slicing
last_word = user_input.split()[-1]
print("Last Word:", last_word)

# Extract the middle portion of the string using string slicing
middle_index = len(user_input) // 2
middle_word = user_input[middle_index - 1:middle_index + 2]
print("Middle Portion of the String:", middle_word)

# Reverse the string using string slicing
reversed_string = user_input[::-1]
print("Reversed String:", reversed_string)

# Extract and print each word of the string using a loop and string slicing
words = user_input.split()
print("Individual Words:")
for word in words:
    print(word)


# In[ ]:




