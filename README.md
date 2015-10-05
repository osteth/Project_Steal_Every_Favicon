# Getips.py
This is a small python script that will echo out every possible IPV4 address. 
To generate a text file with every address in it, pipe the output in to a text file. 
This will take ~9hours to complete and the file will be 16.1GB (tested on an I7 laptop with 16GB ram, time to generate will differ with other specs.)

# Getfavicons.py
a variation of getips.py that formats the output to generate a list for collecting a favicon from every IPv4 address should there be on in the root directory.
This will not get every favicon in the internet because many sites are hosted on the same IP address. However it is a pretty fun thing to test out.

#top-1m.cvs
a list of the top 1million websites on the internet (based on most accessed) pulled from Nmap.org

#top-1m-url-0nly.csv
list of the top 1million websites scrubbed for urls only 

To download every favicon from these sites us the collowing command

#getfavicon.sh
a script used to pull the favicons from the top-1m-url-only.svc file. this will wget the favicon and rename it to the sites url so files do not conflict. 

cat top-1m-url-only.csv | xargs -n 1 -P 8 ./getfavicon.sh

run this command to execute the download.