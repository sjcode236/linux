








https://github.com/sjcode236/toRef/blob/master/misc/prar.md







===ssh and run command =========================================================
csvra89a0104
csvra90a0104
csvra91a0104
csvra92a0104
for serv in `cat servlist`     
do
ssh $serv 'uname -a  && rpm -qa |grep -i "commons-collections"   ' >> output
done
ssh cuvra91a0091 'uname -a  && rpm -qa |grep -i "grub2-common"   ' >> output
