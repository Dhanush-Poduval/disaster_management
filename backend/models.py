from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey,DateTime
from datetime import datetime,date

class Location(Base):
    __tablename__='location'
    id=Column(Integer,primary_key=True, index=True)
    city=Column(String)
    state=Column(String)
    country=Column(String)

class Disaster(Base):
    __tablename__='disaster'
    id=Column(Integer,primary_key=True, index=True)
    disaster_type=Column(String)
    severity=Column(String)
    start_date=Column(DateTime)
    location_id=Column(Integer, ForeignKey('location.id'))

class Victim(Base):
    __tablename__='victim'
    id=Column(Integer,primary_key=True,index=True)
    victim_name=Column(String)
    age=Column(Integer)
    gender=Column(String)
    disaster_id=Column(Integer, ForeignKey('disaster.id'))

class Resource(Base):
    __tablename__='resource'
    id=Column(Integer,primary_key=True,index=True)
    resource_name=Column(String)
    quantity=Column(Integer)

class relief_camp(Base):
    __tablename__='relief_camp'
    id=Column(Integer,primary_key=True,index=True)
    camp_name=Column(String)
    location_id=Column(Integer, ForeignKey('location.id'))
class distribution(Base):
    __tablename__='distribution'
    id=Column(Integer,primary_key=True,index=True)
    resource_id=Column(Integer, ForeignKey('resource.id'))
    camp_id=Column(Integer, ForeignKey('relief_camp.id'))
    quantity=Column(Integer)
    distribution_date=Column(DateTime)