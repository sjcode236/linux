rhcsa training


http://blog.fpmurphy.com/

www.certdepot.net/

https://www.centos.org/download/
Minimal ISO's are here if anyone needs:
ftp://ftp.osuosl.org/pub/centos/7/isos/x86_64/

ls -alZ

man -k
date
time date

whoami
who am i
who

alias
unalias ls

less
more
cd /var/log ;ls
dmesg
lastlog --> last login
cd /var/log/anaconda

yum -y groupinstall "X Window System" "GNOME"
systemctl set-default  graphical.target

select option poweron to firmware/BIOS  to goto  BIOS  on startup

---OS installation notes ----
disale Kdump for practise
security policy -> "change  content"  to not select  policy
change hostname under  network & hostname
software selection -> select "server with GUI"

----------------------

tty = tele type terminal
pts =

during the booting when GRUB menu start displaying
type e  to edit kernel parameters 
when the grub start (when start displaying  kernels )
press ctrl-G  to get mouse focus to vmscreen ; 
press <tab>  to stop timer ; then
e   to enter the  grub editor
add below line "init=/usr/bin/bash" at  end of kernel line "linux16 /vmlinuz-3.00.***  root=/dev/mapper/centos-root rord.lvm.lv=centos/root init=/usr/bin/bash 
press ctrl-X to  start  booting to command  prompt
page 193 in GHoRI book 


page 197   ghoori book
Recomended way to change root password
add below line "init=/sysroot/bin/sh" at  end of kernel line "linux16 /vmlinuz-3.00.***  root=/dev/mapper/centos-root rord.lvm.lv=centos/root  init=/sysroot/bin/sh

chroot /sysroot
mount -o remount,rw /
passwd   ( set  root password )
touch /.autorelabel
exit
reboot

Finnbarr Murphy's blog
`this fastest way to gain root access
http://blog.fpmurphy.com/2016/10/fastest-way-to-gain-root-access-in-rhcsa7-exam.html
fpm@fpmurphy.com
Finnbarr Murphy

add below line "init=/bin/bash" at  end of kernel line "linux16 /vmlinuz-3.00.***  root=/dev/mapper/centos-root rord.lvm.lv=centos/root
init=/bin/bash 

press ctrl-X to  start  booting to command  prompt

it will boot to command prompt
/bin/mount -o remount,rw /
passwd (change  root password )
ls -lZ /etc/shadow  /etc/passwd
/sbin/load_policy -i
/sbin/restorecon -v /etc/shadow
ls -lZ /etc/shadow  /etc/passwd
exec /sbin/init

`practise to change root password  in 8  mins for exam


To get to single user mode  at GRUB menu add to kernel line
systemd.unit=single.target  or (simple  s or S or  single or 1)
to get to rescue mode add to kernel line
systemd.unit=rescue.target
rescue mode similar to single mode.to rescue mode normally boot from CD whereas  single mode normally boot from Hdisk

Runlevel Target Units             Description
0 runlevel0.target, poweroff.target Shut down and power off the system.
1 runlevel1.target, rescue.target     Set up a rescue shell.
2 runlevel2.target, multi-user.target Set up a non-graphical multi-user system.
3 runlevel3.target, multi-user.target Set up a non-graphical multi-user system.
4 runlevel4.target, multi-user.target Set up a non-graphical multi-user system.
5 runlevel5.target, graphical.target Set up a graphical multi-user system.
6 runlevel6.target, reboot.target     Shut down and reboot the system.   

== Changing the Default Target
systemctl set-default multi-user.target 
==Changing the Current Target
systemctl isolate name.target
==Changing to Rescue Mode (in Linux 7, rescue mode is equivalent to single user mode and requires the root password.)
systemctl rescue  or systemctl isolate rescue.target
==Changing to Emergency Mode
systemctl emergency   or  systemctl isolate emergency.target
    Emergency mode provides the most minimal environment possible and allows you to repair your system even in 
 situations when the system is unable to enter rescue mode. In emergency mode, 
 the system mounts the root file system only for reading, does not attempt to mount any 
 other local file systems, does not activate network interfaces
========================================
CHAPTER 36. BASIC SYSTEM RECOVERY
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/installation_guide/ap-rescuemode

30.5. VERIFYING THE INITIAL RAM DISK IMAGE
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-verifying_the_initial_ram_disk_image
30.6. VERIFYING THE BOOT LOADER
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s1-kernel-boot-loader#s3-kernel-boot-loader-grub

 
 
 
*************** Jan 24 -2007  ----------------------------------------
Shell  Commands and utility

stty  ==>  set the terminal settings
stty -a
stty sane  ==>
stty cols 80
stty rows 40
clear
setfont -h
ls /lib/kbd 
ls /lib/kbd/consolefonts |less
alias ll
lspci
lsusb

