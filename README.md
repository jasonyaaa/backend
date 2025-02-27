# 後端 Backend
Python 版本為 3.13.0
## 環境設定
### 建立虛擬環境
```
python -m venv venv
```
或使用 VSCode 的虛擬環境
### 安裝套件
```
pip install -r requirements.txt
```
### 啟動伺服器
```
python app.py
```
### 如何將新增的套件加入 requirements.txt
```
pip freeze > requirements.txt
```
### 如何執行docker
```
docker run -d -p 5001:5000 vocalborn_backend
```
## 參考來源
- [資料夾結構](https://ashleyalexjacob.medium.com/flask-api-folder-guide-2023-6fd56fe38c00)
- [方便中大型專案的維護](https://wehelp.tw/topic/5106248399716352)