capital ={'USA':'Washington DC',
          'India':'New Delhi',
          'China':'Beijing',
          'Russia':'Moscow'}

print(capital['Russia'])
print(capital.get('Germany'))
print(capital.keys())
print(capital.values())
print(capital.items())

capital.update({'Germany':'Berlin'})
capital.update({'USA':'Las Vegas'})
capital.pop('China')
print(capital.items())


for key,value in capital.items():
    print(key,value)