import json
import datetime
import fileinput
reservedWords = {'from'}
# weirdKeys have string-encoded JSON values that need to be decoded
weirdKeys = {'value'}
weirdKeysWithLists = {'12'} # handle these later only if we need to

for line in fileinput.input():
 j = json.loads(line);
 for k in weirdKeys:
   if k in j:
     j[k] = json.loads(j[k])
 for k in weirdKeysWithLists:
   if k in j:
     a=[];
     for e in j[k]:
      a.append(json.loads(e));
     j[k] = a;
 for k in j.keys():
     try:
       v = j[k]
       i =  int(k);
       del j[k]
       k= 'field_'+ k
       j[k] = v
     except:
      pass       
     if k in reservedWords:
      v = j[k]
      del j[k]
      k = 'coursera_' + k
      j[k] = v
 print json.dumps(j, sort_keys=False, indent=4, separators=(',',': '))
