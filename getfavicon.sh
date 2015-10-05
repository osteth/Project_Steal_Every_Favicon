#!/bin/sh


url="http://$1/favicon.ico";
filename="$1.ico";
#echo -n $url; echo -n "  |  ";  echo $filename;

wget -O $filename --tries=1 $url
