# 20 Jan, 2018
# 30 Jan, 2018


from sys import argv
script, user_name = argv
prompt = f'{user_name}> '
print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have at {lives}?")
computer = input(prompt)

print(f"""
All right, so you said {likes} about liking me.
You lives in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
