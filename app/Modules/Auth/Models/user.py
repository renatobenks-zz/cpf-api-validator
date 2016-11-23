from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context


from app import app
from app.Modules.Auth import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        secret_key = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return secret_key.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        secret_key = Serializer(app.config['SECRET_KEY'])
        try:
            data = secret_key.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user