**************  yum  -------------------------------------------------
intense book 140 

/etc/yum.conf  
==This file is the key cofiguration file,you can define yum repositories in it on sepereate sections,
    but better approach is to store repos in /etc/yum.repos.d
 /etc/yum.repos.d/




df -ih
df -h
df -m
find / -type f -name "*.iso"


vi CentOs-Base.repo
set  enabled=0  to all stanzas to disable them

***creating dvd yum repository *******
mount -o ro /dev/cdrom  /mnt
vi  /etc/yum.repos.d/dvd.repo 
[centos72-full-media]
name=CentOS-$releasever - Media
baseurl=file:///mnt
gpgcheck=0
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#yum repolist
***make repo from ISO file *******
=copy the centosbase ISO  to /var/tmp
= and mount the iso file to /var/centos72
mount -o loop /var/tmp/CentOS-7-x86_64-Everything.iso  /var/centos72  
cd /etc/yum.repos.d
=disable all repos  by setting  enabled=0 
make exam.repo
vi /etc/yum.repos.d/exam.repo
[centos72-full-media]
name=CentOS-$releasever - Media
baseurl=file:///var/centos72/
gpgcheck=0
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

yum repolist
======================================

yum repolist
yum list
yum whatprovides */lspci
yum whatprovides */ls
yum whatprovides */iostat

in exam they will give url for thepackage location
then put in examrepo file
baseurl=ftp://192.168.1.1/var/dir32/

parctise to make repo  in 3 mins
*************************************

`***How to fix duplicate packages in yum ******************************
verify yum-utils  installed or install it 
yum list installed  yum-utils*
yum-complete-transaction
==To show duplicate packages on the system:
package-cleanup --dupes
==To removed  duplicate packages (yum verify and erasing the duplicates)
package-cleanup --cleandupes
==update the system again with a standard yum update command. This should take care of any missing dependencies that may have been removed in the previous process
yum update
==to see if there’s any remaining trouble with the yum database
package-cleanup --problems
Loaded plugins: fastestmirror
No Problems Found

`***ADDING, ENABLING, AND DISABLING A YUM REPOSITORY ********************
===To add a .repo repository to your system and enable it, run the following command as root:
yum install -y yum-utils  ==> yum-utils provide  yum-config-manager:
yum-config-manager --add-repo repository_url
# yum-config-manager --add-repo http://www.example.com/example.repo
Loaded plugins: product-id, refresh-packagekit, subscription-manager
adding repo from: http://www.example.com/example.repo
grabbing file http://www.example.com/example.repo to /etc/yum.repos.d/example.repo
example.repo                                             |  413 B     00:00
repo saved to /etc/yum.repos.d/example.repo
===To enable a particular repository or repositories
yum-config-manager --enable repository…
 yum-config-manager --enable example\*
===to disable and enable repos inline with yum command
yum --disablerepo=* --enablerepo=rhel* repolist
===specifying  optional  repository enable  when installing a package with yum.
 yum install rubygems --enablerepo=rhel-6-server-optional-rpms
===To disable a Yum repository
yum-config-manager --disable repository…
===another way to disable a repo is 
vi /etc/yum.repos.d/redhat.repo  and set enabled=0   to  disable the repo 
yum repolist enabled 
===command to patch or update  with yum 
yum --disablerepo=* --enablerepo=rhel* update
===command to use  to patch to exclude  dhcp
yum update --exclude=dhclient --exclude=dhcp-libs --exclude=dhcp-common 
===the downgrade command for dhclient 
yum downgrade -y dhcp-common dhcp-libs dhclient

***Using Subscription-Manager***************************
===Subscription-Manager provides it's own utility to enable & disable repositories within the redhat.repo file:
 subscription-manager repos --list
 subscription-manager repos --enable=rhel-6-server-optional-rpms
 subscription-manager repos --disable=rhel-6-server-optional-rpms
===Disabling the Subscription-Manager Repository:-
	The default redhat.repo repository can be disabled by editing the Subscription-Manager configuration and setting the manage_repos value to zero 
# subscription-manager config --rhsm.manage_repos=0
-----------------------------------------------------------------------------------------
intense school 29
ls -alZ
ls -al exam.repo
stat  exam.repo

pwd
cd ~  -->  goto home directory
cd -  --> to goto last  directory

mkdir
rmdir
rm -rf dir3
echo $?  to  see  the status of last command
0  means success, other number mean  fail

diff  between binarry file and text file ?
text file -> a file got new lines it
binary file -> a file which dont have new lines in it

echo -n hello   --> no new line at end of output
echo -e "hello \t\t\v\vclass"  --> two horizontal tab and two vertical tab

