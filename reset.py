import os

# hard reset to origin master
os.system("git reset --hard")
os.system("git fetch origin master")
os.system("git pull origin master")

print("Done!")