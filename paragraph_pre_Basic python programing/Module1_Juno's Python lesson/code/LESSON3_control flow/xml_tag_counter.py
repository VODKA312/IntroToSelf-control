tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    # you should consider that <> construct one XML element
    if token[0] == '<' and token[-1] == '>':
        count = count + 1

print(count)