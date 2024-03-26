#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State Model """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
