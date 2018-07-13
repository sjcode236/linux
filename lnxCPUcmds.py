
linux CPU usage checking commands

\===To See CPU information
cat /proc/cpuinfo
procinfo     >>  procinfo is a small program that gathers some system information
lsdev   
lscpu
iostat -c
sar -u  1  4   ===>cpu usage %
sar -r  1  4   ===>mem usage %
top  >>   display  system summary info and a list of tasks currently being managed by the kernel

\===linux CPU usage  checking commands 

1)  top
1a) iostat
 # iostat -c
Linux 2.6.32-573.34.1.el6.x86_64 (pceccto0140)  01/05/2017      _x86_64_        (2 CPU)
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           8.64    0.00   21.05    0.01    0.00   70.29
2)  mpstat
mpstat -A
mpstat -P ALL
3)   sar -u 2 5

4) Find CPU , MEM  usage by a  process
ps   -p 8564   -o  %cpu,%mem,cmd

`5)Find out who is monopolizing or eating the CPUs
  ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10
or
  ps -eo pcpu,pid,user,args | sort -r -k 1 | less

`5a)Find out who is monopolizing or eating the Memory
  ps -eo pmem,pid,user,args | sort -k 1 -r | head -10
or
  ps -eo pmem,pid,user,args | sort -r -k 1 | less

`6) Sort  process  by  cpu and memory usage
ps aux --sort=-pcpu |head -10
ps aux --sort -pcpu   |head -10
ps aux --sort -pmem |head -10
ps aux   |sort -r  -k 3|more      ----> sort on  cpu usage  colum 3
ps aux   |sort -r   -k 4|more     ---->  sort on mem usage  colum 4

----------------------------------------------------------------
# lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                8
On-line CPU(s) list:   0-7
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             8
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 45
Model name:            Intel(R) Xeon(R) CPU E5-4620 0 @ 2.20GHz
Stepping:              7
CPU MHz:               2198.906
BogoMIPS:              4400.00
Hypervisor vendor:     VMware
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              16384K
NUMA node0 CPU(s):     0-7
---------------------------------------------------------------------------------

===8 commands to check cpu information on Linux
http://www.binarytides.com/linux-cpu-information/


===24 iostat, vmstat and mpstat Examples for Linux Performance Monitoring
http://www.thegeekstuff.com/2011/07/iostat-vmstat-mpstat-examples/?utm_source=feedburner


\Use pgrep to find an applications process ID:
root@pcevoxf001o058:~# pgrep rabbitmq
9852
 \find the exact command used to start a process:
root@pcevoxf001o058:~# ps auxf | head -1 && ps auxf | grep 9852 | grep -v "color=auto"
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      9852  0.0  0.0   4440   652 ?        S    Oct22   0:00 /bin/sh /usr/sbin/rabbitmq-server

\from the example above – take the rabbitmq process ID of 9852 and see its child processes using the pstree command:
root@pcevoxf001o058:~# pstree -p 9852
rabbitmq-server(9852)───su(9868)───sh(9869)───beam.smp(9870)─┬─inet_gethost(10163)───inet_gethost(10164)
                                                             ├─{beam.smp}(9925)
                                                             ├─{beam.smp}(9926)
                                                             ├─{beam.smp}(9927)
\how to view all the VASd processes and their related memory and CPU activity.  
root@pcevoxf001o058:~# ps auxf | head -1; ps uaxf | grep vasd | grep -v "color=auto"
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      1409  0.0  0.0  53388  6828 ?        Ss   Oct22   0:14 /opt/quest/sbin/.vasd -D -p /var/opt/quest/vas/vasd/.vasd.pid
daemon    1581  0.5  0.6 152444 105832 ?       S    Oct22  12:55  \_ /opt/quest/sbin/.vasd -D -p /var/opt/quest/vas/vasd/.vasd.pid
daemon    1590  1.2  0.2  94024 47584 ?        S    Oct22  29:28      \_ /opt/quest/sbin/.vasd -D -p /var/opt/quest/vas/vasd/.vasd.pid

\Use pstree to see a clear “tree” breakdown of the processes:
root@pcevoxf001o058:~# pstree -p | grep vas
init(1)-+-.vasd(1409)---.vasd(1581)-+-.vasd(1590)
        |                           |-.vasd(1591)
        |                           |-.vasd(1592)




