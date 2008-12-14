import csv
from bot_commons import *

# long just because it is able to be used with different angles for each sail

afoc2 = []
foc2 = []
speeds = csv.reader(open('foc2.csv'), delimiter=' ', quotechar='"')
for row in speeds:
  #print ', '.join(row)
  afoc2.append(float(row[0]))
  foc2.append(float(row[1]))

acode0 = []
code0 = []
speeds = csv.reader(open('code0.csv'), delimiter=' ', quotechar='"')
for row in speeds:
  acode0.append(float(row[0]))
  code0.append(float(row[1]))

aspi = []
spi = []
speeds = csv.reader(open('spi.csv'), delimiter=' ', quotechar='"')
for row in speeds:
  aspi.append(float(row[0]))
  spi.append(float(row[1]))

agennaker = []
gennaker = []
speeds = csv.reader(open('gennaker.csv'), delimiter=' ', quotechar='"')
for row in speeds:
  agennaker.append(float(row[0]))
  gennaker.append(float(row[1]))

agenois = []
genois = []
speeds = csv.reader(open('genois.csv'), delimiter=' ', quotechar='"')
for row in speeds:
  agenois.append(float(row[0]))
  genois.append(float(row[1]))

def parameters(abs, ord):
  a = (ord[1] - ord[0]) / (abs[1] - abs[0])
  b = ord[1] - (a * abs[1])
  return (a,b)

def indice(abs, angle):
  i = 0 
  while angle >= abs[i]:
    i = i + 1
  return i-1

# best speed for angle
def best(angle):
  i = indice(afoc2, angle)
  (a,b) = parameters(afoc2[i:i+2], foc2[i:i+2])
  sfoc2 = a * angle + b
  result = ('foc2', sfoc2)
  i = indice(acode0, angle)
  (a,b) = parameters(acode0[i:i+2], code0[i:i+2])
  scode0 = a * angle + b
  if scode0 > result[1]:
    result = ('code0', scode0)
  i = indice(aspi, angle)
  (a,b) = parameters(aspi[i:i+2], spi[i:i+2])
  sspi = a * angle + b
  if sspi > result[1]:
    result = ('spi', sspi)
  i = indice(agennaker, angle)
  (a,b) = parameters(agennaker[i:i+2], gennaker[i:i+2])
  sgennaker = a * angle + b
  if sgennaker > result[1]:
    result = ('gennaker', sgennaker)
  i = indice(agenois, angle)
  (a,b) = parameters(agenois[i:i+2], genois[i:i+2])
  sgenois = a * angle + b
  if sgenois > result[1]:
    result = ('genois', sgenois)
  if SHOW_ALL:
    print result
  return result

