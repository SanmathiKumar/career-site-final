import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_str = "mysql+pymysql://sgl9o0mztmly30lk0mva:pscale_pw_3wN8UL7gQL8MoW4JXcb7HmAiz2mL2UwHsvOlOGq440K@aws.connect.psdb.cloud/aromacareers?charset=utf8mb4"

engine = create_engine(db_connection_str,
                      connect_args = {
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

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