rmdir -p common/example

id
id -u
id -g
uptime
groups
who
whoami
http://www.linuxjournal.com/article/9001
last
lastb
last reboot
lastlog
who -b   last  boot time
who -r   show the run level

/etc/passwd
/etc/shadow  only root can read shadow file

who is superuser in windows
=trusted  installer

uname -a
cat /etc/*release  to see  version detail of OS
ls  /etc/*release

To See  Kernel verion 
uname -r
cat /proc/version
cat /proc/cmdline
dmesg | grep Linux
ls /boot
rpm -q kernel
In  Ubuntu, try:
$ dpkg --list | grep linux-image

www.rpmfind.net  -->site to search to file rpms

wsus -->its windows  patch repository in windows
gop  -->its windows group policy
redhat satelite server -->its  repository server in linux

cat /etc/hostname
hostnamectl
cat /etc/machine-id
hostnamectl set-hostname hostx.example.com
static hostname stored in /etc/hostname
pretty hostname stored in /etc/machine-info

date
timedatectl
  set-time
  set-date
  set-timezone
timedatectl list-timezones |grep America
timedatectl set-timezone America/Torento
timedatectl set-time 2015-08-12

echo $PATH
which ldd
which  lspci

wc
lspci
lspci -v
lspci -vv
lsusb
lscpu

printenv
set
ghori book 38
intensBook page49
gzip /root/anaconda-ks.cfg
gunzip anaconda-ks.cfg.gz

bzip2 /root/anaconda-ks.cfg
bunzip2 anaconda-ks.cfg.bz2

tar cvf   create a tar ball
tar tvf   list contents of tar ball
tar xvf   extract  a tar ball
j --filter archive through  bzip2 file
z --filter archive through  gzip file
r --append or update files to a  archive file
W --verify a archive file
tar cvjf  demo.tar.bz2  *
file demo.tar.bz2
tar cvzf demo.tar.gz   *


gedit myfile

GHORI book 43
vim (vi)  myfile
search for vi cheatsheet
cw change word
dw delete word
2dd delete 2 line
2yy  yank 2 lines
p  paste
. repeat  last  editing command
/  search forward
n  search next forard
N search  next reverse
?  search  backward
g/G goto first/last line
0/$ goto to

:%s/one/ONE/g  -->replace  one to ONE in all lines
%  means all line
g means global otherise above cmd only change first occurance


cat -vet testfile  -->list  hidden characters also in file

ex  -->  another editor
nano  -->  another simple editor
yum install nano

abebooks.com
ultimate guide to vi and text editor

if somebody remove ls command  ?
echo *


which man
--searching by keyword
man -k password
apropos  password
--quick search in manpage
whatis yum.conf
man -f yum.conf

/usr/share/doc -> documentation of installed packages in it
info -->  command to see tutorial of command
info  passwd
info  ls

better book for RHCE  exam
RHCE https://www.amazon.com/RHCSA-Linux-Certification-Study-Seventh/dp/0071841962 
-----------------------
file system tree
intense bookP 64
GHORI bookp57-60
/boot file system
-contains linux kernel
-boot support
-boot configuration
-default size 500MB

cd /boot
cd grub2
cat grub.cfg  -->  main grub configuration file
grub   contain  kernerl file , initram etc.
vmlinu***   -->kernel file name

/opt -> optional file system

/dev  -> device file system

/proc  -> process file systems , every process got entry into it
cat /proc/version
cat /proc/mounts
cat /proc/cpuinfo
cat /proc/meminfo

/sys  ->info  about hardware
/tmp

cd /usr/share
find ./ -type f -name magic

file /dev/tty0
file /dev/xvda

stty -a

mkdir
vi
cat > file1
cat >> file2

more  ->paging filter
less  ->faster
tail
head
alias
mv  -> move or rename
cp -i  ->  will ask for confirmation
cp -r
cp -R
rm
rm -r
rm -i -> ask for confirmation

GHoRI  69
lsattr , chattr  -> manager  file extended  attributes
chattr +a  file3 -> change file to only be appended
chattr +i file3  ->change file atribite to immutable (cannot delete,rename,change)
lsattr  file*
chattr -i -a file3
lsattr file*

GHORI bookp 73
ln  file1 file2
hardlink share(same)  inod number
hardlink can be used only on files not on directories
ls -li file*

softlink can be used on directories & files
ln -s file3(target)  file4(link)
file4 -> file3
rm file4   -> remove the link

permission  types
-rwxrwxrwx
user,group,other
-rw-r--r--  (644)
drwxr-xr-x  (755)

permission setting
UGO , symbolic
chmod u=rwx,go=rx file2
chmod u+wx  file3

Octal , numeric
chmod  777 file2

mkdir tmp
touch file1 file2

umask

umask 22
umask
0022
file-dir permission will be
644  -> for files
755  -> for dirs

chown  ->  change ownership
chgrp  ->change group

GHORI bookp 76
--sepecial permission (----  first bit is for special perms)
setuid -> for executale files
setgid -> for directories
sticky bit -> for directories
4777  ->  setuid
2777  ->  setgid
1777  ->  set  sticky it
7777  ->  setuid,setgid,sticky bit
-rwSrwSrwT ->means  exec permission missing (capital S)
-rwsrwsrwt ->got exec  permission (small s)
chmod u+s  filename
chmod g+s filename
chmod o+t filename
In the exam atleast 30 times will be setting permissions

----jan 25-2017--------------------------
shell -> interface to kernel
sh csh ksh(aix) bsh  dash(ubuntu)
intens book 96

printenv -> print my env variables
printenv |grep HIST
history  , history 20
chsh ->  to change shell
!45  ->  run the 45th command in history
!ch 
!!  -> run the last command
!$  ->  arguements
!^ 
rc ->means  run control eg  .cshrc
env , export -> show  environment variales
printenv
set  -> show local and environment variable
unset  HOME-> remove  environment variable HOME
VARIABLE="TESTING"
echo $VARIALE
export VARIABLE="TESTING"
env |grep VARIABLE
echo $SHLVL  ->  show shell level

$export PS1="<$LOGNAME@`hostname`:\$PWD>"
$export PS1="<$LOGNAME@`hostname`:\$PWD>"

standard  input ,ouput ,error can be redirected
file discriptores
0  is stdin
1  is stdout
2  is stderror

date > datefile
cat < datefile
date >> datefile
date > /dev/null

1>file  redirect stdout to filename
1>>file redirect and append stdout to file
2>file  redirect stderrr to file
2>>file redirect and append to file
&>file  redirect both stdout and stderr to file
echo  $myvar  &>/tmp/variale.log
echo $HISTFILE
echo $HISTSIZE

set -o vi 
~
~+
~-

GHORI book98
grep
-n  show line numer
-v  show  line not match the search
-w  show exact  string
-i  ignore case
grep ^root  -> lines begin with
grep bash$ ->lines  endwith
grep ^$ /etc/passwd ->print emptylines
|  ->  for OR ( grep root|user  /etc/passwd)
egrep  or grep -E  -> recognise special characters

grep metacharacters and wildcards
?  preceding item optional and matched at most once
*  preceding item matched zero or more times
+  preceding item matched one or more times
.  match single character
bash metacharacters and wildcards
* matches 0 or more characters
  ls /var/log/*.log
. matches one character
  grep -w acce..  /etc/lvm/lvm.conf
? matches  one  character
  ls -d /var/log/???
[] define a set of characters
   ls /usr/sbin/[yw]*

--processes
pidof   crond
pgrep  crond
ps -U root
ps -G qmenu
tty
ps -l
ps -al
ps -aef

nice
+19 is lowest and -20 is highest  priority
nice -2 /usr/script.sh  -> nice value +2
nice --2 /usr/script.sh -> nice value -2
renice +2 PID -> nice vlaue of +2 (  nice and renice  different syntax)
sleep 5
sleep 50 &

--kill command
kill -l
1 -> SIGHUP hangup and restart process
2 -> SIGINT  interrupt  execution
9 -> SIGKILL   complete termination
15 -> SIGTERM  gracefull termination

pkill  -> kill process by name
pkill crond
kill `pidof crond`

^Z -> suspend a job
^C -> kill the running process
sleep 200
^Z
bg
jobs
fg
fg 3 (forground job 3)


GHORI book113
atd  -> run job  onetime in future
/var/spool/at/spool  ->
at -l
atrm 1

yum list installed at
yum -y install at

Run jobs  on
/var/spool/cron  and /etc/cron.d
crontables
 /etc/crontab
user cron entry in
/var/spool/cron/username
system has jobs in
/etc/cron.d
crontab -e
crontab -l
yum list installed |grep cron
yum -y install cronie crontab
user crontab has 6 filed
system crontab has a 7th , user filed 
* * * * * username commandToExecute
minut(0-59)
hour (0-23)
day of month (1-31)
month (1-12)
day of week (0-6)
10 2 * * * command (for user oracle crontab)
10 2 * * * oracle  command  ( in system crontab)
0,30 4,16 * * *  username command
*/5 1-5 1,15 */2 *  command

