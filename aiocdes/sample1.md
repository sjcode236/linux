




```
#!/bin/bash

# Define the directory to search
dir='/commons/share'

# Define the minimum file size in MB
min_size=100

# Define the output file name
output_file='large_files.txt'

# Find all files in the directory and its subdirectories
# that are larger than the minimum size, and save the output to a file
find "$dir" -type f -size +"$min_size"M -exec du -h {} \; > "$output_file"



```

```
 code to include the owner of each file in the report:
 #!/bin/bash

# Define the directory to search
dir='/commons/share'

# Define the minimum file size in MB
min_size=100

# Define the output file name
output_file='large_files_with_owners.txt'

# Find all files in the directory and its subdirectories
# that are larger than the minimum size, and save the output to a file
find "$dir" -type f -size +"$min_size"M -exec ls -lh --author {} \; > "$output_file"
This code uses the ls -lh --author command in the -exec option to display the file size, path, and owner of each file found. The output of this command is redirected to a file with the name stored in the output_file variable. The resulting file, large_files_with_owners.txt, will contain information on the size, path, and owner of all files in the /commons/share directory and its subdirectories that are larger than 100 MB.




sjbuy3@gmail.com
awk usage
awk is a powerful text processing tool that can be used to manipulate and extract data from text files. It is especially useful for working with structured data, such as the output of other commands.

Here's a simple example of using awk to extract the owner of each file from the report generated in the previous script:

bash
Copy code
#!/bin/bash

# Define the directory to search
dir='/commons/share'

# Define the minimum file size in MB
min_size=100

# Define the output file name
output_file='large_files_with_owners.txt'

# Find all files in the directory and its subdirectories
# that are larger than the minimum size, and save the output to a file
find "$dir" -type f -size +"$min_size"M -exec ls -lh --author {} \; > "$output_file"

# Use awk to extract the owner of each file from the report
awk '{ print $3 }' "$output_file"
In this code, awk '{ print $3 }' "$output_file" extracts the 3rd field (the owner) from each line of the large_files_with_owners.txt file and prints it to the screen. The awk command takes the input file as an argument and the script inside single quotes ' defines how to process each line. In this case, the print statement is used to extract and print the 3rd field from each line.




sjbuy3@gmail.com
write this code in python 
Here's a Python equivalent of the previous bash script:

python
Copy code
import os
import subprocess

# Define the directory to search
dir_path = '/commons/share'

# Define the minimum file size in MB
min_size = 100

# Define the output file name
output_file = 'large_files_with_owners.txt'

# Use subprocess to run the find command and save the output to a file
with open(output_file, 'w') as file:
    find_command = "find '{}' -type f -size +{}M -exec ls -lh --author {{}} \;".format(dir_path, min_size)
    result = subprocess.run(find_command, stdout=file, shell=True)

# Read the output file and extract the owner of each file
with open(output_file, 'r') as file:
    for line in file:
        owner = line.split()[2]
        print(owner)
In this code, the subprocess module is used to run the find command and save its output to a file. The subprocess.run function is called with the find_command string, which is constructed using the format method of string objects. The stdout parameter is set to the file object to redirect the output of the find command to the file. The shell=True argument is used to run the command in a shell.

After the find command has been run and its output has been saved to a file, the code reads the file and extracts the owner of each file using the split method of string objects and indexing. The extracted owners are printed to the screen.
```

```
Here's a simple example of using awk to extract the owner of each file from the report generated in the previous script:
#!/bin/bash

# Define the directory to search
dir='/commons/share'

# Define the minimum file size in MB
min_size=100

# Define the output file name
output_file='large_files_with_owners.txt'

# Find all files in the directory and its subdirectories
# that are larger than the minimum size, and save the output to a file
find "$dir" -type f -size +"$min_size"M -exec ls -lh --author {} \; > "$output_file"

# Use awk to extract the owner of each file from the report
awk '{ print $3 }' "$output_file"
```

```
import os
import subprocess

# Define the directory to search
dir_path = '/commons/share'

# Define the minimum file size in MB
min_size = 100

# Define the output file name
output_file = 'large_files_with_owners.txt'

# Use subprocess to run the find command and save the output to a file
with open(output_file, 'w') as file:
    find_command = "find '{}' -type f -size +{}M -exec ls -lh --author {{}} \;".format(dir_path, min_size)
    result = subprocess.run(find_command, stdout=file, shell=True)

# Read the output file and extract the owner of each file
with open(output_file, 'r') as file:
    for line in file:
        owner = line.split()[2]
        print(owner)
        
```

```
import os

# Define the directory to search
dir_path = '/commons/share'

# Define the minimum file size in MB
min_size = 100 * 1024 * 1024 # convert to bytes

# Define the output file name
output_file = 'large_files.txt'

# Find all files that are larger than the minimum size and save the output to a file
with open(output_file, 'w') as file:
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.getsize(file_path) > min_size:
                file.write(file_path + '\n')

# Read the output file and print the contents
with open(output_file, 'r') as file:
    for line in file:
        print(line.strip())
        
```
```

mport os
import pwd
import grp

# Define the directory to search
dir_path = '/commons/share'

# Define the minimum file size in MB
min_size = 100 * 1024 * 1024 # convert to bytes

# Define the output file name
output_file = 'large_files.txt'

# Find all files that are larger than the minimum size and save the output to a file
with open(output_file, 'w') as file:
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.getsize(file_path) > min_size:
                # Get the owner and group ID of the file
                stat = os.stat(file_path)
                uid = stat.st_uid
                gid = stat.st_gid
                
                # Get the owner name and group name
                owner = pwd.getpwuid(uid).pw_name
                group = grp.getgrgid(gid).gr_name
                
                # Write the file path, owner, and group to the output file
                file.write(f"{file_path} owned by {owner}:{group}\n")

# Read the output file and print the contents
with open(output_file, 'r') as file:
    for line in file:
        print(line.strip())
```







