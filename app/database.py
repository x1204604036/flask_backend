from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import config


engine_str = "%s://%s:%s@%s:%s/%s?charset=utf8" % (
    config.MYSQL_CONNECT_TYPE,
    config.MYSQL_USERNAME,
    config.MYSQL_PASSWORD,
    config.MYSQL_HOST,
    config.MYSQL_PORT,
    config.MYSQL_DB_NAME,
)


engine = create_engine(engine_str)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)


Base = declarative_base()
Base.query = db_session.query_property()


def init_db(app):
    import app.models.user
    Base.metadata.create_all(bind=engine)
