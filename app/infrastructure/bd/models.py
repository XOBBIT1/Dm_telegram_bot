from datetime import datetime

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    users = "users"
    __tablename__ = users

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column("name", db.String)
    username = db.Column("username", db.String)
    chat_id = db.Column("chat_id", db.BigInteger)
    user_status = db.Column("user_status", db.String, default="common")
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    last_seen = db.Column(db.TIMESTAMP, default=datetime.now())


class Product(Base):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String, nullable=False)
    description = db.Column("description", db.Text)
    price = db.Column("price", db.Numeric(10, 2), nullable=False)
    image_url = db.Column("image_url", db.String)
    category = db.Column("category", db.String)
    is_available = db.Column(db.Boolean, default=True)


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column("code", db.String, unique=True, nullable=False)
    discount_percent = db.Column(db.Integer, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)


class Order(Base):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))
    products = db.Column(db.JSON)
    total_price = db.Column(db.Numeric(10, 2))
    status = db.Column("status", db.String, default="pending")
    created_at = db.Column(db.DateTime, default=datetime.now())

    user = relationship("User")
