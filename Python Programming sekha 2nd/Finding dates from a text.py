text="This is line 1. Date is 2017/06/01. And there is another date: 2017-07-01. The  third and final date is 2017/08/30."
import re
pat=re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')

print(pat.findall(text))