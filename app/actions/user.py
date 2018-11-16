from app import db
from app.models import pr_users


def create_user(name, phone, email=None, role=1, password=None):

    if not role and password:

        role = 1
        user = pr_users(prus_name=name,
                        prus_email=email,
                        prus_phone=phone,
                        prus_role_id=role,
                        prus_password_hash=password)
        db.session.add(user)
        db.session.commit()
        return user

    elif role and password:

        user = pr_users(prus_name=name,
                        prus_email=email,
                        prus_phone=phone,
                        prus_role_id=role,
                        prus_password_hash=password)
        db.session.add(user)
        db.session.commit()
        return user

    else:
        return False

