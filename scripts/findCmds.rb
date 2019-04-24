

find cmd scripts
find command
scripts
awk , cut ,  etc 

---------find commads -------------

To change ownership of link itself instead of pointed file
chown -h edw01:edw  sched
chown -h -R cauagt pcm

command to find link files
 find . -type l -print -exec chown -h root:system {} \;
  find . -type l -print
find . -type l -print -exec ls -al {} \;

find   xargs  usage
find /abinitio -print0 |xargs -0  chown -h root:sys
find /abinitio -print0 |xargs -0  ls –dl

command to find file with specific userid find  -exec  usage 
find . –user  userid/username
find . -user   501
find /users  -user sobyjose -exec ls -l {} \; -exec echo {}  \;
   
command to find file with specific group
find / -group groupid/groupname
      find / -group   503/osa
command to find files with specific name
  find . -name wk_mers_da* -print -exec chown -h edw01:edw {} \;
find . -name wk_mers_da -print -exec ls -al {} \;

command to find the file with specific sizes
find . –size 2048      (file with 1MB size)
find . –size +2048    (files more than 1MB size)
find . –size -2048    (file more than  1MB size)

To merge  Directories using find command 
cd ${SOURCE};
find . -type d -exec mkdir -p ${DEST}/\{} \;
find . -type f -exec mv \{} ${DEST}/\{} \;
find . -type d -empty -delete

-----!! can use  rsyc command also to merge directories 
rsync -av /images /images2 
If images with the same name exist in both directories, the command above will overwrite /images2/SOMEPATH/SOMEFILE with /images/SOMEPATH/SOMEFILE. 
If you want to replace only older files, add the option -u. If you want to always keep the version in /images2, add the option --ignore-existing.
If you want to move the files from /images, with rsync, you can pass the option --remove-source-files.


  list files with size more than 20MB and sort in revers order

find ../apps  -size +40960 -exec ls -l {} \; |sort -r -k 5

----- awk , cut , sed ,grep   ---------------------------------- 

More  than one command in a line is possible with  “;”

   date;pwd

->  grep commands
dmidecode -t baseboard |egrep -i "Desig|Bus|type|status"
dmidecode -t baseboard |grep -B1 -A3 Ethernet |egrep -i "Desig|Bus|type|status"
      -L, --files-without-match
grep -L : /sys/class/net/*/address
     -l, --files-with-matches
grep -l : /sys/class/net/*/address
       -H, --with-filename
grep -H : /sys/class/net/*/address
        -h, --no-filename
grep -h : /sys/class/net/*/address
       -n, --line-number

