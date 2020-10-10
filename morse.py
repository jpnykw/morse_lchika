morse_list = {
  'A': '.-',
  'B': '-...',
  'C': '-.-.',
  'D': '-..',
  'E': '.',
  'F': '..-.',
  'G': '--.',
  'H': '....',
  'I': '..',
  'J': '.---',
  'K': '-.-',
  'L': '.-..',
  'M': '--',
  'N': '-.',
  'O': '---',
  'P': '.--.',
  'Q': '--.-',
  'R': '.-.',
  'S': '...',
  'T': '-',
  'U': '..-',
  'V': '...-',
  'W': '.--',
  'X': '-..-',
  'Y': '-.--',
  'Z': '--..',
  '0': '-----',
  '1': '.----',
  '2': '..---',
  '3': '...--',
  '4': '....-',
  '5': '.....',
  '6': '-....',
  '7': '--...',
  '8': '---..',
  '9': '----.',
}

import sys
import RPi.GPIO as GPIO
import time

def init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(2, GPIO.OUT)

def sig_s():
  GPIO.output(2, True)
  time.sleep(0.1)
  GPIO.output(2, False)

def sig_l():
  GPIO.output(2, True)
  time.sleep(0.3)
  GPIO.output(2, False)

def send():
  for _ in xrange(int(repeat)):
    for i in xrange(len(plane_text)):
      code = morse_list[plane_text[i].upper()]
      print(code)
      for j in xrange(len(code)):
        signal = code[j]
        sig_s() if signal == '.' else sig_l()
        time.sleep(0.6)

# Start
args = sys.argv
plane_text = args[1]
repeat = args[2]

init()
send()
