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
