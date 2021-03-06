# API Document
## Index
* [Users](#users-title)
  + [/users](#users-sub-title)
    - [[POST] 회원가입](#post-users)
  + [/auth](#auth-sub-title)
    - [[POST] Login](#post-auth)
* [Folders](#folders-title)
  + [/folders](#folders-sub-title)
    - [[POST] create folder](#post-folders)
  + [/folders/<folder_id>](#folders-folderid-sub-title)
    - [[GET] get folder information](#get-folders)
    - [[PATCH] update folder information](#patch-folders)
    - [[DELETE] delete folder](#delete-folders)
* [Files](#files-title)
  + [/files](#files-sub-title)
    - [[POST] file upload](#post-files)
  + [/files/<file_id>](#files-fileid-sub-title)
    - [[GET] file download](#get-files)
    - [[DELETE] file delete](#delete-files)
* [Config](#config-title)
  + [/ping](#ping-sub-title)
    - [[GET] for health check](#get-ping)

## Users <a id="users-title"></a>
### /users <a id="users-sub-title"></a>
#### [POST] register user <a id="post-users"></a>
새 계정을 생성합니다. root folder도 함께 생성합니다.


* Body

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|name|None|사용자 아이디|formData|string|true|
|password|None|사용자 비밀번호|formData|SHA256 encrypted string|true|


* Response (status code: 200)
```json
{
  "new_user": 1
}
```


* Example

```commandline
curl -X "POST" "https://upload-now-box.cf/users" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "name": "firstuser",
  "password": "20504cdfddaad0b590ca53c4861edd4f5f5cf9c348c38295bd2dbf0e91bca4c3"
}'
```


### /auth <a id="auth-sub-title"></a>
#### [POST] Login <a id="post-auth"></a>
Login API 입니다. access_token으로 JWT token을 반환합니다.


* Body

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|name|None|사용자 아이디|formData|string|true|
|password|None|사용자 비밀번호|formData|SHA256 encrypted string|true|


* Response (status code: 200)
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQwODExNiwianRpIjoiMWQ4ZmIxNjAtNDQ3My00ZDJlLTg1NDItNzNlZjBjNTFiM2FmIiwibmJmIjoxNjE4NDA4MTE2LCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjQsImV4cCI6MTYxOTAxMjkxNiwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjI6NDc6NTUifQ.gqOjDBVegv-jACs8n1AK2BZdL2D_Ueu2-qsYLA5RAtQ"
}
```


* Exception

  + "User not found": name에 해당하는 유저가 존재하지 않을 경우
  + "Password error": password 검증에 실패할 경우


* Example
```commandline
curl -X "POST" "https://upload-now-box.cf/auth" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "name": "firstuser2",
  "password": "20504cdfddaad0b590ca53c4861edd4f5f5cf9c348c38295bd2dbf0e91bca4c3"
}'
```


## Folders <a id="folders-title"></a>
### /folders <a id="folders-sub-title"></a>
#### [POST] create folder <a id="post-folders"></a>
folder를 생성합니다. parent_id로 상위 folder의 id를 전달하여 상하관계를 설정합니다.


* Body

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|name|None|folder name|formData|string|true|
|parent_id|None|parent folder id|formData|integer|true|


* Response (status code: 200)
```json
{
  "folder_id": 5
}
```

* Example
```commandline
curl -X "POST" "https://upload-now-box.cf/folders" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMDgzNjczMywianRpIjoiYzMxODc3MGEtMWE1NC00ZjYwLWJkNGItNWZmMmMyMzkwNGE5IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoxLCJuYmYiOjE2MjA4MzY3MzMsImV4cCI6MTYyMTQ0MTUzMywiY3JlYXRlZF9hdCI6IjIwMjEtMDUtMDVUMTQ6NTU6MzYifQ.9pLCpFjEqkvWoxc76N8zTCUPgl90ojP893qTja_nYZo' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "name": "new folder",
  "parent_id": 1
}'
```


### /folders/<folder_id> <a id="folders-folderid-sub-title"></a>
#### [GET] get folder information <a id="get-folders"></a>
folder의 정보, 하위 folder 정보, 현재 folder 내의 file 정보를 반환합니다. 


* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|folder_id|None|folder id|path|integer|true|


* Response (status code: 200)
```json
{
  "child_folders": [
    {
      "id": 2,
      "name": "update folder",
      "parent_id": 1
    }
  ],
  "current_folder": {
    "id": 1,
    "name": "root",
    "parent_id": null
  },
  "files": [
    {
      "id": 1,
      "name": "conaf.jpg"
    }
  ]
}
```


* Exception
  + "Folder not Exist": folder_id에 해당하는 folder가 존재하지 않은 경우
  + "ForbiddenError": folder의 소유자가 아닌 경우


* Example
```commandline
curl "https://upload-now-box.cf/folders/1" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMDgzNjczMywianRpIjoiYzMxODc3MGEtMWE1NC00ZjYwLWJkNGItNWZmMmMyMzkwNGE5IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoxLCJuYmYiOjE2MjA4MzY3MzMsImV4cCI6MTYyMTQ0MTUzMywiY3JlYXRlZF9hdCI6IjIwMjEtMDUtMDVUMTQ6NTU6MzYifQ.9pLCpFjEqkvWoxc76N8zTCUPgl90ojP893qTja_nYZo'
```


#### [PATCH] update folder information <a id="patch-folders"></a>
folder의 정보를 수정합니다.


* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|folder_id|None|folder id|path|integer|true|
|name|None|folder name for update|formData|string|true|


* Response (status code: 200)
```json
{
  "folder_id": 5
}
```


* Exception
  + "Folder not Exist": folder_id에 해당하는 folder가 존재하지 않은 경우
  + "ForbiddenError": folder의 소유자가 아닌 경우
  

* Example
```commandline
curl -X "PATCH" "https://upload-now-box.cf/folders/2" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMDgzNjczMywianRpIjoiYzMxODc3MGEtMWE1NC00ZjYwLWJkNGItNWZmMmMyMzkwNGE5IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoxLCJuYmYiOjE2MjA4MzY3MzMsImV4cCI6MTYyMTQ0MTUzMywiY3JlYXRlZF9hdCI6IjIwMjEtMDUtMDVUMTQ6NTU6MzYifQ.9pLCpFjEqkvWoxc76N8zTCUPgl90ojP893qTja_nYZo' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "name": "update folder"
}'
```


#### [DELETE] delete folder <a id="delete-folders"></a>
folder를 삭제합니다.


* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|folder_id|None|folder id|path|integer|true|


* Response (status code: 200)
```json
{
  "success": true
}
```


* Exception
  + "Folder not Exist": folder_id에 해당하는 folder가 존재하지 않은 경우
  + "ForbiddenError": folder의 소유자가 아닌 경우
  

* Example
```commandline
curl -X "DELETE" "https://upload-now-box.cf/folders/2" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMDgzNjczMywianRpIjoiYzMxODc3MGEtMWE1NC00ZjYwLWJkNGItNWZmMmMyMzkwNGE5IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoxLCJuYmYiOjE2MjA4MzY3MzMsImV4cCI6MTYyMTQ0MTUzMywiY3JlYXRlZF9hdCI6IjIwMjEtMDUtMDVUMTQ6NTU6MzYifQ.9pLCpFjEqkvWoxc76N8zTCUPgl90ojP893qTja_nYZo'
```


## Files <a id="files-title"></a>
### /files <a id="files-sub-title"></a>
#### [POST] file upload <a id="post-files"></a>
file을 생성합니다.


* Body
  
|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|file|None|file for upload|formData|base64 encoded file|true|
|filename|None|file name|formData|string|true|
|folder_id|None|folder id for file|formData|integer|true|


* Response (status code: 200)
```json
{
  "file_id": 5
}
```


* Example
```commandline
curl -X "POST" "https://upload-now-box.cf/files" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMDgzNjczMywianRpIjoiYzMxODc3MGEtMWE1NC00ZjYwLWJkNGItNWZmMmMyMzkwNGE5IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoxLCJuYmYiOjE2MjA4MzY3MzMsImV4cCI6MTYyMTQ0MTUzMywiY3JlYXRlZF9hdCI6IjIwMjEtMDUtMDVUMTQ6NTU6MzYifQ.9pLCpFjEqkvWoxc76N8zTCUPgl90ojP893qTja_nYZo' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "folder_id": 1,
  "file": "base64 encoded file",
  "filename": "test.jpg"
}'
```


### /files/<file_id> <a id="files-fileid-sub-title"></a>
#### [GET] file download <a id="get-files"></a>
file download


* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|file_id|None|file_id for download|path|integer|true|


* Response (status code: 200)
  + file


* Exception
  + "File not Exist": file_id에 해당하는 file이 존재하지 않은 경우
  + "ForbiddenError": file의 소유자가 아닌 경우
  

* Example
```commandline
curl "https://upload-now-box.cf/files/2" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQxMDU3MSwianRpIjoiMjM2MmI5YzgtZjc1OS00NDAxLTljNTQtZWEyYWYxNTkwMzk3IiwibmJmIjoxNjE4NDEwNTcxLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImV4cCI6MTYxOTAxNTM3MSwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjM6Mjk6MjcifQ.-rFVaVoap2UsfC8QrltNE32qZfGEpcbZzHf-SBpe1hk'
```


#### [DELETE] file delete <a id="delete-files"></a>
file 삭제


* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|file_id|None|file_id for download|path|integer|true|


* Response (status code: 200)
```json
{
  "success": true
}
```


* Exception
  + "File not Exist": file_id에 해당하는 file이 존재하지 않은 경우
  + "ForbiddenError": file의 소유자가 아닌 경우


* Example
```commandline
curl -X "DELETE" "https://upload-now-box.cf/files/2" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQxMDU3MSwianRpIjoiMjM2MmI5YzgtZjc1OS00NDAxLTljNTQtZWEyYWYxNTkwMzk3IiwibmJmIjoxNjE4NDEwNTcxLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImV4cCI6MTYxOTAxNTM3MSwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjM6Mjk6MjcifQ.-rFVaVoap2UsfC8QrltNE32qZfGEpcbZzHf-SBpe1hk'
```


## Config <a id="config-title"></a>
### /ping <a id="ping-sub-title"></a>
#### [GET] for health check <a id="get-ping"></a>
health check 용 API


* Response (status code: 200)
```json
{
  "result": "pong"
}
```


* Example
```commandline
curl "https://upload-now-box.cf/ping"
```
