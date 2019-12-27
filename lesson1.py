import json

openfile = open('content.json', 'r')
a = openfile.read()

#print (a)

with open('content.json') as f:
  jfile = json.load(f)
  entryversion=jfile['version']
  entryerror=jfile['error']

  jdata=jfile['data']

  jdetails=jdata['details']
  jentry=jdata['entry']
  jmetadata=jdata['metadata']
  jcomments=jdata['comments']
  jrelated=jdata['related']
  jimage_urls=jdata['image_urls']

jdetailsdescription=jdetails['description']

print(jdetails)
print(jdetailsdescription)

htmlDOCTYPE = '<!DOCTYPE html>'
htmlTag = '<html>'
htmlTagEnd = '</html>'
htmlHeadTag = '<head>'
htmlMeta = 'meta charset="UTF-8"'
htmlHeadTagEnd = '</head>'
htmlBodyTag = '<body>'
htmlBodyTagEnd = '</body>'

#writefile = open('content.html', 'r+')
#writefile.write(htmlTag)
#writefile.write(htmlHeadTag)
#writefile.write(htmlHeadTagEnd)
#writefile.write(htmlBodyTag)
#writefile.write(jdetailsdescription)
#writefile.write(htmlBodyTagEnd)
#writefile.write(htmlTagEnd)
#writefile.close

with open('content.html', 'r+') as wf:
  wf.write(htmlDOCTYPE)
  wf.write(htmlTag)
  wf.write(htmlHeadTag)
  wf.write(htmlMeta)
  wf.write(htmlHeadTagEnd)
  wf.write(htmlBodyTag)
  wf.write(jdetailsdescription)
  wf.write(htmlBodyTagEnd)
  wf.write(htmlTagEnd)