#Baseado em codigo disponivel em
#https://www.tutorialspoint.com/python/python_multithreading.htm
#!/usr/bin/python

import thread
import time

# Define a function for the thread
def funcao_thread( nomeThread, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( nomeThread, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( funcao_thread, ("Thread a cada 2 segundos", 2, ) )
   thread.start_new_thread( funcao_thread, ("Thread a cada 4 segundos", 4, ) )
   thread.start_new_thread( funcao_thread, ("Thread a cada 8 segundos", 8, ) )
   thread.start_new_thread( funcao_thread, ("Thread a cada 10 segundos", 10, ) )
except:
   print "Impossivel executar thread"

while 1:
   pass