practise  at and cron  to do it fast
--ghori book 117

chapter5
--softare package management
Ghori book123 , intenseBook30

yum -> yellowdog update modifier
/var/lib/rpm  ->metadata for packages are here

rpm -qa  -> query all package
rpm -q perl -> check a specific package
rpm -ql iproute -> check list of files in package
rpm -qc
rpm -qf -> check what package a file belong to
rpm -qd  -> documentation
rpm -qR -> list dependencies
rpm -qi -> display information
rpm -qip ->  to check what a package for
rpm --force
rpm -K
rpm -V ->verify integrity
rpm -v ->verbose
rpm -e

cd /tmp
mkdir demo
mv zzlib****.rpm demo
rpm2cpio ./zziplib***.rpm |cpio -di

finviz.com 
zdnet.com

yum
yum history list
yum history list all
yum history summary
yum history list 1..3

   


==kernel ======================================================================== 
modeprobe -h
modinfo dm_log

/etc/sysctl.conf   ==> kernel parameters in this file take effect on every reboot.
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_rmem = 4096 87380 16777216
==To enable them immediately without a reboot, use:
# sysctl -p /etc/sysctl.conf
# sysctl -a  ==>To see all of the currently configured values
==>To see the value of one particular item, use:
# sysctl -q net.ipv4.tcp_window_scaling

