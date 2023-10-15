import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS


con = psycopg2.connect(
            host="postgres",
            port="5432",
            user="postgres",
            password="test")
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

# Obtain a DB Cursor
cursor = con.cursor();
name_Database = "property";

# Create table statement

sqlCreateDatabase = "create database " + name_Database + ";"

# Create a table in PostgreSQL database

#cursor.execute(sqlCreateDatabase);

con.commit()
con.close()

con = psycopg2.connect(
            host="postgres",
            port="5432",
            database="property",
            user="postgres",
            password="test")

cursor = con.cursor();

sqlCreateTable = "CREATE TABLE properties (" \
                 "address VARCHAR (255) NOT NULL," \
                 "img_url VARCHAR (255) NOT NULL" \
                 ");"
#cursor.execute(sqlCreateTable)

con.commit()
con.close()