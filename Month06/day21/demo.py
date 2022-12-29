from collections import Counter
s = 'java'

# Counter(s)
# Counter({'a': 2, 'j': 1, 'v': 1})

for w, t in Counter(s).items():
    print(w, t)

print({'a': 2, 'j': 1, 'v': 1}.values())