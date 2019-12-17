import os
print("cwd before:", os.getcwd())
os.chdir("../")
print("cwd move up one level:\n", os.getcwd())