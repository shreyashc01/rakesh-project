import time
from flask import Flask, jsonify
from multiprocessing import Process, Value
import datetime

from pytz import country_timezones

app = Flask(__name__)


tasks = [
   {
      'id': 1,
      'title': u'Buy groceries',
      'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
      'done': False
   },
   {
      'id': 2,
      'title': u'Learn Python',
      'description': u'Need to find a good Python tutorial on the web', 
      'done': False
   }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
   return jsonify({'tasks': tasks})


def record_loop(loop_on):
   count = 0
   while True:
      if loop_on.value == True:
         x = datetime.datetime.now()
         with open('workfile', 'a') as f: 
            f.write(str(count) + '.' + str(x) )
            f.write('\n')
            count = count+1
      time.sleep(1)


if __name__ == "__main__":
   recording_on = Value('b', True)
   p = Process(target=record_loop, args=(recording_on,))
   p.start()  
   app.run(debug=True, use_reloader=False)
   p.join()