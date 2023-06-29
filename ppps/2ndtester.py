import string
name = 'A& s,@H: v?an-67i'
name_list = [char for char in ''.join(name.split()) if char.isalpha() and char not in string.punctuation and char not in string.digits]
name_list = [elem.lower() for elem in name_list]
print(name_list)