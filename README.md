Django LINE Login
===

使用 Django 實作 LINE Login

### 

### Setup
- 在 [LINE Developers Console](https://developers.line.biz/console/) 建立一個 LINE Login Channel
- 將 Channel 中的 Callback URL 設為 `http://localhost:8000/auth/line/callback`
- 取得 `Channel ID` 和 `Channel secret` 
- 在根目錄下建立檔案 `.env`
- 將 `.env.example` 的內容拷貝至 `.env` 並將 `Channel ID` 和 `Channel secret` 分別填入 `CLIENT_ID` 和 `CLIENT_SECRET`

### Run the App
```console
$ pip install -r requirements.txt
$ python mange.py makemigrations
$ python mange.py migrate
$ python manage.py runserver
```