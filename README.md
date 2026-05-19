# 🚀 Full-Stack CI/CD Pipeline Demo

這是一個展示現代化軟體工程標準工作流的示範專案。本專案整合了 **GitHub Actions** 與 **Docker**，實現了從程式碼提交、自動化測試到容器化打包的完整 CI/CD (持續整合與持續佈署) 流程。

## ✨ 核心特色 (Key Features)

- **自動化單元測試 (CI)**：基於 Python 內建的 `unittest`，具備多檔案探索機制 (`discover`)，並涵蓋正常邏輯與邊界特例 (Edge Cases) 測試。
- **自動化容器打包 (CD)**：當程式碼合併至 `main` 分支且通過測試後，GitHub Actions 會自動編譯 `Dockerfile` 並將映像檔 (Image) 推送至 **GitHub Container Registry (GHCR)**。
- **防護網機制 (Quality Gate)**：透過 Pull Request 觸發測試，嚴格阻擋帶有 Bug 的程式碼進入正式環境。
- **關注點分離 (SRP)**：核心商業邏輯與測試程式碼完全分離，確保系統具備高可維護性。

## 🛠️ 技術堆疊 (Tech Stack)

- **語言**: Python 3.10
- **測試框架**: `unittest` / `unittest.mock`
- **CI/CD 平台**: GitHub Actions
- **容器化技術**: Docker
- **套件管理**: `pip` (搭配 `requirements.txt`)

## 📂 專案結構 (Project Structure)

```text
.
├── .github/workflows/
│   └── ci-cd.yaml       # GitHub Actions 的核心自動化腳本
├── app.py               # 核心商業邏輯
├── CICDTest.py          # 針對正常情境的單元測試
├── EdgeCaseTest.py      # 針對邊界條件與特例的單元測試
├── AdvancedTest.py      # 進階測試示範 (包含 Mock 副作用測試)
├── Dockerfile           # 應用程式容器化打包指令
├── requirements.txt     # 第三方套件依賴清單
├── Summary.md           # 專案從零建置的完整教學總結
└── .gitignore           # Git 版本控制忽略清單
```

## 🚀 快速開始 (Quick Start)

### 1. 本地端執行單元測試
在專案根目錄下，執行以下指令即可一次跑完所有測試：
```bash
python -m unittest discover -p "*Test.py"
```

### 2. 本地端 Docker 打包與執行
```bash
# 建置 Docker Image
docker build -t my-cicd-app .

# 啟動容器
docker run --rm my-cicd-app
```
