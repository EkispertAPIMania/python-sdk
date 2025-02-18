# 駅すぱあと API SDK for Python

[駅すぱあと API](https://docs.ekispert.com/v1/index.html)をPythonから利用するためのSDKです。

## インストール

`pip` でインストールします。

```
pip install ekispert
```

## 初期化

初期化時には、駅すぱあと APIのAPIキーを指定します。[APIキーはトライアル申し込みより取得](https://api-info.ekispert.com/form/trial/)してください。

```py
from ekispert.client import Ekispert

client = Ekispert("YOUR_API_KEY")
```

## 駅情報の取得

駅情報取得APIを実行します。検索条件、結果は[駅情報 - 駅すぱあと API Documents 駅データ・経路検索のWebAPI](https://docs.ekispert.com/v1/api/station.html)を参照してください。

```py
query = StationQuery()
query.code = 22828
points = query.execute()
assert len(points) == 1
assert points[0].station.name == '東京'
assert points[0].geo_point.lati_d == 35.678083
assert points[0].prefecture.name == '東京都'
assert points[0].prefecture.code == 13
```

## ライセンス

MITライセンスです。
