



systemctl status network.service
systemctl restart network.service

======================================================================
$0 => The name of the Bash script.
$1 =>  $9 - The first 9 arguments to the Bash script. (As mentioned above.)
$# => How many arguments were passed to the Bash script.
$@ => All the arguments supplied to the Bash script.
$? => The exit status of the most recently run process.
$$ => The process ID of the current script.
$USER => The username of the user running the script.
$HOSTNAME => The hostname of the machine the script is running on.
$SECONDS => The number of seconds since the script was started.
$RANDOM => Returns a different random number each time is it referred to.
$LINENO => Returns the current line number in the Bash script.

$0, $1, $2, etc. =>  Positional parameters, passed from command line to script, passed to a function
$# => Number of command-line arguments or positional parameters 
$* => All of the positional parameters, seen as a single word
	"$*" must be quoted. ; echo "$*"
$@ => Same as $*, is an array-like construct of all positional parameters, {$1, $2, $3 ...}.
	echo "$*"
$-  => Flags passed to script / current options set for the shell.	
$_  =>  most recent parameter (or the abs path of the command to start the current shell immediately after startup).
$!  => PID (process ID) of last job run in background
$? => The exit status of the most recently run process.
	echo $i
$$ => Process ID (PID) of the script itself. 
	echo $$
$IFS => is the (input) field separator.	
==========================================================================================


