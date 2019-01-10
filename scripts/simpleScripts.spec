
















===ssh and run command =========================================================
host1
host3
host2
host4
for serv in `cat servlist`     
do
ssh $serv 'uname -a  && rpm -qa |grep -i "commons-collections"   ' >> output
done
ssh cuvra91a0091 'uname -a  && rpm -qa |grep -i "grub2-common"   ' >> output
======================================================================

