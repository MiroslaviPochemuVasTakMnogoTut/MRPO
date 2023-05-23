# from data.repository import SQLRepository, XMLRepo
# from data.modelDB.waiterDB import WaiterDB
# from logic.usecase import WaiterToXML
# from flask import Flask, request
# from logic.usecase import *
# from data.uow import XMLUoW, SqlUoW, JsonUoW
from model.models import Waiter
from data.factory import *

# app = Flask(__name__)

# @app.route('/api/all', methods=["GET"])
# def get_all():
#     uow = JsonUoW()
#     # uow = SqlUoW(WaiterDB)
#     return get_waiters(uow)

# @app.route('/api/add', methods=["POST", "GET"])
# def add():
#     if request.method == 'POST':
#         # wtr = Waiter(request.json['name'], request.json['birthdate'])
#         # wtr.phone = request.json['phone']
#         add_waiter(request.json, JsonUoW()) 
#     return str(request)
# @app.route('/api/rem', methods=["POST"])
# def remove():
#     if request.method == 'POST':
#         remove_waiter(request.json['id'], JsonUoW())
        
# @app.route('/api/upd', methods=["POST"])        
# def update():
#     if request.method == 'POST':
#         print(request.json)
#         update_waiter(request.json, JsonUoW())
#         return '  '
        
# def main():
#     waiter1 = Waiter("John","2000-01-01")
#     waiter2 = Waiter("Mike","2000-01-01")
#     # service = WaiterToXML()
#     # service.add("John", "2001-01-01")``
#     wmod1 = WaiterDB(waiter1)
#     wmod2 = WaiterDB(waiter2)
#     repo = SQLRepository(WaiterDB)
#     repo.add(wmod1)
#     repo.add(wmod2)
#     wmod3 = repo.get_by_id(1)
#     wmod3.name = 'Sghrek'
#     repo.update(wmod3)



if __name__=='__main__':
    # main()
    # app.run(debug=True)
    seri = SerializerFactory().serialize('json')
    wtr = Waiter('Joe', '2011-12-12')
    print(wtr.serialize(seri))
    
    