s = input("Enter Email address")
username = ''
domain_name = ''
user_index = s.index("@")
username += s[0:user_index]
domain_name += s[user_index+1:]
print("username: ", username, " domain name: ", domain_name)
