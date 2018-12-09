from json import load
from sys import exit
import argparse,getpass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

with open(r"urls.json") as f:
    urls = load(f)
f = None

options = Options()
options.headless = False

parser = argparse.ArgumentParser()
parser.add_argument("url", type=str, help="expects custom codes of sites", choices=[x for x in urls.keys()])
parser.add_argument("username", type=str, help="expects your username")
parser.add_argument("-p", "--private", action="store_true", help="browse inprivate")
args = parser.parse_args()

uname = args.username
passw = getpass.getpass("password? ")

if args.private :
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
else:
    driver = webdriver.Firefox()
print("Opening Browser...")

print("Redirecting to requested URL...")
url = urls[args.url]
try :
    driver.get(url["url"])
except :
    driver.switch_to_default_content()

print("Filling in credentials...")
driver.find_element_by_name(url["name1"]).send_keys(uname)
driver.find_element_by_name(url["name2"]).send_keys(passw)
driver.find_element_by_name(url["name3"]).click()
print("Logged In!")
print("\n(Please sign out before ending session)")
input("\nPress any key to end session.")
driver.quit()
exit()
