from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from eapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # c4 = Category(name="Desktop")
        #
        # db.session.add_all([c1,c2,c3,c4])
        # db.session.commit()

        products = [{"id": 1,
                     "name": "iPad Pro 2020",
                     "description": "Apple, 128GB, RAM: 6GB",
                     "price": 3700000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 2},
                    {"id": 2,
                     "name": "Laptop",
                     "description": "Apple, 128GB, RAM: 6GB",
                     "price": 37000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 3},
                    {"id": 3,
                     "name": "Galaxy Note 10 Plus",
                     "description": "Samsung, 64GB, RAML: 6GB",
                     "price": 24000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 1},
                    {"id": 4,
                     "name": "iPad Pro 2020",
                     "description": "Apple, 128GB, RAM: 6GB",
                     "price": 37000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 2},
                    {"id": 5,
                     "name": "iPad Pro 2020",
                     "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 2},
                    {"id": 6,
                     "name": "Galaxy Note 10 Plus",
                     "description": "Samsung, 64GB, RAML: 6GB", "price": 24000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 1},
                    {"id": 7,
                     "name": "iPad Pro 2020",
                     "description": "Apple, 128GB, RAM: 6GB",
                     "price": 37000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 2},
                    {"id": 8,
                     "name": "iPad Pro 2020",
                     "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 2},
                    {"id": 9,
                     "name": "Galaxy Note 10 Plus",
                     "description": "Samsung, 64GB, RAML: 6GB", "price": 24000000,
                     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                     "category_id": 1}
                    ]
        for p in products:
            p1 = Product(name=p['name'], description=p['description'], price=p['price'],
                         image=p['image'], category_id=p['category_id'])
            db.session.add(p1)
        db.session.commit()
