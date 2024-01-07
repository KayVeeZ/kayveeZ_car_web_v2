from sqlalchemy import create_engine, text
import os

my_secret = os.environ['db_connection_key']

engine = create_engine(my_secret)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

  
#   print("type(result):",type(result))
#   result_all = result.all()
#   print("type(result_all):",type(result_all))
#   print("result_all:",result_all,"\n\n\n")
#   first_result = result_all[0]
#   print("type(first_result):",type(first_result))
#   first_result_dict = first_result._mapping
#   result_1 = dict(first_result_dict)
#   print("type(first_result_dict):",type(first_result_dict))
#   print("type(result_1):",type(result_1))
  
# print("result_1:",result_1)


