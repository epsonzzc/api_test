import unittest
from api.user_manager import  UserManager

class TestUserManagerCase(unittest.TestCase):

    user_id = None


    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        cls.username = cls.password = 'test95277'
        cls.new_username = cls.new_password = 'xxxx95277'
    # case1：只输入用户名和密码进行添加管理员
    def test01_normal_add(self):

        # 定义测试用例数据
        # username = 'test9527'
        # password = 'test9527'

        # 1)请求添加管理员接口
        actual_result = self.user.add_user(self.username,self.password)
        print(actual_result)
        if actual_result.get('data'):
            TestUserManagerCase.user_id = actual_result.get('data').get('id')

        # 2)对返回数据进行校验
        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.username,actual_result.get('data').get('username'))


    # case2 : 编辑用户
    def test02_edit(self):
        # new_username = 'xxxx9527'
        # new_userpassword = new_username
        actual_result = self.user.edit_user(TestUserManagerCase.user_id,self.new_username,self.new_password)

        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.new_username,actual_result['data']['username'])

    # case3 : 查询用户
    def test03_search(self):

        actual_result = self.user.search_user()

        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.new_username,actual_result.get('data').get('list')[0].get('username'))

    # case4 : 删除测试用例
    def test04_delete(self):
        # 1. 定义测试用例数据

        # 2. 调用被测接口
        actual_result = self.user.del_user(TestUserManagerCase.user_id)

        # 3. 断言
        self.assertEqual(0,actual_result['errno'])



if __name__ == '__main__':
    unittest.main()