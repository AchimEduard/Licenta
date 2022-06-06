from sqlalchemy import Column, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('postgresql://postgres:ParolaPentruLicenta123@serverpentrulicenta.postgres.database.azure.com:5432/postgres?sslmode=require', echo=True)
session = Session(engine, future=True)

class TrainRoutesAdults(Base):
    __tablename__ = 'TrainRoutesAdults'
    train_id = Column(String, primary_key=True)
    depart_station = Column(String, primary_key=True)
    arrival_station = Column(String, primary_key=True)
    cumpara = Column(String)
    date = Column(String)
    ora = Column(String)

    def __repr__(self):
        return 'Train_id: ' + str(self.train_id)


class TrainRoutesElev(Base):
    __tablename__ = 'TrainRoutesElev'
    train_id = Column(String, primary_key=True)
    depart_station = Column(String, primary_key=True)
    arrival_station = Column(String, primary_key=True)
    cumpara = Column(String)
    date = Column(String)
    ora = Column(String)


class TrainRoutesStudent(Base):
    __tablename__ = 'TrainRoutesStudent'
    train_id = Column(String, primary_key=True)
    depart_station = Column(String, primary_key=True)
    arrival_station = Column(String, primary_key=True)
    cumpara = Column(String)
    date = Column(String)
    ora = Column(String)



class TrainRoutesRetiree(Base):
    __tablename__ = 'TrainRoutesRetiree'
    train_id = Column(String, primary_key=True)
    depart_station = Column(String, primary_key=True)
    arrival_station = Column(String, primary_key=True)
    cumpara = Column(String)
    date = Column(String)
    ora = Column(String)


class TrainDetails(Base):
    __tablename__ = 'TrainDetails'
    train_id = Column(String, primary_key=True)
    depart_station = Column(String, primary_key=True)
    arrival_station = Column(String, primary_key=True)
    Durata = Column(String)
    PretStud = Column(Integer)
    PretPens = Column(Integer)
    PretEl = Column(Integer)
    Pret = Column(Integer)
    Locuri = Column(Integer)
    date = Column(String, primary_key=True)
    ora = Column(String)

    def __repr__(self):
        return 'Train_id: ' + str(self.train_id)


class LocuriOcupate(Base):
    __tablename__ = 'LocuriOcupate'
    train_id = Column(String)
    depart_station = Column(String)
    arrival_station = Column(String)
    email = Column(String)
    tip_calator = Column(String)
    comanda_id = Column(String, primary_key=True)
    confirimata = Column(String)
    date = Column(String)

