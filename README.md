# download_googledrive_file
Download file from google drive, support large file, we can bypass viruse scan.

```cmd
PS C:\Users\Desktop> python download.py -h
usage: download.py [-h] [-id ID] [-small]

Help download google drive file without viruse scan.(Public File)

optional arguments:
  -h, --help     show this help message and exit
  -id ID, -i ID  input file id.
  -small, -s     the file is too small that google can scan viruse(Maybe<25MB).
```
Use:
```cmd
python download.py -id your_file_id
```
Download Small File:
```cmd
python download.py -id your_file_id -small
```
Colab:
```cmd
!git clone https://github.com/wayne931121/download_googledrive_file.git
!mv download_googledrive_file/download.py download.py
%run download.py -id your_file_id
```
```cmd
Input:
!git clone https://github.com/wayne931121/download_googledrive_file.git
!mv download_googledrive_file/download.py download.py
%run download.py -id 11jGcJIdbR1MNtRct5DOR5Uk0aoICoXRl

Output:
Cloning into 'download_googledrive_file'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 2.62 KiB | 1.31 MiB/s, done.
https://drive.google.com/uc?id=11jGcJIdbR1MNtRct5DOR5Uk0aoICoXRl&export=download&confirm=t
X-GUploader-UploadID: ADPycds1XpxxwNSqhEzDtsmoX3nAL3RKp1kj5EZPLQcrhP5xZIK6WCr7FeASXvAU7qF0EgZC-VpBxPr2Z8VedQzTxap3zA
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="variables.data-00000-of-00001"; filename*=UTF-8''variables.data-00000-of-00001
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: false
Access-Control-Allow-Headers: Accept, Accept-Language, Authorization, Cache-Control, Content-Disposition, Content-Encoding, Content-Language, Content-Length, Content-MD5, Content-Range, Content-Type, Date, developer-token, financial-institution-id, X-Goog-Sn-Metadata, X-Goog-Sn-PatientId, GData-Version, google-cloud-resource-prefix, linked-customer-id, login-customer-id, x-goog-request-params, Host, If-Match, If-Modified-Since, If-None-Match, If-Unmodified-Since, Origin, OriginToken, Pragma, Range, request-id, Slug, Transfer-Encoding, hotrod-board-name, hotrod-chrome-cpu-model, hotrod-chrome-processors, Want-Digest, X-Ad-Manager-Impersonation, x-chrome-connected, X-ClientDetails, X-Client-Version, X-Firebase-Locale, X-Goog-Firebase-Installations-Auth, X-Firebase-Client, X-Firebase-Client-Log-Type, X-Firebase-GMPID, X-Firebase-Auth-Token, X-Firebase-AppCheck, X-Firebase-Token, X-Goog-Drive-Client-Version, X-Goog-Drive-Resource-Keys, X-GData-Client, X-GData-Key, X-GoogApps-Allowed-Domains, X-Goog-AdX-Buyer-Impersonation, X-Goog-Api-Client, X-Goog-Visibilities, X-Goog-AuthUser, x-goog-ext-124712974-jspb, x-goog-ext-467253834-jspb, x-goog-ext-251363160-jspb, x-goog-ext-259736195-jspb, x-goog-ext-477772811-jspb, X-Goog-PageId, X-Goog-Encode-Response-If-Executable, X-Goog-Correlation-Id, X-Goog-Request-Info, X-Goog-Request-Reason, X-Goog-Experiments, x-goog-iam-authority-selector, x-goog-iam-authorization-token, X-Goog-Spatula, X-Goog-Travel-Bgr, X-Goog-Travel-Settings, X-Goog-Upload-Command, X-Goog-Upload-Content-Disposition, X-Goog-Upload-Content-Length, X-Goog-Upload-Content-Type, X-Goog-Upload-File-Name, X-Goog-Upload-Header-Content-Encoding, X-Goog-Upload-Header-Content-Length, X-Goog-Upload-Header-Content-Type, X-Goog-Upload-Header-Transfer-Encoding, X-Goog-Upload-Offset, X-Goog-Upload-Protocol, x-goog-user-project, X-Goog-Visitor-Id, X-Goog-FieldMask, X-Google-Project-Override, X-Goog-Api-Key, X-HTTP-Method-Override, X-JavaScript-User-Agent, X-Pan-Versionid, X-Proxied-User-IP, X-Origin, X-Referer, X-Requested-With, X-Stadia-Client-Context, X-Upload-Content-Length, X-Upload-Content-Type, X-Use-Alt-Service, X-Use-HTTP-Status-Code-Override, X-Ios-Bundle-Identifier, X-Android-Package, X-Ariane-Xsrf-Token, X-YouTube-VVT, X-YouTube-Page-CL, X-YouTube-Page-Timestamp, X-Compass-Routing-Destination, x-framework-xsrf-token, X-Goog-Meeting-ABR, X-Goog-Meeting-Botguardid, X-Goog-Meeting-ClientInfo, X-Goog-Meeting-ClientVersion, X-Goog-Meeting-Debugid, X-Goog-Meeting-Identifier, X-Goog-Meeting-Interop-Cohorts, X-Goog-Meeting-Interop-Type, X-Goog-Meeting-RtcClient, X-Goog-Meeting-StartSource, X-Goog-Meeting-Token, X-Goog-Meeting-ViewerInfo, X-Goog-Meeting-Viewer-Token, X-Client-Data, x-sdm-id-token, X-Sfdc-Authorization, MIME-Version, Content-Transfer-Encoding, X-Earth-Engine-App-ID-Token, X-Earth-Engine-Computation-Profile, X-Earth-Engine-Computation-Profiling, X-Play-Console-Experiments-Override, X-Play-Console-Session-Id, x-alkali-account-key, x-alkali-application-key, x-alkali-auth-apps-namespace, x-alkali-auth-entities-namespace, x-alkali-auth-entity, x-alkali-client-locale, EES-S7E-MODE, cast-device-capabilities, X-Server-Timeout, x-foyer-client-environment, x-goog-greenenergyuserappservice-metadata, x-goog-sherlog-context
Access-Control-Allow-Methods: GET,HEAD,OPTIONS
Content-Length: 276959163
Date: Fri, 10 Feb 2023 16:38:47 GMT
Expires: Fri, 10 Feb 2023 16:38:47 GMT
Cache-Control: private, max-age=0
X-Goog-Hash: crc32c=z/a+AA==
Server: UploadServer
Connection: close


Downloading...
100%
```
Find ID:
```
URL:
https://drive.google.com/file/d/$ID/view
https://drive.google.com/uc?id=$ID&export=download
...

Example:
https://drive.google.com/file/d/11jGcJIdbR1MNtRct5DOR5Uk0aoICoXRl/view?usp=share_link
id = 11jGcJIdbR1MNtRct5DOR5Uk0aoICoXRl
```
Attention:
Google Drive Anonymous downloads have a daily limit, if exceed(maybe 4.8GB per file), it will say:
```html
Sorry, you can't view or download this file at this time.

Too many users have viewed or downloaded this file recently. Please try accessing the file again later. If the file you are trying to access is particularly large or is shared with many people, it may take up to 24 hours to be able to view or download the file. If you still can't access a file after 24 hours, contact your domain administrator.
```
Then, you can provide cookie and add it to headers to log in, not suggest.

