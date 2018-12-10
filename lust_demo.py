#-*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
import os
'''性能测试任务类'''
class WebsiteTasks(TaskSet):

#初始化函数
    def on_start(self):
        '''
        path = os.path.abspath('.')
        try:
            with open("%s/interface/reportDataUpdate.json"%(path), "r") as f:
                self.request_json = json.load(f)
        except (IOError):
            print ("open interface json file fail!!!")
        '''
        pass

#任务
    @task(1)
    def getDeviceDiagramStst(self):
        u'''
        request_url:请求路径
        request_params:请求头参数
        request_json:请求json参数
        request_url = "http://172.16.42.74:8005/tsp/user/account/getHomePageData?accountId=95"
        request_url = "http://172.16.42.74:8005/tsp/message-center/userMessage/getUnReadMsgCount?accountId=95"
        request_url = "http://172.16.42.74:8005/tsp/user/user/get/95"
        request_url = "http://172.16.42.74:8005/tsp/location/findAllLocationListWithPage?deviceId=ZHANGHAILONG00002&deviceType=VEHICLE&endTime=1535644800000&pageIndex=1&pageSize=500&startTime=1535558400000"
        request_url = "http://172.16.42.74:8005/tsp/continental-gateway/continental-gateway/reportDataUpdate"
        request_url = "http://114.115.185.200:8005/tsp/continental-gateway/continental-gateway/realTimeUploadData"
		'''

        request_url = "http://172.16.42.11:2000/user/get/95"
        try:
            response = self.client.get(url=request_url, timeout=1800)
        except(UnboundLocalError):
            print("interface file")
        response_text = json.loads(response.text)["status"]
        if response.status_code != 200 and response_text != "SUCCEED":
            print ("返回内容：%s"%(response.text))
            print ("返回异常,请求状态码：%s"%(response.status_code))
        elif response.status_code == 200 and response_text == "SUCCEED":
            print ("返回成功")

        '''
        request_url = "http://172.16.42.74:8005/tsp/yqjf-report/statistics/runReport/getDeviceDiagramStst"
        request_params = {"Content-type": "application/json"}
        request_json = {
            "vehId": "ZZZZZZZAAAAAAAAA1",
            "tokenId": "56r9T5tB17JR1F8zRmXxZZzzXhrYwYqH",
            "period": {
                "from": "2018-09-01 00:00:00",
                "to": "2018-09-30 23:59:59"
            }
        }
        try:
            response = self.client.post(url=request_url, headers=request_params, data=json.dumps(request_json))
        except(UnboundLocalError):
            print("json fail")
        response_text = json.loads(response.text)["isSuccess"]
        if response.status_code != 200 and response_text != 0:
            print ("返回内容：%s"%(response.text))
            print ("返回异常,请求状态码：%s"%(response.status_code))
        elif response.status_code == 200 and response_text == 0:
            print ("返回成功")
		'''

#性能测试配置
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #请求响应时间
    min_wait = 120000
    max_wait = 120000
    host = "http://172.16.42.74:8005/"