grep -n : /sys/class/net/*/address





---------script   examples --------------

Header of a cript
#!/bin/sh
set –x      -----------> to display commads on prompt
chfs  -m    /p1n4/edwprod1/partition25/mptsc1             /edwprod1/partition25/mptsc1


To list  the lines in a file
for i in `cat ./soby/userlist`
do
 print $i
done

To read names from a file and create homedirectories and set  ownerships
#!/bin/sh
#set -x

for i in `cat ./soby/userlist`
do
dirc=$i
mkdir  $dirc
owne=$i
grp=`lsuser -a pgrp $i |awk '{print $2}' |cut -c 6-`

chown $owne:$grp  /home/$dirc
print $dirc
done

To list all the physical volumes with pvid in the order of  bcu volume groups (used in dwpf3n1)

for i in $(lsvg  |grep bcu)
do                        
for j  in  $(lsvg -p  $i |awk '{print $1}' )
   do                     
        lspv  |grep $j    
    done                  
done                      

To send mail with bcc by reading the ids from file idlist
#!/usr/bin/ksh
if (( $#  <  2 )); then
print "no subject and To address "
exit
fi
subject=$1
to=$2
bcclist="~b "
for i in `cat  idlist`
do
bcclist=`echo "$bcclist " "$i"`
done
echo $bcclist
echo "$bcclist" > finalmail
echo "this is the body of message\n" >> finalmail
cat /etc/motd >> finalmail

mail -s "$subject"   $to  <  finalmail

to fill filesystem  with dummy files
i=11
while (( $i  <  330000 ))
do
if mkdir tst${i}
then
echo tst${i}
touch   tstfile${i}
cat  firstfile > tstfile${i}
cd tst${i}
touch tstfile${i}a
cat /testfs/firstfile > tstfile${i}a
cd /testfs

else
break
fi
i=$(($i + 1))
done

script to list the Physical volumes in bcu volume groups (server dwpf3n2)
for i in $(lsvg |grep bcu |awk '{print $1}')
do
lsvg -p $i
sleep 1
done
---------------------------------------
Loop for 0 to 100

i=0
while [ $i -le 100 ]
do
echo "Hello Soby checking the value of i=$i"
i=`expr $i + 1`
sleep 2
done
-----------------------------------------------------------------------
List all the  wwwn of all fcs adapters in system
  for i in $(lsdev -Cc adapter |grep fcs |awk '{print $1}')
 do
 k=`lscfg -vl $i |grep -i network `
 echo $i "---->  "$k
 done
---------------------------------------------------------------------------------
for i in $(lsvg)^Jdo^Jecho $i;lsvg -p $i  ;echo;echo;sleep 2^Jdone

---------------------------------------------------------------------------
Recreate  user after remove it

lsuser -f sobtest2  > /tmp/sobtest2.0
  vi /tmp/sobtest2.1     --> put the stirng values in double quotes
cat /tmp/sobtest2.0  |tr  '\n'  ' ' >/tmp/sobtest2.1

  vi /tmp/sobtest2.1     --> add mkuser command at begining and username at end
chmod 755 /tmp/sobtest2.1
rmuser -p sobtest2
rm -r sobtest2
/tmp/sobtest2.1
echo "username:passwd" |chpasswd


lsuser -f  larsk01  > /tmp/larsk01.0
  vi /tmp/larsk01.0     --> put the stirng values in double quotes
cat /tmp/larsk01.0  |tr  '\n'  ' ' >/tmp/larsk01.1
  vi /tmp/larsk01.1     --> add mkuser command at begining and username at end
chmod 755 /tmp/larsk01.1
rmuser -p larsk01
mv  /home/larsk01  /home/larsk01.old2
/tmp/larsk01.1
echo  “larsk01:temppass” | chpasswd

-------------------------------------------------------------------



    ln /tmp/t.sh
    ls -al
    ln /tmp/t.sh a
    ls -al
    cat *
    echo *
    ls *
    ls *.*
    ls *.
    ls *.
    echo ?.*
    echo ?
    echo *.?
    echo .[a-z]
    echo *.[a-z]
    echo *.[!a-p]*
    sort  file1

sort
34
67
87
2
6
7
CTRL d
   sort 34 56 2 8 45 75
    ls x* 2> err      redirecting stndard output
    cat e*
    wc
    wc err
    wc
    ls | sort
    ls | wc –l

echo line 1 > file1  ( write to file1)
echo  line 2  >> file1  (append to file1)
cat file1 >> file2

ed  file1
 r.   ->period matches any single character
1,$p     print all the lines
/ ... /  look for three chars surrounded by blanks
/   repeat  last search
1,$s/p.o/xxx/g  change all p.o  to xxx
1,$p  print all the lines

/^the/    find the line that starts with the
1,$s/^/xx/      insert  xx at the begining of each line
^     beging of the line
$     end of the line

abc$   matches characters 'abc' at the end of a line
^abc   matches chractes 'abc'  at the begining of line

\.$    matches any line ends with period
^\.    matches any line start with period

1,$s/..$//   delete the two characters form each line

^$  matches any line contains no characters
^ $   matches lines with single space character
/the/  find line containing the
/[tT]he/  look for the or The
/      continue serach  , 'n' also do same thing
/     once again

1,$s/[aeiouAEIOU]//G   delete all the vowels
/[0-9]/ find a line containing a digit
/^[A-z]/  Find a line that starts with an uppercase letter
1,$s/[A-Z]/*/g    change all uppercase letters to *
[^A-Z]   matches any character except an uppercase letter
[^A-Za-z]   matches any nonalphabetic character

1,$s/[^a-zA-Z]//g   delete all nonalphabetic characters

