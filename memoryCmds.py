
http://linux236.blogspot.com/2016/07/linux-memory-commands.html
  
\Linux memory commands
free  -m
vmstat  1

1a)  Find CPU , MEM  usage by a  process
ps   -p 8564   -o  %cpu,%mem,cmd

\Find out who is monopolizing or eating the CPUs
  ps -eo pcpu,pmem,pid,user,args | sort -k 1 -r | head -10
or
  ps -eo pcpu,pmem,pid,user,args | sort -r -k 1 | less

\Find out who is monopolizing or eating the Memory
  ps -eo pmem,pcpu,pid,user,args | sort -k 1 -r | head -10
or
  ps -eo pmem,pcpu,pid,user,args | sort -r -k 1 | less

ps aux   |sort -r  -k 3|more      ==> sort on  cpu usage  colum 3
ps aux   |sort -r   -k 4|more     ->  sort on mem usage  colum 4

ps aux | awk '{print $6/1024 "  "  $11}' | sort -n

5  common commands
1)free -m
free -t
2)top
3)cat /proc/meminfo
4)vmstat 1
 vmstat 1  3
procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  1 4903264 255048  36276 892204   58   45    78    61   60   33  3  1 96  0  0
 0  0 4903264 255040  36280 892204    0    0     0     1  248  402  1  1 99  0  0
 0  0 4903264 255040  36280 892204    0    0     0     0  309  442  1  1 99  0  0

5)dmidecode -t 17 |more
# dmidecode 2.12
SMBIOS 2.4 present.

Handle 0x00E3, DMI type 17, 27 bytes
Memory Device
        Array Handle: 0x00E2
        Error Information Handle: No Error
        Total Width: 32 bits
        Data Width: 32 bits
        Size: 8192 MB
        Form Factor: DIMM
        Set: None
        Locator: RAM slot #0
        Bank Locator: RAM slot #0
        Type: DRAM
        Type Detail: EDO
        Speed: Unknown
        Manufacturer: Not Specified
        Serial Number: Not Specified
        Asset Tag: Not Specified


        Part Number: Not Specified

To find swap information
cat /proc/swaps   ==>  will show info on each swap partition.
swapon -s       ==>   shows swap partitions and info
swapon -a       >>    makes all swap partitions available as indicated in /etc/fstab.
cat /proc/sys/vm/pagecache

To see the process use the swap memory most
Run top then press 'O' (capital letter o) followed by 'p' then 'enter'. Now processes should be sorted by their swap usage.

To see  the swap usage details 
free -m
vmstat 1
vmstat 1  5
>>You need to check the swap column where si means “swap in”, and so means “swap out.” If the numbers are high, it means a lot of swapping activity which is an indicator of low memory issues. If you see swap usage by free but little active swapping, tweaking swappiness might be due.

`What is your swappiness set to? 
cat /proc/sys/vm/swappiness
sysctl -a |grep  swappiness
--Lowering swappiness to “10” is often advised 
sysctl vm.swappiness=10
sysctl -w vm.swappiness=10
echo 10 > /proc/sys/vm/swappiness
--you can permanently change the system configuration by editing 
“/etc/sysctl.conf”
#Set swappiness value
vm.swappiness=10

/sbin/sysctl  -p 
sysctl -a  or sysctl -A

--You can run swapoff -a as root to swap all memory back in. Don't forget to run swapon -a afterwards to make swap available again. Note that swapoff will fail if there is not enough physical memory available to swap everything back in.

\drop_caches  (Freeing page cache)
Writing to this will cause the kernel to drop clean caches, dentries and
inodes from memory, causing that memory to become free.
To free pagecache:
    echo 1 > /proc/sys/vm/drop_caches
To free dentries and inodes:
    echo 2 > /proc/sys/vm/drop_caches
To free pagecache, dentries and inodes:
    echo 3 > /proc/sys/vm/drop_caches

egs:-    
 free -m  && sync && echo 3 > /proc/sys/vm/drop_caches && free -m
echo 3 | sudo tee /proc/sys/vm/drop_caches
# free -m
              total        used        free      shared  buff/cache   available
Mem:          15791       10619        4383          88         788        4746

Swap:          4095        2917        1178

\Topas  usage
top -c /  top c     ==>  list the process with commands 
iostat -x 10  100

\lsof 
lsof -p  25385      ==>  show all the files open by that process 
lsof |grep grid
lsof -i :1002   ==> show the port status of 1002
