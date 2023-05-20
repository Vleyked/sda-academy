from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

USER = "root"
PASSWORD = "root"
HOST = "localhost"
DB = "store"

# Step 1: Create the database engine
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DB}")

# Step 2: Define the database models
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))


class Product(Base):
    __tablename__ = "products2"
    product_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Integer)
    description = Column(String(255))


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    order_date = Column(String(255))
    customer = relationship("Customer")


class OrderItem(Base):
    __tablename__ = "order_items"
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, ForeignKey("products2.product_id"))
    quantity = Column(Integer)
    order = relationship("Order")
    product = relationship("Product")


# Step 5: Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Exercise 8: Retrieve the products with their average price
# Tip: func.avg

product_avg_price = (
    session.query(Product, func.avg(Product.price)).group_by(Product).all()
)
for product, avg_price in product_avg_price:
    print(f"Product: {product.name}, Average Price: {avg_price}")

# subquery = session.query(func.avg(Product.price)).subquery()
# print(subquery)
session.close()
