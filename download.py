import argparse
import sys
import re
from urllib import request

parser = argparse.ArgumentParser(description="Help download google drive file without viruse scan.(Public File)")
parser.add_argument("-id", "-i", help="input file id.", type=str, default="")
parser.add_argument("-small", "-s", help="the file is too small that google can scan viruse(Maybe<25MB).", action="store_true")
args = parser.parse_args()
if args.id=="":
    print("No ID provide.")
    sys.exit(0)
######################################################################################
"""
Regex:
    find file name: <span class="uc-name-size"><a href="[^"]+">(?<name>.+?)<\/a>
    find url token: <form id="download-form" action="[^"]+confirm=(?<token>[^"])&[^"]+" method="post">
"""
######################################################################################

def url_decoder(b):
# From → https://github.com/wayne931121/Python_URL_Decode
# https://zh.wikipedia.org/zh-tw/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81
# %21 mean 21hex, => int("21",16) => 33 => chr(33) => "!", result: "!"
    if type(b)==bytes:
        b = b.decode("utf-8") #byte can't insert utf8 charater
    result = bytearray()
    enter_hex_unicode_mode = 0
    hex_tmp = ""
    now_index = 0
    for i in b:
        if i=='%': #like %51%52, have entered mode, continue appending bytearray
            enter_hex_unicode_mode = 1
            continue
        if enter_hex_unicode_mode:
            hex_tmp += i
            now_index += 1
            if now_index==2: #%51%5F len("51")=2 len("5F")=2
                result.append(int(hex_tmp, 16) )
                hex_tmp = ""
                now_index = 0
                enter_hex_unicode_mode = 0
            continue
        result.append(ord(i))
    result = result.decode(encoding="utf-8")
    return result

url = "https://drive.google.com/uc?id={}&export=download".format(args.id)
if not args.small:
   response = request.urlopen(request.Request(url)).read().decode(encoding="utf-8")
   token = re.search('<form id="download-form" action="[^"]+confirm=(?P<token>[^"])&[^"]+" method="post">', response)["token"]
   #filename = re.search('<span class="uc-name-size"><a href="[^"]+">(?P<name>.+?)<\\/a>', response)["name"]
   DownloadURL = url+"&confirm="+token
   method = "POST"
else:
   DownloadURL = url
   method = "GET"
print(DownloadURL)
content = request.urlopen(request.Request(DownloadURL, method=method))
info = content.info()
print(info)
content_length = int(info["Content-Length"]) #Byte
filename = url_decoder(info["Content-Disposition"].split("filename*=UTF-8''")[1])
file = open(filename, "wb")
buffer = 1*1024*1024 #Buffer:1MB → 1*1024*1024 Byte
length = content_length
printf = lambda: print("\r"+"%3d"%(int((1-length/content_length)*100))+"%", end='', flush=True)
print("Downloading...")
printf()
while 1:
   if length>=buffer:
       chunk_size = buffer
       length -= buffer
   else:
       chunk_size = length
   chunk = content.read(chunk_size)
   file.write(chunk)
   if chunk_size==length: break
   printf()
length = 0
printf()
file.close()
