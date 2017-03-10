import RPi.GPIO as GPIO
import time
import pydocumentdb.documents as documents
import pydocumentdb.base as base

GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

masterKey = 'eaN9uC2STpK58y75F5u9O3K24qlQiJivPFMwJCRfR640AK84z7pekS8Ua641Kk6JrvpLiz78mMc8d2ZsrMdAdQ=='
host = 'https://myblogdemo.documents.azure.com:443/'
client = document_client.DocumentClient(host, masterKey)
while True:
  print "Distance Measurement In Progress"

  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

  GPIO.output(TRIG, False)
  print "Waiting For Sensor To Settle"
  time.sleep(2)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  print "Distance:",distance,"cm"

  GPIO.cleanup()
  document_definition = {'id': '', 'reading' : distance}

  client.CreateDocument('SensorsReadings','UltraSonicCollection',document_definition)