from . import db

class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    propertytitle = db.Column(db.String)
    numberofbedrooms = db.Column(db.Integer)
    numberofbathrooms = db.Column(db.Integer)
    location = db.Column(db.String)
    price = db.Column(db.Float)
    description  = db.Column(db.String)
    propertype = db.Column(db.String)
    photo=  db.Column(db.String)



    def __init__(self,propertytitle,numberofbedrooms,numberofbathrooms,location, price, description, propertype,photo ):
        self.propertytitle = propertytitle
        self.numberofbedrooms = numberofbedrooms
        self.numberofbathrooms = numberofbathrooms
        self.location = location
        self.price= price
        self.description = description
        self.propertype = propertype
        self.photo = photo