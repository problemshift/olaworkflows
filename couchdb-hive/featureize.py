import sys
import json
#base_page_url = 'https://class.coursera.org/aboriginaled-001/'
base_page_url = sys.argv[1]
#print len(base_page_url)
base_page_url_len = len(base_page_url)
for line in sys.stdin:
  d = line.split('\001')
  timestamp = d[0][:-3] # drop the milliseconds
  userid = d[1]
  sessionid = d[2]
  eventtype = d[3]
  if eventtype != 'pageview':
    continue
  page_url = d[4]
  print "%s %s %d %s" % (userid, timestamp, 1, page_url[base_page_url_len:])
