import json
import datetime
import couchdb

# weirdKeys have string-encoded JSON values that need to be decoded
weirdKeys = {'value'}
weirdKeysWithLists = {'12'} # handle these later only if we need to

f = open('../mydata/mh_001')

couch=couchdb.Server()
db=couch.create('test01')

timestampold=0
for line in f:
 j = json.loads(line);
 for k in weirdKeys:
   if k in j:
     j[k] = json.loads(j[k])
 #print json.dumps(j, sort_keys=False, indent=4, separators=(',',': '))
 print j['key']
 db.save(j)
