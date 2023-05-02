from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import xml.etree.ElementTree as ET
from lxml import etree


Base = declarative_base()
 
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

class SQLRepository(Repository):
    def __init__(self, model_class):
        self.model_class = model_class
        engine = create_engine('postgresql://postgres:123@127.0.0.1:15432/WP')
        Base.metadata.create_all(engine)
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


    def remove(self, entity):
        self.session.delete(entity)
        self.session.commit()

class XMLWaiter(Repository):
    def __init__(self, model_class):
        with open('3/waiters.xml', 'rb') as file:
            xml = file.read()
        self.tree = ET.parse('3/waiters.xml')
        self.root = self.tree.getroot()
        self.xtree = etree.fromstring(xml)
    
    def add(self, entity):

        xpath_expr = "//id"
        ids = self.xtree.xpath(xpath_expr)
        lids = [int(i.text) for i in ids]
        # Создать новый элемент
        nw = ET.SubElement(self.root, 'waiter')
        ids = self.xtree.xpath('//id')
        id  = ET.SubElement(nw, 'id')
        nam = ET.SubElement(nw, 'name')
        bd = ET.SubElement(nw, 'birthdate')
        id.text = str(max(lids)+1)
        nam.text = entity.name
        bd.text = entity.birthdate
        # nw.set('id',        f'{max(lids)+1}')
        # nw.set('name',      f'{entity.name}')
        # nw.set('birthdate', f'{entity.birthdate}')
        # Записать изменения в файл
        self.tree.write('waiters1.xml')
        
    def remove(self, id):
        xpath_expr = "//id"
        ids = self.xtree.xpath(xpath_expr)
        lids = [int(i.text) for i in ids]
        if id in lids:
            fired = self.root.find(f'./waiter[id="{id}"]')
            self.root.remove(fired)
        # else:
            
    
    
    def update(self, entity):
        waiter = self.root.find(f"./waiter[id='{entity.id}']")
        waiter.find('name').text = entity.name
        waiter.find('birthdate').text = entity.birthdate
        self.tree.write('waiters1.xml')
        
        
    def get_all(self):
        al = []
        for w in self.root:
            id = int(w.find('id').text)
            name = w.find('name').text
            birthdate = w.find('birthdate').text
            
    def get_by_id(self, id):
        pass
    
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