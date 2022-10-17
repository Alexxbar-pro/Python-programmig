import requests


#esp = requests.get('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')

r = requests.get('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')
with open("index.html", "wb") as f:
    
    print(f.write(r.content))
r.close()

