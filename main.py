# http://10.0.2.42:999/system_check
# https://10.0.2.66/mdclone-api/api/v1/system-check
# http://10.0.2.42:999/system_check
# http://10.0.2.53:999/system_check
import requests # pip install requests
import re
import os
import datetime

file_name = os.environ.get('FILE_NAME')
ip_server = os.environ['MY_IP_SERVER']
with open(os.getcwd() + '\\' + file_name + ".txt", "w+") as file:
    url = "http://" + ip_server + ":999/system_check"
    services = requests.get(url)
    strings = re.findall('<h1 style="color:[A-Za-z ]+">[A-Za-z ]+:</h1>' ,services.text)
    for string in strings:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        micro_service = re.search('>[A-Za-z ]+:<' ,string).group(0)[1:-2]
        if "lightgreen" in string:
            file.write(str(date) + "," + micro_service + ",Online\n")
        else:
            file.write(str(date) + "," + micro_service + ",Offline\n")
    file.write("---------------------------------------------------------------------\n")

# docker build . -t test -f Dockerfile.dockerfile
# docker run -e FILE_NAME=logfilename -e MY_IP_SERVER=10.0.2.42 test