



====Reboot server ===================================
hostname --fqdn
echo OPSW_REBOOT 
#(or use  echo OPSW_FORCE_REBOOT )
echo  "after boot"
uptime ; date 
===copy / set up startup script links================================
cp -P /etc/rc.d/rc2.d/K01ego /etc/rc.d/rc3.d 
ls -l /etc/rc.d/rc3.d  |grep ego
cp /tmp/bob/ego /etc/rc.d/init.d 
chmod 755 /etc/rc.d/init.d/ego 
echo "after cp "
ls -al /etc/rc.d/init.d |grep ego
ln -s ../init.d/ego  /etc/rc.d/rc3.d/K01ego
ln -s ../init.d/ego  /etc/rc.d/rc3.d/S99ego
ls -al /etc/rc.d/rc3.d |grep ego

