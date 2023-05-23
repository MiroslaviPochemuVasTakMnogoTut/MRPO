from data.repository import *
from data.uow import *
import json
import xml.etree.ElementTree as et


class RepositoryFactory:
    def repositize(self, format):
        repositizer = get_repositizer(format)
        return repositizer()

class SerializerFactory:
    def serialize(self, format):
        serializer = get_serializer(format)
        return serializer

class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)

def get_serializer(format: str):
    if format.lower() == 'xml':
        return XmlSerializer()
    elif format.lower() == 'json':
        return JsonSerializer()
    
class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


def get_repositizer(format: str):
    if format.lower() == 'json':
        return _json_repositizer
    elif format.lower() == 'xml':
        return _xml_repositizer
    elif format.lower() == 'sql':
        return _sql_repositizer
    else:
        return ValueError('Invalid format')




def _json_repositizer():
    return JsonRepo()
    # uow = JsonUoW()
    # with uow:
    #     uow.repo.add(waiter)


def _xml_repositizer():
    return XMLRepo()


def _sql_repositizer():
    return SQLRepository()

    # uow = XMLUoW()
    # with uow:
    #     uow.repo.add(waiter)
