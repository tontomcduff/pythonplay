import json

openfile = open('c:\\python34\\content.json', 'r')
a = openfile.read()

#print (a)

with open('c:\\python34\\content.json') as f:
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

htmlTag = '<html>'
htmlTagEnd = '</html>'
htmlHeadTag = '<head>'
htmlHeadTagEnd = '</head>'
htmlBodyTag = '<body>'
htmlBodyTagEnd = '</body>'

writefile = open('c:\\python34\\content.html', 'r+')
writefile.write(htmlTag)
writefile.write(htmlHeadTag)
writefile.write(htmlHeadTagEnd)
writefile.write(htmlBodyTag)
writefile.write(jdetailsdescription)
writefile.write(htmlBodyTagEnd)
writefile.write(htmlTagEnd)
writefile.close

