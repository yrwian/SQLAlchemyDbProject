from sqlalchemy import create_engine
# 连接本地test数据库
from sqlalchemy.orm import sessionmaker

from model.user import User

'数据库管理工具'


class DbManager:
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8", echo=False)
    # 创建会话
    session = sessionmaker(engine)
    mySession = session()

    '创建表格'

    def createtable(self):
        User().createtable(self.engine)

    '添加数据'

    def addUser(self, city: User):
        self.mySession.add(city)
        self.mySession.commit()

    '添加数据集合'

    def addUsers(self, citys):
        self.mySession.add_all(citys)
        self.mySession.commit()

    '查询结果集'

    def query(self):
        results = self.mySession.query(User).all()
        result = []
        for city in results:  # type: User
            result.append(city.tojson())
        return result

    '查询结果集'

    def queryByKeywords(self, keywords):
        results = self.mySession.query(User).filter(
            User.city_name.like('%%%s' % keywords + '%')).all()
        result = []
        for city in results:  # type: User
            result.append(city.tojson())
        return result

    '查询结果集'

    def query(self):
        results = self.mySession.query(User).all()
        result = []
        for city in results:  # type: User
            result.append(city.tojson())
        return result

    '删除所有数据'

    def clearAll(self):
        results = self.mySession.query(User).filter(User.id > 0).all()
        for city in results:  # type: User
            self.mySession.delete(city)

    def close(self):
        self.mySession.close()
        self.engine.dispose()


if __name__ == '__main__':
    manager = DbManager()

    # 创建表格
    manager.createtable()

    # 清空表格
    manager.clearAll()
    # 插入数据
    manager.addUser(User(city_name="你好"))

    # 批量插入数组
    users = [User(city_name="用户1"), User(city_name="用户2")]
    # 批量插入数组
    manager.addUsers(users)

    # 查询对象
    query = manager.queryByKeywords("用户1")
    print(query)
