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
        self.db_file ='3/db.xml'
        with open('3/db.xml', 'rb') as file:
            xml = file.read()
        self.tree = ET.parse('3/db.xml')
        self.root = self.tree.getroot()
        self.xtree = etree.fromstring(xml)
    
    def add(self, item:dict, table_name):
        new_item = ET.Element('row')
        table = self.root.find(f'./table[@name="{table_name}"]')
        ids = table.findall('row/field[@name="id"]')
        nid = max([int(i.text) for i in ids]) + 1
        xid = ET.SubElement(new_item, 'field')
        xid.set('name', 'id')
        xid.text = str(nid)
        for atr in item.keys():
            at =ET.SubElement(new_item, 'field')
            at.set('name', atr)
            at.text = item[atr]
        # print(item.keys())
        table.append(new_item)
        self.tree.write('waiters1.xml')
        
    def remove(self, id, table_name:str):
        items = self.root.find(f'./table[@name="{table_name}"]')
        # fired = items.find(f'./row[field[@name="id"]="1"]')
        fired = None
        for item in items:
            if (fired is not None):
                break
            fids = item.findall(f'./field[@name="id"]')
            for fid in fids:
                # print(fid.text)
                if int(fid.text) == id:
                    fired = item
                    break
                else:
                    return False
        items.remove(fired)
        self.tree.write('waiters1.xml')
        return True
            
    
    
    def update(self, id, nitem:dict, table_name):
        upd:ET.Element = self.get_by_id(id, table_name)
        for fld in nitem.keys():
            ufield = upd.find(f'./field[@name="{fld}"]')
            ufield.text = nitem[fld]
        self.tree.write('waiters1.xml')
        
        
    def get_all(self, table_name):
        items = []
        for item in self.root.findall(f'./table[@name="{table_name}"]/row'):
            waiter ={}
            for wtr in item:
                waiter[wtr.attrib['name']] = wtr.text
            items.append(waiter)
                
        return items
            
    def get_by_id(self, id, table_name)->ET.Element:
        items = self.root.find(f'./table[@name="{table_name}"]')
        # fired = items.find(f'./row[field[@name="id"]="1"]')
        fnd = None
        for item in items:
            if (fnd is not None):
                break
            fids = item.findall(f'./field[@name="id"]')
            for fid in fids:
                # print(fid.text)
                if int(fid.text) == id:
                    fnd = item
                    break
        return fnd 
    
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