==>to set the value of one item without configuring it in sysctl.conf 
# sysctl -w net.ipv4.tcp_window_scaling=1

cat /proc/sys/net/ipv4/tcp_window_scaling
cat /proc/sys/net/ipv4/tcp_rmem



ghori book 213
===systemd targets  ================================================================


httpd is apache web server
yum install httpd
yum list installed |grep http
yum list installed  httpd
systemctl status httpd
systemctl status httpd -l
systemctl  stop httpd
systemctl disable httpd
google install apache webserver on centOS 7

systemctl get-default
systemctl set-default multiuser.target
systemctl isolate  multiuser.target


===system logging   ============================================
rsyslog
systemctl status rsyslog
cd /etc
ls logrotate*
vi logrotate.conf
cd /etc/logrotate.d/ ; ls
cat httpd

cat /var/log/boot
tail -f  /var/log/messages

systemctl status dbus
setenforce 0  -> make selinux liberal

journelctl /sbin/crond
journelctl /usr/bin/dbus-deamon



===chapter8--ghori236,intenseBook200 =======================
user and groups
/etc/passwd
/etc/shadow
/etc/group
/etc/gshadow


/etc/passwd 
username:x:uid:gid:GECOs comment:homedir:shell
apache:x:48:48:apache:/usr/share/httpd:/sbin/nologin
x ->means password in shadow file

man 5 passwd

/etc/shadow
user:password:lastchg days:mindays:maxdays:warndays:inactive days:disabledDays:

/etc/group
goupname:password:goupid:users

chage
gpasswd  ->group password
pwck
grpck
vipw
vigr

useradd -D  ->show the defaults
cat /etc/default/useradd

-u ->uid
-g ->group id

usermod G lpadmin bob
useradd -u 1010 -g 1010 -m -d /home/user3 -k /etc/sjel -s /bin/sh user3

wheel  ->this group users can 'sudo su - root' without password
grep wheel /etc/sudoers
wheel group group id 12
gpasswd wheel  ->set password for group
newgrp  ->login to a group
groups
passwd -l user ->lock user
passwd -u user   -> unlock user
usermod -L test ->lock user test
userdel test

setenforce 0
getenforce

cd /etc/selinux ;cat config
.bashrc

/etc/skel  ->this foldercontain the default files created in  user homedirectory at user creation

script order
/etc/profile
~/.bash_profile
~/.bashrc
/etc/bashrc

echo pass123 |passwd --stdin user3

chage -l user3

-----26 jan 7 -------------------------------
--partitions & disk management

lsblk  -> list disks(list block devices )
fdisk  make  nbr partition
gdisk  make gpt partition
parted  can make NBR/GPT partition

fdisk /dev/sdb
m
n
p
1

+200M
8e

n
p
2

+200M
w
lsblk



GHORI book270
parted /dev/sdb
help
print
mklabel msdos
(to make GPT type partition table ,run "mklabel gpt" instead)
print
mkpart primary  1 1g
print
quit

partprobe
parted /dev/sdb print
grep sdb /proc/partitions

to delete  MBR partition using parted
parted /dev/sdb
print
rm 1
print
quit
partprobe
parted /dev/sdb print
grep sdb /proc/partitions  


gdisk
/dev/sdc
?
o
y
p
n


+200M
L
8300 or 8e00
p
w
y
lsblk
gdisk -l /dev/sdc
grep sdc /proc/partitions

gdisk /dev/sdc
p
d1
p
w
y
q
gdisk -l /dev/sdc
grep sdc /proc/partitions

--lvm-----

