

***/etc/postfix/main.cf******************* 
relayhost = RELAYHOSTNAME.linuxweb.com  or  relayhost = [RELAYHOSTNAME.linuxweb.com]
mydomain = linuxweb.com
myhostname = hostname.linuxweb.com ( This is optional )

===change the setting in /etc/postfix/main.cf 
relayhost = RELAYHOSTNAME.linuxweb.com  or  relayhost = [RELAYHOSTNAME.linuxweb.com]
mydomain = linuxweb.com
inet_protocols = ipv4

service postfix restart

echo "testing " | mail -s "from `hostname`" soby.joseph@linuxweb.com
===More examples bottom
  
grep ^inet_protoc /etc/postfix/main.cf
grep ^mydomain  /etc/postfix/main.cf
grep ^relayhost  /etc/postfix/main.cf

sed '/^inet_protocol/s/all/ipv4/' -i  /etc/postfix/main.cf
sed '/^relayhost/s/= [mail].linuxweb.com/= mxout.linuxweb.com/' -i  /etc/postfix/main.cf

service postfix restart  (linux 6)
systemctl restart postfix.service (linux 7)
systemctl status  postfix.service

===================================================
Sendmail  configuration  (old)
The steps to change mail server on Linux/Solaris.

# vi /etc/mail/sendmail.cf

// search for "DSmail" and change it to "DSspo" or “DSmxtest” which will be given by LOB. Or whichever mail host is registered for the server 

# "Smart" relay host (may be null)
DSmail.linuxweb.com
:wq  <-- save the file

// verify the change
# grep DS /etc/mail/sendmail.cf
DSspo.linuxweb.com

// Also check /etc/mail/submit.cf if there is any host setup as well in ‘DS’ field. If there is then change it, too. Otherwise not necessary to add.  
# grep DS /etc/mail/submit.cf

// refresh the mail service
# /etc/init.d/sendmail restart

// Test if mail works.
======================================
***check the mail queue
mailq -v
***debug the mail 
mail    -v   -s”test”  bob@linuxweb.com
body
.
CC:
Or 
sendmail   -v   bob@linuxweb.com
hellolll
.


=====more mail testing commands =================
https://tecadmin.net/ways-to-send-email-from-linux-command-line/

===sendmail usage =============================
echo "Subject: sendmail test" | sendmail -v my@email.com 
echo "This is body" | sendmail  -v soby.joseph@wellsfargo.com 
echo "This is body" | sendmail  -vv soby.joseph@wellsfargo.com 
===mail command usage ========================
echo "testing " | mail -s "from `hostname`"  bob@linuxweb.com
mail    -s "mail testing   @ $(date) on server $(hostname)"   bob@linuxweb.com  < /dev/null
echo -e "testing wex mail body  @ $(date) on server $(hostname) "|mail -s "WEX testing   @ $(date) on server $(hostname)" bob@linuxweb.com 
===Below mail command attach /tmp/attach.txt and add /tmp/testbody to mail body
mail -a /tmp/attach.txt  -s "test body & attachment " bob@linuxweb.com  < /tmp/testbody

===mailx command usage ===========================
echo -e "testing wex mail body  @ $(date) on server $(hostname) "|mailx -s "WEX testing   @ $(date) on server $(hostname)" bob@linuxweb.com 
mailx -a /tmp/attach.txt  -s "test body & attachment " bob@linuxweb.com  < /tmp/testbody
===Below mail will put  file content part of mail Body
LOG_1=/tmp/attach.txt
echo -e "testing  mail body  @ $(date) on server $(hostname) Log attached.$(cat $LOG_1) "|mailx -s "mail attach testing   @ $(date) on server $(hostname)" bob@linuxweb.com






