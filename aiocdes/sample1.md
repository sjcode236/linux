




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
