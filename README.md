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
query = client.stationQuery()
query.code = 22828
points = query.execute()
assert len(points) == 1
assert points[0].station.name == '東京'
assert points[0].geo_point.lati_d == 35.678083
assert points[0].prefecture.name == '東京都'
assert points[0].prefecture.code == 13
```

## 駅簡易情報の取得

駅簡易情報APIを実行します。検索条件、結果は[駅簡易情報 \- 駅すぱあと API Documents 駅データ・経路検索のWebAPI](https://docs.ekispert.com/v1/api/station/light.html)を参照してください。

```python
query = client.stationLightQuery()
query.name = '東京'
points = query.execute()
assert len(points) > 0
assert points[0].station.name == '東京'
assert points[0].prefecture.name == '東京都'
assert points[0].prefecture.code == 13
```

## 平均待ち時間探索

平均待ち時間探索APIを実行します。検索条件、結果は[平均待ち時間探索 \- 駅すぱあと API Documents 駅データ・経路検索のWebAPI](https://docs.ekispert.com/v1/api/search/course/plain.html)を参照してください。

```python
query = client.searchCoursePlainQuery()
query.from_ = 25077
query.to = 29090
courses = query.execute()
assert len(courses) > 0
assert courses[0].routes[0] is not None
assert courses[0].prices[0].kind == "ChargeSummary"
assert courses[0].prices[0].one_way == 2530
assert courses[0].prices[0].round == 5060
```

## 経路探索

経路探索APIを実行します。検索条件、結果は[経路探索 \- 駅すぱあと API（旧：駅すぱあとWebサービス） Documents 駅データ・経路検索のWebAPI](https://docs.ekispert.com/v1/api/search/course/extreme.html)を参照してください。

```python
query = client.courseExtremeQuery()
query.via_list = ['22671', '22741']
query.answer_count = 1
courses = query.execute()
assert len(courses) == 1
assert courses[0].serialize_data is not None
assert courses[0].teiki.serialize_data is not None
assert courses[0].routes[0].lines[0].train_id is not None
assert courses[0].pass_statuses[0].name is not None
assert courses[0].pass_statuses[0].kind is not None
assert courses[0].prices[0].kind == "ChargeSummary"
assert courses[0].routes[0].distance == 58
assert courses[0].routes[0].exhaust_co2 == 116
```

## 定期券の払い戻し計算

定期券の払い戻し計算APIを実行します。検索条件、結果は[定期券の払い戻し計算 \- 駅すぱあと API Documents 駅データ・経路検索のWebAPI](https://docs.ekispert.com/v1/api/course/repayment.html)を参照してください。

```python
query = client.courseRepaymentQuery()
query.serializeData = '1,true'
query.checkEngineVersion = False
query.serializeData = 'VkV4QaECp9nIAsMCpgEz76YDpgEz76UEkcIBQwAAAAKmATPvpQPKAQECAQMBBAEHAQgBCgIPQv9_EKX_9xSRpVjVBZfBAqVYj8ECpVjVwQKlWXvBAqVZLMECpVkPwQKlWvHBAqVXwAaSwwEBAgEDxwGlWFoCDQMPBQMGRDk0NlQHBAgDwwEBAgEDxgGmAAIwMwIVAxYFAwcGCAUHksUBpgEz76gDpQJfBKUCZgUACADGAaYBM||oAgEDpQJwBKUCcQUACAAIksQEAQUBB6RtCAHGAgEEAgUBBgEHpQEvCAIJksEDAcMBAQIBAwEPkcUBkwABAgKSwwEAAgADAMMBAQIBAwEDksMBAAIAAwDDAQECAQMBBJIAAQWSAAA*--T3221233232319:F332112212000:A23121141:--88eed71f6168dfe5ab30b8cc5e938621dd3806a7--0--0--0--284'
results = query.execute()
assert results['repayment_list'] is not None
assert results['teiki_route'] is not None
assert results['repayment_list'].repayment_date is not None
assert results['repayment_list'].repayment_tickets is not None
assert results['repayment_list'].repayment_tickets[0].fee_price_value is not None
assert results['teiki_route'].section_separator is not None
assert results['teiki_route'].teiki_route_sections is not None
assert results['teiki_route'].teiki_route_sections[0].points is not None
assert results['teiki_route'].teiki_route_sections[0].points[0].station.name is not None
assert results['teiki_route'].teiki_route_sections[0].points[0].prefecture is not None
```

## 緯度経度からの周辺駅検索

```py
query = client.geoStationQuery()
query.set_geo_point(langitude="35.6783055555556", longitude="139.770441666667", radius=1000, geodetic='tokyo')
# または
query.set_geo_point(langitude="35.6783055555556", longitude="139.770441666667", radius=1000)
# または
query.set_geo_point(langitude="35.6783055555556", longitude="139.770441666667", geodetic='tokyo')
# または
query.set_geo_point(langitude="35.6783055555556", longitude="139.770441666667")
points = query.execute()
assert(len(points) > 0)
assert(isinstance(points[0], Point))
assert(points[0].station.name is not None)
assert(points[0].prefecture is not None)
assert(points[0].prefecture.name is not None)
assert(points[0].prefecture.code is not None)
print(points[0].distance)

print(points[0].station.name)
print(points[0].prefecture)
print(points[0].prefecture.name)
print(points[0].prefecture.code)
```

## ライセンス

MITライセンスです。
