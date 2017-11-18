# -*- coding: utf-8 -*-

import requests

'''
tn:resultjson_com
ipn:rj
ct:201326592
is:
fp:result
queryWord:微距摄影
cl:2
lm:-1
ie:utf-8
oe:utf-8
adpicid:
st:-1
z:
ic:0
word:微距摄影
s:
se:
tab:
width:
height:
face:0
istype:2
qc:
nc:1
fr:
pn:60
rn:30
gsm:3c
1510961219650:
'''

RequestURL = 'http://image.baidu.com/search/acjson'
Parameters = ''

finalUrl = RequestURL + Parameters

cookies = {
    'BDUSS': ''
}

req = requests.get(url=finalUrl, cookies=cookies)