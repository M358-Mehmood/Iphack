#coded by mehmood (noob hackers)

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (f""" \033[1;96m[V™]

\033[1;97m d8888. db   db  .d8b.  d888888b db   dD db   db 
88'  YP 88   88 d8' `8b   `88'   88 ,8P' 88   88 
`8bo.   88ooo88 88ooo88    88    88,8P   88ooo88 
  `Y8b. 88~~~88 88~~~88    88    88`8b   88~~~88 
db   8D 88   88 88   88   .88.   88 `88. 88   88 
`8888Y' YP   YP YP   YP Y888888P YP   YD YP   YP 
              \033[0;97m
                                                      v 1.0
"""+red)
print (lgreen+bold+"         <===[[ coded by Mehmood ]]===> \n"+clear)
print (yellow+bold+"   <---(( Noob hack Mehmood ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[City]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
