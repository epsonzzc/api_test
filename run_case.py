from HTMLTestRunner import HTMLTestRunner
import unittest
from setting import TEST_REPORT_PATH,LOGIN_INFO
from api.user_manager import UserManager



if __name__ == '__main__':
    user = UserManager()
    user.login(LOGIN_INFO.get('username'),LOGIN_INFO.get('password'))

    suite = unittest.TestLoader().discover('./case','test*.py')

    with open(TEST_REPORT_PATH,'wb') as f:

        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)