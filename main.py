# Check if a String starts with any element from List in Python

my_str = 'hello'

my_list = ['apple', 'one', 'he']

# ✅ Using str.startswith() with a tuple

if my_str.startswith(tuple(my_list)):
    # 👇️ this runs
    print('string starts with at least one of the elements from the list')
else:
    print('string does NOT start with any of the elements from the list')

# 👇️ True
print(my_str.startswith(tuple(my_list)))