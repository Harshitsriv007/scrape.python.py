#created by harshit*/
from urllib import request
import re

# open a web page and scrape everything off
with request.urlopen("http://python.org") as response:
    response_data = response.read()

# isolate and print everything between paragraph tags
paragraphs = re.findall(
    r"<p>(.*?)</p>",
    str(response_data)
    )

for content in paragraphs:
    print(content)

# credit to sentdex (https://pythonprogramming.net/parse-website-using-regular-expressions-urllib/)
