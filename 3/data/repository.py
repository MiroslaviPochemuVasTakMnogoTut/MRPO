from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


 
class Repository(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def add(self, item):
        pass
    @abstractmethod
    def remove(self, item):
        pass
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass

class SQLRepository:
    def __init__(self, model_class):
        self.model_class = model_class
        engine = create_engine('postgresql://postgres:123@127.0.0.1:15432/WP')
        Session = sessionmaker(bind=engine)
        self.session = Session() # UoW


    def get_all(self):
        return self.session.query(self.model_class).all()

    def get_by_id(self, id):
        return self.session.query(self.model_class).filter_by(id=id).first()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def update(self, entity):
        db_entity = self.get_by_id(entity.id) # находим сущность в базе данных
        # обновляем данные в объекте db_entity на основе данных из entity
        db_entity = entity
        # сохраняем изменения
        self.session.commit()


    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()


class FakeRepo(Repository):
    def __init__(self):
        self.base = []
        pass
    def add(self, item):
        self.base.append(item)
    def remove(self, item):
        self.base.remove(item)
    def get_all(self):
        return self.base
    def get_by_id(self, id):
        return self.base[id]


# def create_db_connection():
#     db_user     = "postgres"
#     db_password = "123"
#     db_host     = "localhost"
#     db_port     = "15432"
#     db_name     = "WP"
#     db_url      = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
#     engine      = create_engine(db_url)
#     # Session = sessionmaker(bind=engine)
#     # return Session()
#     return engine.connect()