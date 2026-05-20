#!/usr/bin/env python3
"""
Google OAuth 認證腳本
執行一次即可，之後我就能幫你操作 Gmail / Calendar / Drive

使用方法:
    python3 auth.py

執行後會:
1. 自動開啟瀏覽器
2. 讓你登入 Google 帳號
3. 取得授權
4. 把 token 存到 token.json 以後就不用再認證了
"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.file',
]

CREDENTIALS_PATH = 'credentials.json'
TOKEN_PATH = 'token.json'


def main():
    # 確認 credentials 存在
    if not os.path.exists(CREDENTIALS_PATH):
        print(f'錯誤：找不到 {CREDENTIALS_PATH}')
        print('請把 Google Cloud Console 下載的 credentials.json 放在同目錄')
        return
    
    print('開始 OAuth 認證...')
    print('將自動開啟瀏覽器，請在瀏覽器中登入並授權')
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    credentials = flow.run_local_server(port=0, prompt='consent')
    
    # 儲存 token
    with open(TOKEN_PATH, 'w') as f:
        f.write(credentials.to_json())
    
    print(f'✓ 認證成功！Token 已儲存到 {TOKEN_PATH}')
    print('之後直接執行其他腳本即可，不需要再認證')


if __name__ == '__main__':
    main()