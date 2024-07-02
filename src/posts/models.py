from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, MetaData, Table

metadata = MetaData()

post = Table(
    'post',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=True),
    Column("data", TIMESTAMP, default=datetime, nullable=True),


)
