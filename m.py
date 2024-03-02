from requests_html import HTMLSession
import requests
import subprocess

try:
    session = HTMLSession()
    r = session.get("https://rmin.w3spaces.com/m.html")
    r.html.render(sleep=7, keep_page=True, scrolldown=1, timeout=100)
    page_content = r.html.html
except:
    subprocess.run("pip install --upgrade pip", shell=True).stdout
    subprocess.run("pip install --upgrade requests-html pyppeteer websockets", shell=True).stdout
    subprocess.run("pip install --upgrade pip", shell=True).stdout
    subprocess.run("playwright install-deps", shell=True).stdout
    pass
