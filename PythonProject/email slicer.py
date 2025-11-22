email=input("Enter the name of your email:")
index=email.index("@")
username=email[: index]
domain=email[index+1:]
print(f'your username is {username} and domain name is {domain}')
