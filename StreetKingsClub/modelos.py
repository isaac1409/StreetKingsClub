from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    __tablename__ = "Usuarios"
    id: int = Field(default=None, primary_key=True)
    Nombre: str
    Username: str
    Password: str

