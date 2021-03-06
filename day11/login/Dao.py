# DAO = Data Access Object
from day11.login import User

class UserDao:

    __users = [
        User('john', '1234'),
        User('mary', '5678')
    ]

    def find_user(self, username):
        for user in self.__users:
            if user.username == username:
                return user
        return None

    # 查詢
    def find_all_user(self):
        return self.__users

    # 新增
    def add_user(self, user):
        self.__users.append(user)
        print('新增成功')

    # 修改 password （Homework）
    def update_password(self, username, new_password):
        user = self.find_user(username)
        if user is not None:
            user.password = new_password
            print('密碼修改成功')
        else:
            print('密碼修改失敗')

    # 刪除 （Homework）
    def delete_user(self, user):
        self.__users.remove(user)
        print('刪除成功')