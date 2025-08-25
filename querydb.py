from website.models import User

email="sn@gmail.com"

user = User.query.filter_by(email=email).first()
print(user)