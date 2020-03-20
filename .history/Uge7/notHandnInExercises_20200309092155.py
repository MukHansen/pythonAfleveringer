import re
p = re.compile(r'(Peter) (\w+)')
text = "Peter Hansen was meeting up with Jacob Fransen for a quick lunch, but first he had to go by Peter Beier to pick up some chokolate for his wife. Meanwhile Pastor Peter Jensen was going to church to give his sermon for the same 3 people in his parish. Those were Peter Kold and Henrik Halberg plus a third person who had recently moved here from Norway called Peter Harold"
m = p.search(text)
m1 = p.findall(text)

print(m.group(0))
print(m.group(1))
print(m.group(2))
# print(m1.group(0))
