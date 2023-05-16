from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data.repository import Repository, SQLRepository, FakeRepo, XMLRepo, JsonRepo
import xml.etree.ElementTree as ET
from lxml import etree

Base = declarative_base()
engine = create_engine('postgresql://postgres:123@127.0.0.1:15432/WP')
Base.metadata.create_all(engine)
DEFAULT_SESSION_FACTORY = sessionmaker(bind=engine)

class AbstractUoW(ABC):
    repo: Repository
    
    def __exit__(self, *args):
        self.rollback()
        
    @abstractmethod
    def commit(self):
        raise NotImplementedError
    
    @abstractmethod
    def rollback(self):
        raise NotImplementedError

class SqlUoW(AbstractUoW):
    def __init__(self,  model_class, session_factory=DEFAULT_SESSION_FACTORY):
        self.model_class = model_class
        self.session_factory = session_factory
        
    def __enter__(self):
        self.session = self.session_factory()
        self.repo = SQLRepository(self.session, self.model_class)
        # return super().__enter__()
    
    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()
        
    def commit(self):
        self.session.commit()
        
    def rollback(self):
        self.session.rollback()
        
XML_DB = '3/db.xml'        
class XMLUoW(AbstractUoW):
    def __init__(self, xmlfile=XML_DB):
        self.db_file = xmlfile
        
    def __enter__(self, *args):
        self.tree = ET.parse(self.db_file)
        self.copy = ET.parse(self.db_file)
        self.repo= XMLRepo(self.tree)
        # self.root = self.tree.getroot()
        # with open(self.db_file, 'rb') as file:
        #     xml = file.read()
        # self.xtree = etree.fromstring(xml)
        
    def __exit__(self, *args):
        super().__exit__(*args)
        self.tree.write(self.db_file)
    
    def commit(self):
        self.tree.write(self.db_file)
        
    def rollback(self):
        self.tree = self.copy


class JsonUoW(AbstractUoW):
    def __init__(self, file='3/db.json'):
        self.db_file = file
    
    def __enter__(self):
        self.repo = JsonRepo(self.db_file)
        # self.data = self.repo.load_data()
        
    def __exit__(self, *args):
        super().__exit__(*args)
        self.repo.save()
        
    def commit(self):
        self.repo.save()
        
    def rollback(self):
        pass
        
class FakeUoW(AbstractUoW):
    def __init__(self):
        self.repo = FakeRepo([])
        self.commited = False
        
    def commit(self):
        self.commited = True