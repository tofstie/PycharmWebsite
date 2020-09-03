import sqlalchemy as sa
from data.modelbase import SqlAlchemyBase


class Package(SqlAlchemyBase):
    __tablename__ = 'data'

    data_date = sa.Column(sa.DateTime, primary_key=True)
    TNG_data = sa.Column(sa.Integer)
    MC_data = sa.Column(sa.Integer)

    def __repr__(self):
        return '<Package {}>'.format(self.data_date)
