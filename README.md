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