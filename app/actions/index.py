from app.models import pr_users
from app import db


def users_page():

    all_users = db.session.query(pr_users).all()

    def get_all_users(all_users):
        lst = []
        for i in all_users:
            lst.append(row2dict(i))
        return lst

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d

    db_users = get_all_users(all_users)

    return db_users

