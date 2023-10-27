#!/usr/bin/python3
"""Holds class city"""

import models
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Representation of city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize city"""
        super().__init__(*args, **kwargs)
