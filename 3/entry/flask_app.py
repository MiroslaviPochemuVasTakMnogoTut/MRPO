from flask import Flask, request
from logic.usecase import get_waiters
from data.uow import XMLUoW
app = Flask(__name__)

@app.route('/api/all', methods=["GET"])
def get_all():
    uow = XMLUoW()
    return get_waiters(uow)
# @app.route('/api/', methods=["POST"])
# def q():
#     pass
# @app.route('/api/', methods=["POST"])
# def a():
#     pass
# @app.route('/api/', methods=["POST"])
# def a():
#     pass
# @app.route('/api/', methods=["POST"])
# def a():
#     pass

if __name__ == '__main__':
    app.run(debug=True)
