

====bash change string to array 
$  myline='this is new string'
$ myarr=($myline)
$  echo -e " ${myarr[0]} , ${myarr[1]} , ${myarr[2]} , ${myarr[3]} "
 this , is , new , string 
OR 
$  myarr=(this is an array) 
$ echo -e " ${myarr[0]} , ${myarr[1]} , ${myarr[2]} , ${myarr[3]} "
 this , is , an , array 
OR
myarr=('item1' 'item2' 'item3')

====Array examples 
array=( one two three )
More examples:
files=( "/etc/passwd" "/etc/group" "/etc/hosts" )
limits=( 10, 20, 26, 39, 48)
To print an array use:
printf "%s\n" "${array[@]}"
printf "%s\n" "${files[@]}"
printf "%s\n" "${limits[@]}"

===length of Array 
## define it
distro=("redhat" "debian" "gentoo")
## get length of $distro array
len=${#distro[@]}
## Use bash for loop 
for (( i=0; i<$len; i++ )); do echo "${distro[$i]}" ; done

===itereate through array
for i in "${arrayName[@]}"
do
   # do whatever on $i
done
for i in "${serverList[@]}"
do
echo $i
done
=====
#Declare a string array
LanguageArray=("PHP"  "Java"  "C#"  "C++"  "VB.Net"  "Python"  "Perl")
 
# Print array values in  lines
echo "Print every element in new line"
for val1 in ${LanguageArray[*]}; do
     echo $val1
done
echo ""
 
# Print array values in one line
echo "Print all elements in a single line"
for val2 in "${LanguageArray[*]}"; do
    echo $val2
done
echo ""
https://linuxhint.com/bash_loop_list_strings/   
https://stackabuse.com/array-loops-in-bash/

====================================================
======loops 
count=0
while [ count -lt 10 ] ; do ; echo $count ; (( count++))  ; done 
while [ count -le 10 ] ; do ; echo $count ; count=$(($count+1)) ; done 
count=0  
while ((count <= 10)) 
do ; echo $count ; count=$(($count+1)) ; done 
count=0  
until [ $count -gt 10 ]  ; do ;   echo "$count"
    count=$(( $count + 1 ))
done  

for (( n=1; n<=10; n++ ))  
do  
    echo "$n"
done 

users=(John Harry Jake Scott Philis)  
for u in "${users[@]}"  
do  
    echo "$u is a registered user"
done  




====================================================
====logical operators
http://tldp.org/LDP/abs/html/comparison-ops.html  

====integer comparison
-eq
is equal to
if [ "$a" -eq "$b" ]

-ne
is not equal to
if [ "$a" -ne "$b" ]

-gt
is greater than
if [ "$a" -gt "$b" ]

**** The == comparison operator behaves differently within a double-brackets test than within single brackets.
[[ $a == z* ]]   # True if $a starts with an "z" (pattern matching).
[[ $a == "z*" ]] # True if $a is equal to z* (literal matching).

[ $a == z* ]     # File globbing and word splitting take place.
[ "$a" == "z*" ] # True if $a is equal to z* (literal matching).
 
if [[ "$a" < "$b" ]]
if [ "$a" \< "$b" ]
Note that the "<" needs to be escaped within a [ ] construct.


======================================
