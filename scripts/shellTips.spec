


====bash change string to array 
$  myline='this is new string'
$ myarr=($myline)
$  echo -e " ${myarr[0]} , ${myarr[1]} , ${myarr[2]} , ${myarr[3]} "
 this , is , new , string 
OR 
$  myarr=(this is an array) 
$ echo -e " ${myarr[0]} , ${myarr[1]} , ${myarr[2]} , ${myarr[3]} "
 this , is , an , array 
OR
myarr=('item1' 'item2' 'item3')
===============================================
