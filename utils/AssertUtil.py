from utils.LogUtil import my_log
import json
#1、定义封装类
class AssertUtil:
#2、初始化数据，日志
    def __init__(self):
        self.log = my_log("AssertUtil")
#3、code相等
    def assert_code(self,code,expected_code):
        """
        验证返回状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is %s,expected_code is %s"%(code,expected_code))

            raise
#4、body相等
    def assert_body(self,body,expected_body):
        """
        验证返回结果内容相等
        :param body:
        :param expected_body:
        :return:
        """
        try :
            assert body == expected_body
            return True
        except:
            self.log.error("body error,body is %s,expected_body is %s"%(body,expected_body))
            raise
#5、body包含
    def assert_in_body(self,body,expected_body):
        """
        验证返回结果是否包含期望的结果
        :param body:
        :param expected_body:
        :return:
        """
        try:
            # body = json.dumps(body)
            assert expected_body in body
            return True
        except:
            self.log.error('%s %s '%(type(body), type(expected_body)))
            self.log.error("不包含或者body是错误，body is %s,expected_body is %s"%(body,expected_body))
            raise


if __name__ == '__main__':
    str1 =str ({'nickname': '1号超级管理员', 'ret': 0, 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEsInVzZXJuYW1lIjoiYnloeSIsImV4cCI6MTcwNDAwNzU0N30.Cuo6RE1a3wumwBP1yXihN3YiaxGAbGVLB_XT-fUCvtE'})
    str2 = "'nickname': '1号超级管理员'"
    assert_util = AssertUtil()
    assert_util.assert_in_body(str1,str2)
    print(2)
    import pickle
    pickle.dump