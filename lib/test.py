

import time

import threading

class MyThread ( threading.Thread ):

   def run ( self ):

      print('You called my start method, yeah.')
      time.sleep(3) #will sleep for 5 seconds

      print('Were you expecting something amazing?')

MyThread().start()
