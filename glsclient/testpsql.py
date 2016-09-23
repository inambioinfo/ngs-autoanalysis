#!/usr/bin/env python
# encoding: utf-8
"""
testpsql.py

Created by Anne Pajon on 2014-07-25.
"""

import psycopg2
from psycopg2.extras import RealDictCursor

print psycopg2.__version__

db_connection = psycopg2.connect(database='clarityDB', user="readonly", password="readonly", host="limsdev.cruk.cam.ac.uk", cursor_factory=RealDictCursor)
db = db_connection.cursor()

db.execute("select * from researcher")
results = db.fetchall()

print results
print results[0]['firstname']