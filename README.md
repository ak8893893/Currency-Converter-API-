# 匯率轉換 API

匯率轉換 API 是一個簡單的應用程式介面，用於實現不同貨幣之間的匯率轉換，同時支援四捨五入和千分位分隔符。

## 使用說明
### 安裝相依套件

請確保已經安裝以下相依套件：

- Flask

你可以使用以下指令安裝相依套件：

```
pip install Flask
```

啟動應用程式
執行 Currency Converter API 應用程式：

```
python main.py
```

API 會在 http://localhost:5000 上運行。

使用 API
您可以使用 GET 請求來呼叫 API，並提供以下參數：

source: 來源貨幣代碼
target: 目標貨幣代碼
amount: 金額（以美元符號 $ 和千分位分隔符表示）

範例請求：
```
http://localhost:5000/convert?source=USD&target=JPY&amount=$1,525
```

範例回應：
```
{
    "msg": "success",
    "amount": "$170,496.53"
}
```

單元測試
Currency Converter API 包含了單元測試，您可以運行測試以確保 API 的正確性。

執行單元測試：
```
python test_currency_converter.py
```

匯率資料
API 使用以下匯率資料作為範例資料：
```
{
    "currencies": {
        "TWD": {
            "TWD": 1,
            "JPY": 3.669,
            "USD": 0.03281
        },
        "JPY": {
            "TWD": 0.26956,
            "JPY": 1,
            "USD": 0.00885
        },
        "USD": {
            "TWD": 30.444,
            "JPY": 111.801,
            "USD": 1
        }
    }
}

```

Author: AK Lai
License: MIT