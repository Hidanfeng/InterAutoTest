import allure

from config import Conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
#1、获取测试用例内容list
#获取testlogin.yml文件路径
test_file = os.path.join(Conf.get_data_path(),"testlogin.yml")
#print(test_file)
#使用工具类来读取多个文档内容
data_list = YamlReader(test_file).data_all()
# print(data_list)
#2、参数化执行测试用例

@pytest.mark.parametrize("login",data_list)
def test_yaml(login):
    #初始化url,data
    url = ConfigYaml().get_conf_url()+login["url"]
    # print("url %s"%url)
    data = login["data"]
    # print("data %s"%data)
    #post请求
    request = Request()
    res  = request.post(url,json=data)
    # print(request.Session)

    # allure
    # sheet名称  feature 一级标签
    allure.dynamic.feature(login['case_name'])
    # # 模块   story 二级标签
    # allure.dynamic.story(divoiecs['case_name'])
    # # 用例ID+接口名称  title
    # allure.dynamic.title(divoiecs['case_name'])
    # 请求URL  请求类型 期望结果 实际结果描述
    desc = "<font color='red'>请求URL: </font> {}<Br/>" \
           "<font color='red'>期望结果: </font>{}<Br/>" \
           "<font color='red'>实际结果: </font>{}".format(url, login['expect'], res)
    allure.dynamic.description(desc)


    assert login['expect'] in str(res)
    #打印结果
    # print(res)

if __name__ == "__main__":
    pytest.main(["-s","test_login.py"])

