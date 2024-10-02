from sqlmodel import create_engine, Session

DATABASE_URL = "mysql+mysqlconnector://u502766237_changotartario:Tartarios*99@193.203.166.209:3306/u502766237_StreetKings"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)
