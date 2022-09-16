from flask import Flask, jsonify
from dataclasses import dataclass
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, CheckConstraint
from flask_migrate import Migrate
import requests
from sqlalchemy.sql import text

from producer import publish


# def pubish(method, body):
#     pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db-main/main'
CORS(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
###
# file name has to be app.py
# flask db init
# flask db migrate
# flask db upgrade
###


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)


@app.route('/api/products/')
def index():
    query = Product.query.all()
    CheckConstraint
    return jsonify(query)


@app.route('/api/products/<int:id>/like/', methods=['POST'])
def like(id):
    req = requests.get("http://docker.for.mac.localhost:8000/api/user/")
    req_userid = str(req.json()['id'])  # have to be str to use in query
    print(type(req_userid))
    product_id = str(id)
    data = dict(user_id=req_userid, product_id=product_id)
    statement = text("""SELECT count(*) FROM main.product_user 
                     WHERE user_id = :user_id and product_id = :product_id;""")
    print(data)
    with db.engine.connect() as con:
        result = con.execute(statement, data)  # return ? object
        # print(result.first()[0]) # get only result -> 0
        like = result.first()[0]

    productUser = ProductUser(user_id=data['user_id'], product_id=data['product_id'])

    if not like:
        db.session.add(productUser)
        db.session.commit()
        publish('product_like_add', data)
        return jsonify({
            'message': 'add like, completed'
        })
    else:
        db.session.query(ProductUser)\
            .filter(ProductUser.user_id == data['user_id'])\
            .filter(ProductUser.product_id == data['product_id']).delete()
        db.session.commit()
        publish('product_like_remove', data)
        return jsonify({
            'message': 'remove like, completed'
        })


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
