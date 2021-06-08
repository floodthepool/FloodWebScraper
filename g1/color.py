f = open('colors', 'r')
g = open('colors1', 'w')

words = f.read()
words = words.replace('\n', ' ')
words = words.replace('\t', ' ')
words = words.split(' ')
ls = []

print(words[0:100])

for word in words:
    if len(word) > 3:
        w = word.lower()
        if w not in ls:
            ls.append(w)

colors = ' '.join(ls)

colors = colors.replace('\n', ' ')

g.write(colors)

f.close()
g.close()
