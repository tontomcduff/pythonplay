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

  jtitle=jentry['title']
  jimage_url=jentry['image_url']
  jdetailsdescription=jdetails['description_html']

print(jentry)
print(jdetails)
print(jdetailsdescription)

htmlDOCTYPE = '<!DOCTYPE html>'
htmlTag = '<html>'
htmlTagEnd = '</html>'
htmlHeadTag = '<head>'
htmlMeta = '<meta charset="UTF-8"> '
htmlCSSFile = '<link rel="stylesheet" type="text/css" media="screen" title="Custom Settings" href="lesson1.css" >'
htmlHeadTagEnd = '</head>'
htmlBodyTag = '<body>'
htmlBodyTagEnd = '</body>'
htmlEntryImageTag = '<img id="main_image" src="'
htmlEntryImageTagEnd = '" alt>' 
htmlH1Tag = '<h1>'
htmlH1TagEnd = '</h1>'
htmlParaTag = '<p>'
htmlParaTagEnd = '</p>'
htmlDivInnerBodyStart = '<Div id="body_inner">'
htmlDivEnd = '</Div>'

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
  wf.write(htmlCSSFile)
  wf.write(htmlHeadTagEnd)
  wf.write(htmlBodyTag)
  wf.write(htmlDivInnerBodyStart)
  wf.write(htmlEntryImageTag)
  wf.write(jimage_url)
  wf.write(htmlEntryImageTagEnd)
  wf.write(htmlH1Tag)
  wf.write(jtitle)
  wf.write(htmlH1TagEnd)
  wf.write(htmlParaTag)
  wf.write(jdetailsdescription)
  wf.write(htmlParaTagEnd)
  wf.write(htmlDivEnd)
  wf.write(htmlBodyTagEnd)
  wf.write(htmlTagEnd)