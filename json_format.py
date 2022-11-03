# https://10.0.2.30/mdclone-api/api/v1/system-check
import requests # pip install requests
import os
import json
import datetime
import urllib3

start = datetime.datetime.now()
urllib3.disable_warnings()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
timestamp = datetime.datetime.now().strftime('%m-%d-%Y %H-%M-%S')
file_name = os.environ.get('FILE_NAME')
ip_server = os.environ['MY_IP_JSON']
url = "http://" + ip_server + "/mdclone-api/api/v1/system-check"
session = requests.session()
session.auth = ('mdclone.admin', 'Mmm@24680')
session.headers.update(headers)
response = session.get(url, verify=False)
html_page = response.content.decode('latin1')
json_data = json.loads(html_page)
with open('/usr/app/src/' + file_name + "_" + timestamp + ".txt", "w") as file:
    file.write(json.dumps(json_data, indent=4))
end = datetime.datetime.now()
print("total runtime: " + str(end - start))

# docker build . -t test -f Dockerfile.dockerfile
# docker run -v $PWD/:/usr/app/src/ -e FILE_NAME=logfilename -e MY_IP_SERVER=10.0.2.30 test