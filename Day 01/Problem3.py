import os

# Specify the directory path
path = "/python"

# Print all files and folders in the directory
contents = os.listdir(path)

for item in contents:
    print(item)