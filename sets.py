

a = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
b = 'ttgJtRGJQctTZtZT'
c = 'CrZsJsPPZsGzwwsLwLmpwMDw'

print(set(a))
print(set(b))
print(set(c))


k = set(a) & set(b) & set(c)

print(k)
print(type(k))