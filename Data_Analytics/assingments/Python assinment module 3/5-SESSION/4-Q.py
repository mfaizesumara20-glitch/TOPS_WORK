insta_filters = ('Clarendon','Juno','Lark','Ludwig')
hi = type(insta_filters)
print(hi)

res = insta_filters.pop(2)
# AttributeError: 'tuple' object has no attribute 'pop'


