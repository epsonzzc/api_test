from api.base import Base

# 主要用于关于系统管理员的接口

class UserManager(Base):

    def __init__(self):
        self.add_user_path = "/admin/admin/create"
        self.edit_user_path = "/admin/admin/update"
        self.del_user_path = "/admin/admin/delete"
        self.search_user_path = "/admin/admin/list?page=1&limit=20&sort=add_time&order=desc"

    # 添加管理员
    def add_user(self,username,password,**kwargs):
        user_data = {'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
        user_url = self.get_url(self.add_user_path)
        return self.post(user_url,user_data)

    # 修改管理员
    def edit_user(self,id,username,password,**kwargs):
        user_data = {'id':id,'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
        user_url = self.get_url(self.edit_user_path)
        return self.post(user_url,user_data)

    # 删除管理员
    def del_user(self,id,**kwargs):
        user_data = {'id':id}
        if kwargs:
            user_data.update(**kwargs)
        user_url = self.get_url(self.del_user_path)
        return self.post(user_url, user_data)

    # 查询管理员
    def search_user(self):
        user_url = self.get_url(self.search_user_path)
        return self.get(user_url)
