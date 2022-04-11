import requests
import sys

subd_list = open("subdomains-1000.txt").read()
subs = subd_list.splitlines()

for sub in subs:
    url_to_check =  f"http://{sub}.{sys.argv[1]}"


    try: 
        requests.get(url_to_check)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain",url_to_check)