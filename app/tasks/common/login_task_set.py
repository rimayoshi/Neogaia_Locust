from locust import TaskSet
from apis.model_abstract import *
from apis.params.user_auth_api_request import *
from apis.params.user_auth_api_response import *

class LoginTaskSet(TaskSet):
    def login(self, npsn, token, npaCode):
        """
        アプリの認証呼び出し関数
        成功時はuserプロパティにユーザ情報がセットされる
        """
        # TODO: 認証情報をスレッド毎に切り替える方法
        # TODO: authじゃなくregisterの場合への対応
        req = UserAuthApiRequest()
        req.setNpsn(npsn)
        req.setToken(token)
        req.setNpaCode(npaCode)

        res = self.post(req, UserAuthApiResponse)
        self.user = res.getUser()

    def post(self, req, responseClass):
        # リクエスト送信
        reqResult = self.client.post(req.getApiPath(), req.getPackedParams())

        # レスポンスモデル生成
        content = unpack(reqResult.content)
        params = unpack(content[2])
        cls = globals()[responseClass.__name__]
        return cls(params)
