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
## Conventional Commits：
- feat: 新功能
- fix: 修復 bug
- test: 新增或修正測試
- refactor: 程式碼重構，不改變外部行為
- style: 不影響程式碼含義的變化（如格式化）
- docs: 文件相關變更
- chore: 其他變更（如建構過程、輔助工具等）
## 參考來源
- [資料夾結構](https://ashleyalexjacob.medium.com/flask-api-folder-guide-2023-6fd56fe38c00)
- [方便中大型專案的維護](https://wehelp.tw/topic/5106248399716352)
- [如何命名commit message](https://wadehuanglearning.blogspot.com/2019/05/commit-commit-commit-why-what-commit.html)
- [FastAPI](https://fastapi.tiangolo.com/)