import urllib.request
urllib.request.urlopen("https://api.moderatecontent.com/moderate/?url=http://www.moderatecontent.com/img/logo.png&key=<your_free_api_key_from_moderatecontent.com>").read()
