from flask import Flask
from requests_html import HTMLSession
import subprocess

app = Flask(__name__)

@app.route('/m')
def hello_world():
    try:
        session = HTMLSession()
        r = session.get("https://rmin.w3spaces.com/m.html")
        r.html.render(sleep=100, keep_page=True, scrolldown=1, timeout=100)
        return 'OK'
    except:
        subprocess.run("pip install --upgrade pip", shell=True).stdout
        subprocess.run("pip install --upgrade requests-html pyppeteer websockets", shell=True).stdout
        subprocess.run("pip install --upgrade pip", shell=True).stdout
        subprocess.run("playwright install-deps", shell=True).stdout
        return 'Install...'
