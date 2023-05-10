import os
import sys
#os.system('pip install websockets==10.4')
#os.system('pip install sanic==22.6.2')

import sanic
import uvloop
import aiohttp

from time         import time
import requests
from urllib.parse import urlencode
session = requests.Session()

import json
import asyncio

from typing import Any

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = sanic.Sanic("Config")

@app.route('/', methods=["GET"])
async def xxcz(request):
  return sanic.response.text('work')

@app.get("/disco")
async def disco(request):
  username = request.args.get('username')
  params = urlencode({
      "id": f"{str(username)}",
      "iid": 7228371047271089926,
      "device_id": 6875493957611849221,
      "channel": "googleplay",
      "aid": 1233,
      "app_name": "musical_ly",
      "version_code": 290204,
      "version_name": "29.2.4",
      "device_platform": "android",
      "ab_version": "29.2.4",
      "device_type": "SM-N976N",
      "device_brand": "samsung",
      "os_api": "28",
      "os_version": "9",
      "manifest_version_code": "2022902040",
      "resolution": "900*1600",
      "dpi": "320",
      "update_version_code": "2022902040",
      "_rticket": int(time() * 1000),
      "current_region": "FR",
      "sys_region": "FR",
      "mcc_mnc": "20801",
      "timezone_name": "Africa/Harare",
      "ts": int(time()),
      }
  )

  api = 'https://www.tikwm.com/api/service/sign'
  postData = {
      'params': params,
      'headers': '{"user-agent":"okhttp/3.10.0.1"}'
  }

  response = session.post(api, data=postData, verify=True)
  
  x = session.get(
      url="https://api31-normal-alisg.tiktokv.com/aweme/v1/user/uniqueid/?" + params,
      headers={
          "accept-encoding": "gzip",
          "connection": "Keep-Alive",
          "cookie": "",
          "host": "api31-normal-alisg.tiktokv.com",
          "multi_login": "1",
          "passport-sdk-version": "19",
          "sdk-version": "2",
          "user-agent": "com.zhiliaoapp.musically/2022804030 (Linux; U; Android 9; fr_FR; SM-N976N; Build/LMY48Z;tt-ok/3.12.13.1)",
          "x-argus": response.json()["data"]["X-Argus"],
          "x-gorgon": response.json()["data"]["X-Gorgon"],
          "x-khronos": str(response.json()["data"]["X-Khronos"]),
          "x-ladon": response.json()["data"]["X-Ladon"],
          "x-ss-req-ticket": str(int(time() * 1000)),
          "x-tt-store-region": "fr",
          "x-tt-store-region-src": "local",
          "x-vc-bdturing-sdk-version": "2.3.0.i18n"
      }
  ).json()
  new = {
    "ims": x['uid'],
    "ncs": x['sec_uid']
  }
  return sanic.response.json(new)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, access_log=True)
