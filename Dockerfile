# 使用官方 Python 輕量級映像檔作為基底
FROM python:3.10-slim

# 在容器內部建立並設定工作目錄
WORKDIR /app

# 將當前目錄下的所有檔案複製到容器的 /app 目錄中
COPY . /app

# 讀取並安裝專案依賴套件
# --no-cache-dir 參數可避免產生不必要的暫存檔，讓打包出來的 Docker Image 體積更小
RUN pip install --no-cache-dir -r requirements.txt

# 容器啟動時執行的預設指令 (啟動我們的主程式)
CMD ["python", "app.py"]