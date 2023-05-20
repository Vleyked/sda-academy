from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
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
    __tablename__ = "products"
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
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    order = relationship("Order")
    product = relationship("Product")


# Step 3: Drop the tables if they exist
Base.metadata.drop_all(engine)

# Step 4: Create the database tables
Base.metadata.create_all(engine)

# Step 5: Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Step 6: Perform database operations
# Create customers
customer1 = Customer(name="John Doe", email="john@example.com", address="123 Main St")
customer2 = Customer(name="Jane Smith", email="jane@example.com", address="456 Oak St")
session.add_all([customer1, customer2])
session.commit()

# Create products
product1 = Product(name="Product A", price=10, description="Description for Product A")
product2 = Product(name="Product B", price=20, description="Description for Product B")
session.add_all([product1, product2])
session.commit()

# Crete order
order1 = Order(customer_id=customer1.customer_id, order_date="2023-01-01")
order2 = Order(customer_id=customer2.customer_id, order_date="2023-02-01")
session.add_all([order1, order2])
session.commit()

# Crete order item
order_item1 = OrderItem(
    order_id=order1.order_id, product_id=product1.product_id, quantity=2
)
order_item2 = OrderItem(
    order_id=order1.order_id, product_id=product2.product_id, quantity=3
)
order_item3 = OrderItem(
    order_id=order2.order_id, product_id=product1.product_id, quantity=1
)
session.add_all([order_item1, order_item2, order_item3])
session.commit()

# Querying records

# Get all customers
customers = session.query(Customer).all()
for customer in customers:
    print(
        f"Customer: {customer.name}, Email: {customer.email}, Address: {customer.address}"
    )

# Get all products
products = session.query(Product).all()
for product in products:
    print(
        f"Product: {product.name}, Price: {product.price}, Description: {product.description}"
    )

# Get all orders with customer information
orders = session.query(Order).join(Customer).all()
for order in orders:
    print(
        f"Order ID: {order.order_id}, Customer: {order.customer.name}, Date: {order.order_date}"
    )

# Get all order items with product information
order_items = session.query(OrderItem).join(Product).all()
for order_item in order_items:
    print(
        f"Order Item ID: {order_item.order_item_id}, Product: {order_item.product.name}, Quantity: {order_item.quantity}"
    )

# Step 7: Close the session
session.close()
