user_input = input("-")
user_list = list(user_input)
print (user_list)
text=[]
for i in user_list:
    text.append(int(ord(i)))
print(text)


work = (0)
for i in text:
    text[0+work] = text[0+work] + 2
    work += 1


print(text)


user_list = ""
for i in text:
    user_list += chr(i)

print (user_list)    
 
