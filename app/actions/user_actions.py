from app import db
from app.models import pr_users


class CreateNewUser:

    def __init__(self, username, phone, email, role):
        self.username = username
        self.phone = phone
        self.email = email
        self.role = role

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_role(self):
        return self.role

    def add_new_user_2_db(self):

        new_user = pr_users(prus_name=self.get_username(),
                            prus_phone=self.get_phone(),
                            prus_email=self.get_email(),
                            prus_role_id=self.get_role())

        db.session.add(new_user)
        db.session.commit()
        return new_user


class DeleteSelectedUser:

    def __init__(self, id):
        self.id = id

    def delete_user(self):
        db.session.delete()