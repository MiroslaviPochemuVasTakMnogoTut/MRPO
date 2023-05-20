from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import xml.etree.ElementTree as ET
from lxml import etree
import json
# import requests

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
    @abstractmethod
    def update(self, entity):
        pass

class SQLRepository(Repository):
    def __init__(self, session, model_class):
        self.model_class = model_class
        self.session = session


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

class XMLRepo(Repository):
    def __init__(self, tree: ET.ElementTree):
        self.db_file ='3/db.xml'
        self.tree = tree
        self.root = self.tree.getroot()
        # with open('3/db.xml', 'rb') as file:
        #     xml = file.read()
        # self.xtree = etree.fromstring(xml)
    
    def add(self, item:dict, table_name='waiters'):
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
        
    def remove(self, id, table_name:str='waiters'):
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
            
    
    def update(self, id, nitem:dict, table_name='waiters'):
        upd:ET.Element = self.get_by_id(id, table_name)
        for fld in nitem.keys():
            ufield = upd.find(f'./field[@name="{fld}"]')
            ufield.text = nitem[fld]
        self.tree.write('waiters1.xml')
        
        
    def get_all(self, table_name='waiters'):
        items = []
        for item in self.root.findall(f'./table[@name="{table_name}"]/row'):
            waiter ={}
            for wtr in item:
                waiter[wtr.attrib['name']] = wtr.text
            items.append(waiter)
                
        return items
            
    def get_by_id(self, id, table_name='waiters')->ET.Element:
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


class JsonRepo(Repository):
    def __init__(self, filename='db.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=2)

    def add(self, item):
        # Генерируем уникальный идентификатор для элемента
        id = str(max([int(i['id']) for i in self.data['database']['tables']['waiters']])+1)
        item['id'] = id
        self.data['database']['tables']['waiters'].append(item)
        self.save()

    def remove(self, id):
        self.data['database']['tables']['waiters'] = [x for x in 
                                                      self.data['database']
                                                               ['tables']
                                                               ['waiters'] if x['id'] != id]
        self.save()

    def get_all(self):
        # Получение всех элементов из репозитория
        return self.data['database']['tables']['waiters']

    def get_by_id(self, id):
        # Получение элемента по его идентификатору
        return next((x for x in self.data['database']['tables']['waiters'] if x['id'] == id), None)

    def update(self, entity):
        # Обновление элемента в репозитории
        # entity - объект, который нужно обновить
        self.remove(entity['id'])
        self.data['database']['tables']['waiters'].append(entity)
        # for item in self.data['database']['tables']['waiters']:
        #     if item['id'] == entity['id']:
        #         item = entity
        #         self.save()
        #         return True
        return False

class FakeRepo(Repository):
    def __init__(self, base=[]):
        self.base = base
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