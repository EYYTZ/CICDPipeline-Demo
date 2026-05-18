# 使用官方 Python 輕量級映像檔作為基底
FROM python:3.10-slim

# 在容器內部建立並設定工作目錄
WORKDIR /app

# 將當前目錄下的所有檔案複製到容器的 /app 目錄中
COPY . /app

# 如果未來你有 requirements.txt，可以取消下方的註解來安裝依賴套件
# RUN pip install --no-cache-dir -r requirements.txt

# 容器啟動時執行的預設指令 (啟動我們的主程式)
CMD ["python", "app.py"]