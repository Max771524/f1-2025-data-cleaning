import pandas as pd

# 載入資料
df = pd.read_csv("F1_2025_RaceResults.csv")

# 資料處理:
# 1. 將 DNF, DNS 或其他無成績的 Time/Retired 以 NaN 表示
df["Time/Retired"] = df["Time/Retired"].apply(lambda x: x if any(c.isdigit() for c in str(x)) else None)

# 2. 轉換 "Fastest Lap Time" 到時間格式，空值以 NaN 表示
df["Fastest Lap Time"] = pd.to_timedelta("0:" + df["Fastest Lap Time"].astype(str), errors="coerce")

# 3. 刪除或標記缺失值 (目前以標記 NaN 並保存資料完整性)
# 可視需要過濾 DNF 資料，例如： df = df.dropna(subset=['Time/Retired'])

# 儲存整理後資料
df.to_csv("F1_2025_RaceResults_CLEANED.csv", index=False)

# 資料概覽
print("資料整理完畢！")
print(df.info())
print(df.head())