parted /dev/sdc mklabel msdos
parted /dev/sdc mkpart primary 1 201m
parted /dev/sdc print
pvcreate /dev/sdb /dev/sdc1
vgcreate -s 16 vg01 /dev/sdb /dev/sdc1 -v
vgs -v
vgscan
vgs vg01
vgdisplay -v vg01
pvs -v
pvscan
pvsdisplay /dev/sdb
lvcreate -L 600 vg01 -v   -->  default unit in MB (600MB)
lvcreate -L 1.3g -n oravol vg01
lvs
lvscan
lvdisplay /dev/vg01/lvol0
pvcreate /dev/sdd -v
vgextend vg01 /dev/sdd -v
pvs
lvextend -L 1g /dev/vg01/lvol0 (lvextend -L +400m /dev/vg01/lvol0)
lvresize  -L 2g /dev/vg01/oravol (or lvresize -L +700m /dev/vg01/oravol)

lvrename vg01 lvol0 lvolnew
lvs |grep vg01

lvreduce  -L 800m /dev/vg01/lvolnew ( -L -200m)
lvresize  -L 700m /dev/vg01/oravol  ( -L -500m)
lvs
lsblk
lvremove -f /dev/vg01/lvolnew
lvremove -f /dev/vg01/oravol
vgdisplay vg01 |grep 'Cur LV'
  Cur LV                0

# vgreduce vg01 /dev/sdb /dev/sdc1
vgremove vg01
pvremove /dev/sdb /dev/sdc1 /dev/sdd

dd if=/dev/zero of=/dev/sdc -->  to wipeout the disk data
pvck
pvcreate
pvdisplay
pvresize
pvmove
pvremvoe
pvs
pvscan
vgck
vgcreate
vgdisplay
vgextend
vgreduce
vgrename
vgremove
vgs
vgscan
lvcreate
lvdisplay
lvextend
lvreduce
lvremove
lvrename
lvresize
lvs
lvscan
lvm
lvmdiskscan

--filesystems ------
ext4 -> default on RHEL6
xfs -> default on RHEL 7
VFAT -> virtual file allocation table
dump2fs
e2fsck
e2label
mke2fs
resize2fs
tune2fs  -> tune file system attributes

mkfs.xfs
xfs_admin
xfs_growfs
xfs_info
xfs_repair

blkid ===>  list the file systems  with uuid 
df
du -h
du -hs
findmnt ->list mountedFS in tree form
fuser
wall  -> send message to all terminals
mount/umount
use the path,uuid or label to recognise filesystem
adds entry to /etc/mtab

mount options
ro/rw
auto
loop  for iso images

uuid mount , 
blkid  -> to get uuid of file system


parted /dev/sdb mklabel msdos
parted /dev/sdb print
parted /dev/sdb print |grep Table
parted /dev/sdb mkpart primary ext3 1 201m
parted /dev/sdb print
  mke2fs -t ext3  /dev/sdb1
pvcreate /dev/sdd  -v
vgcreate -s 16 -v  vg10 /dev/sdd
lvcreate -L 1.5g -n lvolext4 vg10 -v
mke2fs -t ext4 /dev/vg10/lvolext4
  mkdir -v /mntext3 /mntext4
mount /dev/vdb1 /mntext3
mount /dev/sdb1 /mntext3
mount /dev/vg10/lvolext4 /mntext4
df -h |grep mnt
tune2fs -l /dev/sdb1 |grep UUID
Filesystem UUID:          025b65bd-f19f-4991-9360-6eb07ed7f76f

vi  /etc/fstab
UUID=025b65bd-f19f-4991-9360-6eb07ed7f76f  /mntext3   ext3  defaults  1 2
/dev/vg10/lvolext4    /mntext4   ext4   defaults   1  2

parted /dev/sdb mkpart primary 202m 703m
parted /dev/sdb print
fdisk -l /dev/sdb
pvcreate /dev/sdb2
[root@centos ~]# pvcreate /dev/sdb2
  Physical volume "/dev/sdb2" successfully created
[root@centos ~]# vgextend vg10 /dev/sdb2
  Volume group "vg10" successfully extended
lvresize -r -L 2g /dev/vg10/lvolext4
lvs |grep lvolext4
df -h |grep mntext4
lvresize -r -L 1.1g /dev/vg10/lvolext4 --> reduce the file systemSize with LVsize
lvs |grep lvolext4
df -h |grep mntext4

Finnabar will write blog about how to make yum repo from the centeOS-ISO in hostsystem and without copying to client
I found a site with a few simple review material 
http://www.tecmint.com/rhcsa-exam-reviewing-essential-commands-system-documentation/

