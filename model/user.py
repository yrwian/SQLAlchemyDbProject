from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    # 表名称
    __tablename__ = 'user'
    # news表里id字段
    id = Column(Integer, primary_key=True, autoincrement=True, )

    # news表里title字段
    city_name = Column(String(length=255), nullable=True)

    def droptable(self):
        Base.metadata.drop_all()

    def createtable(self, engine):
        Base.metadata.create_all(engine)

    def tojson(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
