import requests

class HttpRequest:
    """
    利用request封装get和post请求
    """
    def http_request(self,url,data,method,cookie=None):
        """"
        url
        method
        """
        if method.lower()=="get":#lower统一变换成小写
            res = requests.get(url,data, cookies=cookie,verify=False)  # 响应结果的消息实体
            return res #返回一个消息实体
        elif method.lower()=="post":
            res=requests.post(url,data,cookies=cookie,verify=False)#响应结果的消息实体
            return res #返回一个消息实体

 
if __name__ == '__main__':
    url="https://www.vipzhonglian.com/index/login/"
    data={"uname":"17701583363","upwd":"583363"}
    res1=HttpRequest().http_request(url,data,"post")
    # print("第一个接口测试的结果",res1.text)
    print("响应头:",res1.headers)#获取的是响应头
    print("状态码:",res1.status_code)
    # print("代理user-agent：",res1.request.headers)#获取的是请求头
    # print("响应正文：",res1.text,"类型",type(res1.text))





# url="https://www.baidu.com/"
# # data={"":"","":""}/
# header={'User-Agent': '6666'}#伪装User-Agent
#
# res=requests.get(url,headers=header)#返回消息实体
# print(res)
# print("响应头:",res.headers)#获取的是响应头
# print("状态码:",res.status_code)
# print("响应正文：",res.text,type(res.text))
# print("代理user-agent：",res.request.headers)#获取的是请求头
# print("代理user-agent：",res.headers)#获取的是响应头



