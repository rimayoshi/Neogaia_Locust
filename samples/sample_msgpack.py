import msgpack

# 変換するデータを用意
data = {u'key':u'myKeyName', u'日本語キー':u'日本語の値'}

# シリアライズ実行
packed = msgpack.packb(data)

# 変換後のバイト長表示
print('変換後のbyte:', len(packed))

# デシリアライズ
ret = msgpack.unpackb(packed, encoding='utf-8')

# ちゃんと復元できたか確認
print(u'key:' + ret[u'key'])
print(u'日本語キー:' + ret[u'日本語キー'])

###
# python samples/sample_msgpack.py で実行
# ※動かない場合は一度 pip install msgpack してみる
###