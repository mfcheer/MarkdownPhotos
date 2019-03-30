
import re

reg = re.compile('\s')


import requests


with open('index.md', 'r') as f:
	for line in f:
		if reg.sub('', line):
			ss = line.split(' ')
			if len(ss) >= 4:
				url =  ss[2]
				r = requests.get(url)
				filename = url.split('/')[-1] 
				with open(filename,'wb') as f:
					f.write(r.content)
					

