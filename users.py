import os

print(os.listdir("/home/"))
print(os.getuid("pram"))

running = True

usrslst = []
permlst = []
while running:
    user = input("input user: ")
    
    if user == "done":
        break

    userperm = input("input (a)dministrator or (s)tandard: ")

    usrslst.append(user)
    permlst.append(userperm)

for usr in os.listdir("/home/"):
    if usr not in usrslst:
        os.system(f"sudo userdel -r {usr}")

    
    
