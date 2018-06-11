
`Linux memory commands
free  -m
vmstat  1

1a)  Find CPU , MEM  usage by a  process
ps   -p 8564   -o  %cpu,%mem,cmd

Find out who is monopolizing or eating the CPUs
  ps -eo pcpu,pmem,pid,user,args | sort -k 1 -r | head -10
or
  ps -eo pcpu,pmem,pid,user,args | sort -r -k 1 | less

Find out who is monopolizing or eating the Memory
  ps -eo pmem,pcpu,pid,user,args | sort -k 1 -r | head -10
or
  ps -eo pmem,pcpu,pid,user,args | sort -r -k 1 | less

ps aux   |sort -r  -k 3|more      ----> sort on  cpu usage  colum 3
ps aux   |sort -r   -k 4|more     ---->  sort on mem usage  colum 4

ps aux | awk '{print $6/1024 "  "  $11}' | sort -n
