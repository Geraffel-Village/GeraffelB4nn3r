#!/usr/bin/python

import os
import time
import pickle, hashlib

DEBUG=False

PATTERN_AVAIL="./pattern"
PATTERN_QUEUE="./pattern-queue"

currentPatternNumer = 0

patternfiles = sorted(os.listdir(PATTERN_QUEUE))
patternfilesHash = hashlib.md5(pickle.dumps(patternfiles)).hexdigest()
if DEBUG:
  print patternfiles
  print patternfilesHash

while True:
  
  newpatternfiles = sorted(os.listdir(PATTERN_QUEUE))
  newpatternfilesHash = hashlib.md5(pickle.dumps(newpatternfiles)).hexdigest()
  
  if patternfilesHash != newpatternfilesHash:
    if DEBUG:
      print "new file found"
      print newpatternfiles
    patternfiles = newpatternfiles
    patternfilesHash = newpatternfilesHash
    currentPatternNumer = 0

  print "playing pattern %s (filename: %s)" % (currentPatternNumer, patternfiles[currentPatternNumer])

  time.sleep(2)
  if len(patternfiles)-1 <= currentPatternNumer:
    currentPatternNumer = 0
  else:
    currentPatternNumer += 1
  #break
  if DEBUG:
    print "loop end"

