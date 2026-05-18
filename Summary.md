# 🚀 Full-Stack CI/CD Pipeline 專案建置教學總結

本專案示範了如何從零開始建置一個具備「自動化測試 (CI)」與「自動化容器打包 (CD)」的現代化軟體開發工作流。

---

## 📌 第一階段：專案初始化與 Git 基礎設定

在撰寫程式碼之前，我們必須先建立良好的版本控制習慣，並過濾掉不該上傳的機密與垃圾檔案。

### 1. 建立 `.gitignore` 檔案
在專案根目錄建立 `.gitignore`，確保如 `.env` (機密變數)、`venv/` (虛擬環境) 與 `__pycache__/` (快取) 等檔案不會被推送到 GitHub。

### 2. 初始化 Git 儲存庫
打開終端機，在專案根目錄依序執行以下指令：
```bash
# 初始化本機儲存庫
git init

# 將所有檔案加入暫存區 (會自動略過 .gitignore 裡定義的檔案)
git add .

# 提交第一次的變更
git commit -m "chore: 專案初始化與設定 .gitignore"

# 將主分支強制命名為 main (符合現今 GitHub 預設標準)
git branch -M main
```

---

## 📌 第二階段：撰寫商業邏輯與單元測試

我們採用**「關注點分離 (Separation of Concerns)」**的原則，將核心邏輯與測試程式碼分開管理。

### 1. 建立核心程式 (`app.py`)
撰寫專案的商業邏輯（例如 `add_numbers` 函式），作為未來要上線運行的主程式。

### 2. 建立測試程式 (`CICDTest.py`)
引入 Python 內建的 `unittest` 模組，並從 `app.py` 匯入要測試的函式，編寫測試案例。這個檔案將在 CI 階段扮演「防護網」的角色。

---

## 📌 第三階段：Docker 容器化設定 (CD 的前置作業)

為了解決「在我的電腦可以跑，但在伺服器會壞掉」的問題，我們使用 Docker 將環境標準化。

### 建立 `Dockerfile`
在專案根目錄建立 `Dockerfile` (無副檔名)，寫入以下指令：
1. `FROM python:3.10-slim` (使用輕量級 Python 基礎環境)
2. `WORKDIR /app` (設定容器內工作目錄)
3. `COPY . /app` (將本機程式碼複製進容器)
4. `CMD ["python", "app.py"]` (設定容器啟動時執行的預設指令)

---

## 📌 第四階段：建立 GitHub 遠端儲存庫

我們使用 GitHub CLI (`gh`) 來快速在雲端建立儲存庫，並推送本地程式碼。

```bash
# 1. 登入 GitHub 帳號並授權
gh auth login

# 2. 建立名為 CICDPipeline-Demo 的公開專案，並自動將本地程式碼推上去
gh repo create CICDPipeline-Demo --public --source=. --remote=origin --push
```

---

## 📌 第五階段：建置 GitHub Actions (CI/CD 核心)

在專案中建立 `.github/workflows/ci-cd.yaml` 檔案，宣告自動化腳本。我們的 Pipeline 分為兩個 Job：

### Job 1: `integration` (持續整合 - CI)
* **觸發條件**：當有程式碼 `push` 到 `main` 分支時執行。
* **執行步驟**：
  1. 拉取程式碼 (`actions/checkout`)
  2. 建立 Python 3.10 環境 (`actions/setup-python`)
  3. 執行語法檢查 (`py_compile`)
  4. **執行單元測試** (`python -m unittest CICDTest.py`) ➔ 若測試失敗，流程立即終止！

### Job 2: `deployment` (持續佈署 - CD)
* **觸發條件**：必須等 `integration` 階段成功 (`needs: integration`) 才會執行。
* **執行步驟**：
  1. **登入 GHCR** (GitHub Container Registry)：利用 GitHub Actions 內建的 `GITHUB_TOKEN` 自動登入，無需手動設定密碼。
  2. **環境變數轉換**：使用指令將 GitHub 專案名稱轉為全小寫，以符合 Docker 映像檔的嚴格命名規範。
  3. **打包並推送**：使用 `docker/build-push-action` 將 `Dockerfile` 編譯成 Image，並使用全小寫名稱打上標籤 (Tag) 上傳至 GitHub Packages 供未來伺服器拉取。

---

## 📌 第六階段：測試與驗證 CI/CD 流程

### 1. 測試 CI 防禦機制 (故意破壞)
* 修改 `CICDTest.py`，故意將預期結果寫錯（例如改為 `999`）。
* `git commit` 並 `push` 到 GitHub。
* **結果觀察**：GitHub Actions 中 `integration` 階段會亮紅燈 ❌，且 `deployment` 階段不會被執行。成功阻擋壞代碼！

### 2. 測試 CD 自動打包 (修復並放行)
* 將測試代碼修復回正確數值。
* 再次 `push` 到 GitHub。
* **結果觀察**：CI 階段通過 ✅，接著 CD 階段成功將 Docker Image 打包，並發布在專案首頁右下角的 **Packages** 區塊中！

---
🎉 **結論**：透過以上步驟，我們成功建立了一個能**自動檢查程式碼品質**，並且能**自動將應用程式封裝成標準化 Docker 容器**的現代化開發流程！