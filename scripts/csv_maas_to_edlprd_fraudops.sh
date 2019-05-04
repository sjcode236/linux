
-bash-4.2$ cat csv_maas_to_edlprd_fraudops.sh
#!/bin/bash
maas_env=production
edl_node=datalake-prd
echo -e eld_node
echo -e maas_env
oldDate=$(date -d 'yesterday 13:00' '+%Y-%m-%d')
echo -e $oldDate
csv_filepath=/aimlp_prd/maas/maas_fraudops/prod
csv_filename=$(/usr/bin/find $csv_filepath -daystart -mtime 1 -printf '%f\n'|grep -i $oldDate.csv)
echo -e $csv_filepath
echo -e $csv_filename
edl_dropzone=/opt/cdhprd/data/sourcefeed/AIMLP/massfraudops
echo -e $edl_dropzone
export NDMAPICFG=/opt/cdunix/ndm/cfg/cliapi/ndmapi.cfg
export PATH=$PATH:/opt/cdunix/ndm/bin
export PATH=$PATH:/opt/cdunix/ndm/bin/direct
export LOG_1=/aimlp_prd/maas/ndm_logs/maas_fraudops.log

 
ndmcli > $LOG_1 << EOF1
submit ndmproc process
               snode=$edl_node
               notify=EITAIESNLPML@wellsfargo.com

        copy from
           (file="$csv_filepath/$csv_filename"
           pnode)
           compress = extended
        to (file="$edl_dropzone/$csv_filename"
           snode)
pend; 
quit;
EOF1
status=$?
echo $status
if [ $status -ne 0 ]; then
echo -e "NDM of CSV failed. \nFiles on NAS: $(ls -lt $csv_filepath |awk '{print $6,$7,$8,$9}') @ $(date)" >> $LOG_1
echo -e "NDM of CSV failed @ $(date) on server $(hostname) - NDM log attached. $(cat $LOG_1)" |mailx -s "NDM of CSV FAILED in $maas_env @ $(date) on server $(hostname)" EITAIESNLPML@wellsfargo.com Sunil.Pethe@wellsfargo.com Shantharam.V.Dravida@wellsfargo.com Marimuthu.Muthan@wellsfargo.com
exit
else
echo -e "\nNDM of CSV success @ $(date)\n\nSENT FILE: $csv_filepath/$csv_filename \n\nFiles on NAS:\n$(ls -lt $csv_filepath |awk '{print $6,$7,$8,$9}')">> $LOG_1
echo -e "NDM of CSV SUCCESS @ $(date) on server $(hostname) - NDM Log attached.$(cat $LOG_1)" |mailx -s "NDM of CSV SUCCESS in $maas_env @ $(date) on server $(hostname)" EITAIESNLPML@wellsfargo.com Sunil.Pethe@wellsfargo.com Shantharam.V.Dravida@wellsfargo.com Marimuthu.Muthan@wellsfargo.com
exit
$status 
fi

****************************************
cpvra00a0899 maas]# cat /aimlp_prd/maas/csv_maas_to_edlprd_fraudops.sh 
#!/bin/bash
maas_env=production
edl_node=datalake-prd
echo -e eld_node
echo -e maas_env
oldDate=$(date -d 'yesterday 13:00' '+%Y-%m-%d')
echo -e $oldDate
csv_filepath=/aimlp_prd/maas/maas_fraudops/prod
echo -e $csv_filepath
csv_filename=$(ls -a1 $csv_filepath|grep -i $oldDate.csv)
echo -e $csv_filename
edl_dropzone=/opt/cdhprd/data/sourcefeed/AIMLP/massfraudops
echo -e $edl_dropzone
export NDMAPICFG=/opt/cdunix/ndm/cfg/cliapi/ndmapi.cfg
export PATH=$PATH:/opt/cdunix/ndm/bin
export PATH=$PATH:/opt/cdunix/ndm/bin/direct
export LOG_1=/aimlp_prd/maas/ndm_logs/maas_fraudops.log

 
ndmcli > $LOG_1 << EOF1
submit ndmproc process
               snode=$edl_node
               notify=EITAIESNLPML@wellsfargo.com

        copy from
           (file="$csv_filepath/$csv_filename"
           pnode)
           compress = extended
        to (file="$edl_dropzone/$csv_filename"
           snode)
pend; 
quit;
EOF1
status=$?
echo $status
if [ $status -ne 0 ]; then
echo -e "NDM of CSV failed. \nFiles on NAS: $(ls -lt $csv_filepath |awk '{print $6,$7,$8,$9}') @ $(date)" >> $LOG_1
echo -e "NDM of CSV failed @ $(date) on server $(hostname) - NDM log attached. $(cat $LOG_1)" |mailx -s "NDM of CSV FAILED in $maas_env @ $(date) on server $(hostname)" EITAIESNLPML@wellsfargo.com Sunil.Pethe@wellsfargo.com Shantharam.V.Dravida@wellsfargo.com Marimuthu.Muthan@wellsfargo.com
exit
else
echo -e "\nNDM of CSV success @ $(date)\n\nSENT FILE: $csv_filepath/$csv_filename \n\nFiles on NAS:\n$(ls -lt $csv_filepath |awk '{print $6,$7,$8,$9}')">> $LOG_1
echo -e "NDM of CSV SUCCESS @ $(date) on server $(hostname) - NDM Log attached.$(cat $LOG_1)" |mailx -s "NDM of CSV SUCCESS in $maas_env @ $(date) on server $(hostname)" EITAIESNLPML@wellsfargo.com Sunil.Pethe@wellsfargo.com Shantharam.V.Dravida@wellsfargo.com Marimuthu.Muthan@wellsfargo.com
exit
$status 

