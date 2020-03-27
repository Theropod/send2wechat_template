# -*- coding: UTF-8 -*-
# 3 hard-coded id/secrest in wechat for work: corpid, corpsecret, agentid
# see https://www.cnblogs.com/mengyu/p/10073140.html
import requests
import json
def get_token():
    payload_access_token = {'corpid': 'ww2841fdcaad043e7d', 'corpsecret': '5Oule66iuL8PPiX3cFdevonHfqP2y0e3-wZKyTrDurY'}
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    r = requests.get(token_url, params=payload_access_token)
    dict_result = (r.json())
    return dict_result['access_token']


def send_textmessage(textmessage):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % get_token()
    # expecting a dictionary
    data={"toparty": 1, "msgtype": "text", "agentid": 1000002, "text": {"content": textmessage}, "safe": 0}
    data = json.dumps(data, ensure_ascii=False)
    r = requests.post(url=url, data=data.encode("utf-8"))
    return r.json()