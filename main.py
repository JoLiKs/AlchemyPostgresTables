from sqlalchemy import create_engine, MetaData, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing.schema import Table, Column

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/postgres")
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

class MyTable:

    def __init__(self, *args):
        self.table = Table(self.__class__.__name__, metadata,
                 Column('id', Integer(), primary_key=True),
            *[Column(i, String(200), nullable=False) for i in args],
                 )

class Customer(MyTable):

    def __init__(self, *args):
        super().__init__(*args)

        
c = Customer(
    'name',
    'mail'
)


class Users(MyTable):

    def __init__(self, *args):
        super().__init__(*args)


users = Users(
    'name',
    'username',
    'password'
)

metadata.create_all(engine)

