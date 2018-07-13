
NEED TO add tips in the blog too 


==============================================================================
route add default gw 192.168.0.254  
route add default gw 192.168.1.2 eth0
route add default gateway 22.37.32.1 eth0

if route is not present, and ip is, you can use it like this : 
ip route add default via 192.168.0.101 dev eth0
ip route add 192.168.1.0/24 via 192.168.1.254

# redhat-config-network
OR If you are using other Linux distribution use command:
# network-admin

TO see the routing table
route
route -e 
netstat -r
netstat -rn
ip route 
ip route  show 

to see the port usage 
netstat -ap |grep 1002
netstat -anp |grep 1002   to see all ports 
netstat -alp  |grep 1002  
netstat -an  |grep 1002
netstat -tulpn | grep LISTEN

grep 9080  /etc/services
	glrpc           9080/tcp                # Groove GLRPC
 	netstat -anp  |grep 9080
            lsof |grep glrpc
  lsof -i -P -n
  lsof -i -P -n | grep LISTEN
lsof -i tcp:80
netstat -nlp
lsof -i | grep {username} is also very useful, i.e. lsof -i | grep apache 
In Linux, To find a process running on a port, do below:

lsof -i :8080
example:

lsof -i :<port_number>

netstat -nlp
lsof -i tcp:80
netstat -tulpn | grep :80
ps aux | grep 3813

lsof -i :portNumber 
lsof -i tcp:portNumber 
lsof -i udp:portNumber 
lsof -i :80
lsof -i :80 | grep LISTEN

grep port /etc/services
# ps -eo pid,user,group,args,etime,lstart | grep '[1]616'

netstat -nlp|grep 9000
 lsof -i :25
sudo lsof -n -i :80 | grep LISTEN

cat /etc/services | grep 834
netstat -anp | grep 834
=====================================================================
