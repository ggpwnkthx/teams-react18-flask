from sqlalchemy import ForeignKey, String, DECIMAL
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from libs.sql.types.Geography import Geography
from ..base import Base, genUUID
from flask_sqlalchemy import SQLAlchemy
from libs.flask import app
db = SQLAlchemy(app)

#Location table
class Location(Base):
    """
    Model for the Location table
    """
    __tablename__ = 'locations'
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=genUUID)
    owner = db.Column(String(128), unique=False)
    smartystreets = relationship("SmartyStreets", back_populates="location", uselist = False)
    googleplaces = relationship("GooglePlaces", back_populates="location", uselist = False)
    geoframes = relationship("GeoFrames", back_populates="location")
    
#SmartyStreets table
class SmartyStreets(Base):
    """
    Model for the SmartyStreets table
    """
    __tablename__ = 'smartystreets'
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=genUUID)
    location_id = db.Column(UNIQUEIDENTIFIER, ForeignKey('locations.id'))
    md5 = db.Column(String(), unique=False)
    latitude = db.Column(DECIMAL(11,6), unique=False)
    longitude = db.Column(DECIMAL(11,6), unique=False)
    cityName = db.Column(String(), unique=False)
    defaultCityName = db.Column(String(), unique=False)
    deliveryPoint = db.Column(String(), unique=False)
    deliveryPointCheckDigit = db.Column(String(), unique=False)
    extraSecondaryDesignator = db.Column(String(), unique=False)
    extraSecondaryNumber = db.Column(String(), unique=False)
    plus4Code = db.Column(String(), unique=False)
    pmbDesignator = db.Column(String(), unique=False)
    pmbNumber = db.Column(String(), unique=False)
    primaryNumber = db.Column(String(), unique=False)
    secondaryDesignator = db.Column(String(), unique=False)
    secondaryNumber = db.Column(String(), unique=False)
    state = db.Column(String(), unique=False)
    streetName = db.Column(String(), unique=False)
    streetPostdirection = db.Column(String(), unique=False)
    streetPredirection = db.Column(String(), unique=False)
    streetSuffix = db.Column(String(), unique=False)
    urbanization = db.Column(String(), unique=False)
    zipCode = db.Column(String(), unique=False)
    location = relationship("Location", back_populates="smartystreets")

#GeoJson table
class GeoFrames(Base):
    """
    Model for the frame table
    """
    __tablename__ = 'geoframes'
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=genUUID)
    location_id = db.Column(UNIQUEIDENTIFIER, ForeignKey('locations.id'))
    esq_id = db.Column(String(128), unique=False)
    type = db.Column(String(), unique=False)
    geoframe = db.Column(Geography(), unique=False)
    location = relationship("Location", back_populates="geoframes")
    
#Google Places table
class GooglePlaces(Base):
    """
    Model for the Google Places table
    """
    __tablename__ = 'googleplaces'
    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, default=genUUID)
    location_id = db.Column(UNIQUEIDENTIFIER, ForeignKey('locations.id'))
    md5 = db.Column(String(), unique=False)
    location = relationship("Location", back_populates="googleplaces")