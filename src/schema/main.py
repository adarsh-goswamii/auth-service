from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def import_schemas():
    import src.schema.auth_code
    import src.schema.user
    import src.schema.client
    import src.schema.application