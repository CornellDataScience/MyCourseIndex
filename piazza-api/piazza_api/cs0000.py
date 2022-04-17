import json
from datetime import datetime
from piazza_api import Piazza
from piazza_api import exceptions
from slacker import Slacker
from time import sleep



course_id = 'j91pec3j5o6yx'
piazza_email = 'zw238@cornell.edu'
piazza_password = 'sth'

p = Piazza()
p.user_login(email = piazza_email, password = piazza_password)
cs0000 = p.course(course_id)

# posts = cs0000.get_post('1432')

i = 1

with open('test.json', 'w') as f:
  while True:
    try:
      posts = cs0000.get_post(str(i))
      json.dump(posts, f)
      f.write('\n')
      i += 1
      print(i)
    except exceptions.PiazzaRequestError:
      print(i)
      if i > 1600:
        break
      else:
        i += 1
        continue
      

    



  