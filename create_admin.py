from admin.model import AdminLogin
from utils.passwd import Password

from create_app import db



password  = "123456789"

admin = AdminLogin(user="admin", password=Password.hash_password(password))
db.session.add(admin)
db.session.commit()
