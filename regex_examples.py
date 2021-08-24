import re
#re.DOTALL, conside newline as a character

p = re.compile(r' Issue : (.*)\nSolution : .*', re.DOTALL)
text=" Issue : customer wants a refund for the purchases made by his brother. do not have option to process a refund on his end\nSolution : checked and verified account\nadvised to set up passkey\neducate customer to update password\nprovided refund policy\nprocessed one time courtesy refund<|endoftext|>"
match = p.search(text)
if match:
    print(match.group(0))
    print("-----")
    print(match.group(1))
print()
p = re.compile(r' Issue : .*\nSolution :(.*)', re.DOTALL)
text=" Issue : customer wants a refund for the purchases made by his brother. do not have option to process a refund on his end\nSolution : checked and verified account\nadvised to set up passkey\neducate customer to update password\nprovided refund policy\nprocessed one time courtesy refund<|endoftext|>"
match = p.search(text)
if match:
    print(match.group(0))
    print("-----")
    print(match.group(1))