#!/usr/bin/env python3
"""
This module introduces a class.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    This class defines a table called users.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(350), nullable=True)
    reset_token = Column(String(250), nullable=True)
