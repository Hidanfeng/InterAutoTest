import allure
import requests

from  utils.LogUtil import my_log
from config import Conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
log = my_log('devicetype')

'''
/api/operator/devicetype/list
'''

test_file_path = os.path.join(Conf.get_data_path(),'divoiecs_list.yml')
divoiecs_data = YamlReader(test_file_path).data_all()

@pytest.mark.parametrize("divoiecs",divoiecs_data)
def test_divoiecslist(divoiecs,get_token):
    url = ConfigYaml().get_conf_url()+divoiecs['url']
    headers = get_token
    data = divoiecs['data']
    res = requests.get(url=url, headers=headers, json=data).json()
    log.debug(f'接口返回 {res}')
    print(res["retlist"][0]["name"])

    # allure
    # sheet名称  feature 一级标签
    allure.dynamic.feature(divoiecs['case_name'])
    # # 模块   story 二级标签
    # allure.dynamic.story(divoiecs['case_name'])
    # # 用例ID+接口名称  title
    # allure.dynamic.title(divoiecs['case_name'])
    # 请求URL  请求类型 期望结果 实际结果描述
    desc = "<font color='red'>请求URL: </font> {}<Br/>" \
           "<font color='red'>期望结果: </font>{}<Br/>" \
           "<font color='red'>实际结果: </font>{}".format(url, divoiecs['expect']['name'], res)
    allure.dynamic.description(desc)


    assert divoiecs['expect']['name'] == res['retlist'][0]['name']



