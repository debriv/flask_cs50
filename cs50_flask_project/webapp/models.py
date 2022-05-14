from datetime import datetime
from flask import current_app
from sqlalchemy import except_all
from webapp import db#, login_manager
from flask_login import UserMixin
import jwt
from datetime import datetime ,timedelta



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_stocks = db.relationship('User_stock', backref='author', lazy=True)


    # available_funds = db.Column(db.String(20), nullable=True)
class User_stock(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=True)
    stock_holding = db.Column(db.Integer, nullable= False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)


    def __repr__(self):
        return f"User_stock('{self.stock_id}','{self.date_posted}')"

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    code = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    buy_price = db.Column(db.String, nullable= False)
    sell_price =db.Column(db.String, nullable= False)
    stock_transacts = db.relationship('Stock_transact', backref='author2', lazy=True)
    user_stocks = db.relationship('User_stock', backref='author2', lazy=True)


class Stock_transact(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    code = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    quantity = db.Column(db.Integer, nullable= False)
    buy_price = db.Column(db.String, nullable= False)
    sell_price =db.Column(db.String, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"