---------------------------------------------
TO remove  orphan volumes from cinder (vmware Datastore  Lun)
#! /bin/bash 

LIST="/tmp/serverlist"
RESULTS="/tmp/results"
ORPHS="/tmp/orphans"
SIZE="/tmp/size"
ALL="/tmp/all_orphans"

### source OpenStack creds ###
. /home/stack/service.osrc

### Gather all volume UUIDs ###
cinder list --all-tenants | awk '{print $2}' | grep -v ID > ${LIST}

### Determine which Volumes are not attached to an instance ###
for i in `more ${LIST}`
do
  cinder show $i | grep server_id
  if [ $? = 0 ]; then
  echo "$i is good to go" >> ${RESULTS}
  else
  echo "$i is an orphan UUID" >> ${RESULTS}
  fi
done  2> /dev/null> report 2>&1

### Seperate the Orphaned volumes from known active volumes###
grep orphan ${RESULTS} | awk '{print $1}' >> ${ORPHS}

### Determine the size of each orphaned volume. ###
for i in `more ${ORPHS}`
do
  cinder show $i | grep size | awk '{print $2, $4}' >> ${SIZE}
  paste ${ORPHS} ${SIZE} | pr -t -e20 > ${ALL}
  echo "Total orphaned space in GB: `more ${ALL} | awk '{print $3}' | paste -sd+ | bc`" >> ${ALL}
done 2> /dev/null> report 2>&1

###Deleting orphaned files###
#for i in `more ${ORPHS}`
#do
#  cinder delete $i
#done 2> /dev/null> report 2>&1


rm ${RESULTS} ${ORPHS} ${SIZE} reports \
----------------------------------------------------------------------------------
