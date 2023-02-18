from bd import app, db, ma

class Articulo(db.Model):
    __tablename__ = 'articulo'
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column(db.String(20),unique = True)
    Precio = db.Column(db.Float())

    def __init__(self, nombre, precio):
        self.Nombre = nombre
        self.Precio = precio

       
with app.app_context():
    db.create_all()


class ArticuloSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre','Precio')
