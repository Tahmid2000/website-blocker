import datetime
import time
hosts_path = '/etc/hosts'
redirect = '127.0.0.1'
weblist = ['www.instagram.com', 'www.facebook.com']

while True:
    x = datetime.datetime.now().hour
    if 14 < x < 22:
        with open(hosts_path, 'r+') as hosts:
            content = hosts.read()
            for website in weblist:
                if website not in content:
                    hosts.write("\n" + redirect + " " + website)
                else:
                    pass
    else:
        with open(hosts_path, 'r+') as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(web in line for web in weblist):
                    hosts.write(line)
            hosts.truncate()
    time.sleep(5)
