import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file")

    print("Stuck at Engine")
    conn_str = 'sqlite:///' + db_file.strip()
    engine = sa.create_engine(conn_str, echo=False)
    print("Stuck at factory")
    factory = orm.sessionmaker(bind=engine)
    print("Stuck at metadata")
    from data.packages import Package
    SqlAlchemyBase.metadata.create_all(engine)
    print("finished")