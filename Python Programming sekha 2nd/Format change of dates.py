text="This is line 1. Date is 22/07/2017. And there is another date: 20/01/2017. The  third and final date is 01/01/2018."
import re
pat=re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')

print(re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',text))