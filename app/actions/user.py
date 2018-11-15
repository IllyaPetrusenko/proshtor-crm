from app import db
from app.models import pr_users


class User:

    def __init__(self, username, phone, email, role):
        self.username = username
        self.phone = phone
        self.email = email
        self.role = role

    def create_user(self):

        db.session.add(pr_users(prus_name=self.username,
                                prus_phone=self.phone,
                                prus_email=self.email,
                                prus_role_id=self.role))
        db.session.commit()

        return True

    def edit_user(self):
        pass

    def delete_user(self):
        pass