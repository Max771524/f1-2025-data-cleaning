# F1 2025 資料清洗專案

## 專案概覽
本專案以 `F1_2025_RaceResults.csv` 資料集為例，練習資料清洗、整理及處理技術，建立一套可套用到其他資料集的處理範例。

-資料來源:`https://www.kaggle.com/datasets/makslypko/f1-race-result-2025
### 資料處理步驟
- 載入資料 (`pandas`)
- 處理資料中的異常值，例如：
  - `Time/Retired` 欄位中的 `DNF`、`DNS` 資料以 `NaN` 表示
- 轉換時間資料 (`Fastest Lap Time`) 到時間格式
- 標記缺失值，保存資料完整性
- 輸出處理後資料檔案 `F1_2025_RaceResults_CLEANED.csv`

### 資料庫說明
- 原始資料：`F1_2025_RaceResults.csv`
- 清洗後資料：`F1_2025_RaceResults_CLEANED.csv`
- 程式檔案：`data_cleaning.py`

---

### 執行環境
- Python 3.9+
- 套件：`pandas`

安裝：
```bash
pip install pandas
