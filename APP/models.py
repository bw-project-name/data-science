from flask_sqlalchemy import SQLAlchemy  
DB = SQLAlchemy()

class user(DB.Model):
    """ Spotify Artist """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(25), nullable=False)
    new_artist = DB.Column(DB.BigInteger)

    def __repr__(self):
        return 'User {}'.formar(self.name)


class songs(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    artist_id = DB.Column(DB.BigInteger, DB.ForeignKey('artist_id'), nullable=False)
    artist = DB.relationship('User', backref=DB.backref('artist', lazy=True))

    def __repr__(self):
        return '[Artist {}]'.format(self.text)
    