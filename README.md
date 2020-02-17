# 負荷試験用スクリプト
負荷試験用のスクリプトです。  
[Locust](https://docs.locust.io/en/stable/index.html) を使ってます。

## 開発環境
任意のIDE or エディタ + Python サポート  
Python 3.8 で動作を確認。  

## 準備
pip で locustio と msgpack-python をインストールしてください。  
```pip install locustio msgpack-python```  

## 起動
```
locust -f ./app/locustfile.py
```
または
```
cd app
locust
```  
複数台でやる場合は、```--master``` とか、```--slave --master-host=xxxxx``` みたいにやるみたい。  

  
Web画面なしでやる場合は、```--no-web -c 10 -r 3 -n 1000``` みたいにして実行。  

|option||
|:-:|-|
|-c|同時接続数|
|-r|秒間のスポーン数|
|-n|合計リクエスト数(省略可)|  

