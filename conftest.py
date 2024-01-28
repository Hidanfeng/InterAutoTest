import pytest
import requests
from config.Conf import ConfigYaml


@pytest.fixture(scope='session', autouse=True)
def get_token():
    url = ConfigYaml().get_conf_url()+"/api/operator_login"
    data = {'username': 'byhy', 'password': 'sdfsdf'}
    s = requests.Session()
    respon = s.post(url=url,json=data).json()
    # print(type(respon))

    token = respon.get('token')
    headers = {'Authorization': 'Bearer '+ token}
    return headers