You can split file too many small file to solve this problem:<br>
See here: https://github.com/wayne931121/tensorflow_remove_person_background_project/blob/main/Export_Model_Function.ipynb

https://colab.research.google.com/drive/1rDcVczczKy8IbUnfA4aAVrM_AKSwuJl7

先將檔案或資料夾壓縮成zip檔案並新增一個資料夾，再把zip檔案拆分放到剛新增的資料夾內，並上傳到google drive，最後將google drive資料夾內的檔案一個個個別下載再結合。
[Google Transform]
First compress the file or folder into a zip file and add a new folder, then split the zip file into the newly added folder, and upload it to google drive, and finally copy the files in the google drive folder one by one  Individual downloads are then combined.

1.Large File or Folder to Zip File
2.Add New Folder
3.Split Zip File to The New Folder(Split Large Zip File to Small Files that <25MB per file. Example one 900MB file to 90 10MB files.)
4.Upload The New Folder to Google Drive
5.Use Gdown Download File in Google drive  folder one by one.
6.Combine Splited File to Zip File
7.Unzip

On Computer:
```python
import os
import zipfile

def zip(path):
    zf = zipfile.ZipFile('{}.zip'.format(path), 'w', zipfile.ZIP_DEFLATED)
   
    for root, dirs, files in os.walk(path):
        for file_name in files:
            zf.write(os.path.join(root, file_name))
zip(path)

# 為了防止 colab gdown 下載檔案時因檔案過大而出現無法掃描病毒，造成下載失敗。
def export_for_google_drive(file, target_folder, size = 10*1024*1024):
    target_folder_files = target_folder+"\\%d"
    
    # Make target folder is empty.
    for e in os.listdir(target_folder):
        f = target_folder+"\\"+e
        os.remove(f)
    
    # Read source file, then write them to files by numbers.
    with open(file, "rb") as f:
        # 每個檔案大小 10MB
        # size = 10*1024*1024 # 單位 bytes
        i = 1
        while True:
            tmp = f.read(size)
            
            if len(tmp)==0 :
                break
            
            with open(target_folder_files%i, "wb") as gf:
                gf.write(tmp)
                
            i += 1
try:
    os.mkdir("detection model for google drive")
except:
    pass
# Limit 25MB
file = "detection_model.zip"
target = "detection model for google drive"
export_for_google_drive(file, target, 20*1024*1024)
```
On Google Colab:
```python
!gdown --no-cookies --folder "ID"
def export_from_split_file(source_folder, target_file):
    # create a empty file
    with open(target_file, "wb") as gf:
        gf.write(b"")
    
    # write all buffers to a new file
    export = sorted([int(i) for i in os.listdir(source_folder)])
    # For each source file, we read it, apppending to new file.
    with open(target_file, "ab") as f:
        
        for _ in export:
            tmp = source_folder+"/"+str(_)
            
            with open(tmp, "rb") as f1:
                tmp = f1.read(-1)
            
            f.write(tmp)
export_from_split_file("detection model for google drive", "detection_model.zip")
with zipfile.ZipFile("detection_model.zip", 'r') as zip_ref:
    zip_ref.extractall("/content")
!rm "detection model for google drive" -r
!rm "detection_model.zip"
```
