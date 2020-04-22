from app import db


class Script(db.Model):
    __tablename__ = 'scripts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(200))
    path = db.Column(db.String(200))


    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id, self.name)