pvcreate /dev/sdc1
vgextend vg10 /dev/sdc1
lvcreate -L 172m  -n lvolxfs vg10 /dev/sdc1
mkfs.xfs /dev/vg10/lvolxfs
mkdir /mntxfs
mount /dev/vg10/lvolxfs  /mntxfs
df -h |grep mntxfs

vi /etc/fstab
/dev/vg10/lvolxfs     /mntxfs   xfs   defaults  1 2

lvresize -r  -L 300m /dev/vg10/lvolxfs
lvs |grep lvolxfs
df -h |grep mntxfs
xfs_info /mntxfs

--make vfat file system
 488  parted /dev/sde mklabel msdos
  489  parted /dev/sde print |grep -i partition
  490  parted /dev/sde mkpart primary fat32 1 401m
  491  pated /dev/sde print
  492  prated /dev/sde print
  493  parted /dev/sde print
mkfs.vfat /dev/sde1
mkdir /mntvfat
mount /dev/sde1  /mntvfat
df -h |grep mntvfat
# blkid /dev/sde1
/dev/sde1: SEC_TYPE="msdos" UUID="A6E1-C529" TYPE="vfat"

vi /etc/fstab
UUID=A6E1-C529     /mntvfat   vfat   defaults   1 2
mount -a

----
ghori 314
lab 10-5
parted  /dev/sdc mkpart primary 202 303m
parted  /dev/sdc mkpart primary 402 503m

mkfs


--repair  file systems
fuser -cu /filesystem -> show which user or prcess using this mountpoint
umount /dev/sdb1
e2fsck /dev/sdb1
e2fsck -v /dev/sdb1
dumpe2fs /dev/sdb1
# dumpe2fs /dev/sdb1 |grep superblock
dumpe2fs 1.42.9 (28-Dec-2013)
  Primary superblock at 1, Group descriptors at 2-2
  Backup superblock at 8193, Group descriptors at 8194-8194
  Backup superblock at 24577, Group descriptors at 24578-24578
  Backup superblock at 40961, Group descriptors at 40962-40962
  Backup superblock at 57345, Group descriptors at 57346-57346
  Backup superblock at 73729, Group descriptors at 73730-73730
fsck -b 24577 /dev/sdb1


=== NFS  ==========================
install  nfs-utils
yum -y isntall nfs-utils

mount -t nfs 192.168.0.110:/nfsdemo  /nfsmnt
vi /etc/fstab
192.168.0.110:/nfsdemo  /nfsmnt  nfs   _netdev   0  0
mount /nfsmnt

===swap ======================================
free
free -h

mkswap /dev/sdb2
swapon /dev/sdb2
swapon -s
cat /proc/swaps
swapof /dev/sdb2

mkswap /dev/vg10/swaplv
swapon -v /dev/vg10/swaplv   or (swapon -av /dev/vg10/swaplv)
swapoff  /dev/vg10/swaplv
lvremove /dev/vg10/swaplv

vmstat
vmstat -s


--acl--access  control list ---
acl  can set only on files/dir  under   filesystems only
mount -o remount,acl /dev/sdd1 /mnt
getfacl  /mnt
cd /mnt ; mkdir temp
cd temp ; touch file1
getfacl  file1
setfacl -m  u:soby:rw,m:r file1

touch file3
setfacl -m u:test1:7 file3
getfacl  file3
getfacl -c  file3
ll
-rw-rwxr--+ 1 root root     0 Jan 27 09:00 file3
setfacl  -m u:test2:rw file3
getfacl file3
# file: file3
# owner: root
# group: root
user::rw-
user:test1:rwx
user:test2:rw-
group::r--
mask::rwx
other::r--

setfacl -x u:test1  file3  -> delete acl  for test1
getfacl  file3
setfacl -b file3   ->  delete all the ACL entries
mkdir dir3
setfacl -m u:test1:7 dir3
getfacl dir3
setfacl -m d:u:test1:6,d:u:test2:7 dir3
getfacl -c dir3


-----27 jan 2017 -----------
===Chapter11 firewall ========================================================
Ghori book 348
intense   250

exs 11-1
iptables -F  -->  flush iptables
iptables -t filter -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p icmp -j DROP
iptables -A FORWARD -d 192.168.0.0/24 -j ACCEPT
iptables -I INPUT -m state --state NEW -p tcp --dport 21 -j ACCEPT
iptables -A OUTPUT -m state --state NEW,ESTABLISHED -p tcp --dport 25 -j DROP

yum list installed |grep iptables
yum install iptables-services
systemctl enable iptables
systemctl start iptables
systemctl status iptables
iptables-save  > /etc/sysconfig/iptables-config1

excis 11-2
iptables -I INPUT  -s 192.168.1.0/24 --dport 90 -j ACCEPT

