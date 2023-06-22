from sqlalchemy import create_engine, text
import os

db_connection_str = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


# open the connect using connect() function and use it
def get_db_jobs():
  jobs = []
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()

    # converting the sql datatype into python dictionary using _mapping function
    # then appending to the list.
    for row in result_all:
      jobs.append(row._mapping)

  return jobs
