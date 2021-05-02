text="Email us for any feedback here: shahriyarmitul3737 (at) gmail dot com , py At booksubeen.com , book (at)py dot com, book [at] subeen [dot] com thank you"
import re
p1=re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@',text,flags=re.I)
print(re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*\s+','.',p1,flags=re.I))