--firewalld
to user firewall command need to turn off iptables
either iptables or firewall  can run
/usr/lib/firewalld
/usr/lib/firewalld/services --> contains  template files
/setc/firewalld
/etc/firewalld/services

exs 11-3
firewall-cmd --get-default-zone
firewall-cmd --permanent --add-service=http

firewall-cmd --reload
firewall-cmd --add-port=443/tcp
firewall-cmd --permanent --add-port=5901-5910/tcp; firewall-cmd --reload
firewall-cmd --list-services
firewall-cmd --list-ports
iptables -L -n
cat /etc/firewalld/zones/public.xml

firewall-cmd --permanent --remove-service=http
firewall-cmd --remove-port=443/tcp
firewall-cmd --list-ports
firewall-cmd --permanent --remove-port=5901-5910/tcp
firewall-cmd --permanent --add-port=5901-5902/tcp
firewall-cmd  --reload
firewall-cmd  --list-services
firewall-cmd  --list-ports
iptables -L
iptables -L -n
cat /etc/firewalld/zones/public.xml

--SElinux------
getenforce  ->check if SElinux on
  enforcing
cd /etc/selinux ; list   -> configuration files here
cat /etc/selinux/config

ps -eZ
ls -lZ
id -Z

sestatus
seinfo  -u
sesearch
sealert
semanage login -l

exs 11-5
useradd -Z staff_u  user5
echo user123 |passwd --stdin user5
semanage login -l |grep user5
id -Z
semanage login -a -s user_u user4
semanage login -l |grep user4

semanage login -m -S targeted -s staff_u -r s0 __default__
semanage  login -l |grep default

exs 11-6
touch /root/file1
ll -Z /root/file1
chcon -vu user_u -t public_content_t /root/file1

semanage fcontext -a -s user_u -t public_content_t /root/file1
ll -Z /root/file1
chcon -vu staff_u -t var_run_t  /root
ll -dZ /root

restorecon -vF /root
ll -dZ /root

/var/log/audit

--networking -------

hotnamectl set-hostname
ip addr
127.0.0.1/8   ->

cat /etc/sysconfig/network-scripts/ifcfg-eno16777736

/etc/hosts
ipaddress  fqdn  shortname

ifup/ifdown
ip     ->command replace  ifconfig
nmcli  -> command line tool for admin
nmtui   ->text based tools
nm-connection-editor ->graphical tool

systemctl status NetworkManager




---ntp-----
mout iso file from fstab
/path/to/file.iso  /path/to/folder  iso9660 loop 0 0
/var/tmp/CentOS-7-x86_64-Everything-1511.iso    /var/centos72   iso9660 loop 0 0

yum install ntp system-config-date
/etc/ntp.conf
systemctl
systemctl status stpd


--ldap--
yum install authconfig

[root@centos tmp]# locate authconfig-tui
/usr/sbin/authconfig-tui


--ssh & TCP wrapper-----

ntpq -pn
ntpdate

/etc/ssh/sshd_config   -> deamon / server configuration
/etc/ssh/ssh_config  ->  client configuration

yum list  |grep ssh

on Server1
sh - user2
ssh-keygen -t rsa   -> type rsa (default type)
ssh-keygen -t dsa  -> type dsa
[user2@centos .ssh]$ ls
id_dsa  id_dsa.pub  id_rsa  id_rsa.pub
id_rsa  -> private key
id_rsa.pub  -> public key

copy id_rsa.pub  file to server2 under /home/user2/.ssh to authorized_keys
ssh-copy-id  -i ~/.ssh/id_rsa.pub server2
cat ~/.ssh/known_hosts
ssh  server2
on server2
cat /var/log/secure  ->  see login attempts


tcp wrapper
man hosts_access
/etc/hosts.allow
/etc/hosts.deny

--virtualisation ----


ls /sys/hypervisor

in vm settings ->processors -> check virtualize  Intel VT

lscpu |grep -i virtualiz
cat /proc/cpuinfo |grep vmx   -->  intel cpu
cat /proc/cpuinfo |grep    -->  amd cpu

yum group info "virtualization hypervisor"
yum -y group install "virtualization hypervisor"
yum -y group install "virtualization client"
yum -y group install "virtualization platform"
yum -y group install "virtualization tools"

the  VM network  should be NAT

virt-manager


virsh -> to manage hypervisor and virtual machines

cert Guide
by
sander van vugt
certdepot.net
redhat jboss  developer  subscription ;  cheap  way to get redhat linux subscription

to install Graphics  on RHEL minimum install
yum group install "X Windows System" "GNOME" -y
systemctl set-default graphical.target



Swami Chettiar
631-979 1189
david stahura linkedin
Steven Carrato
Trey Tyler



