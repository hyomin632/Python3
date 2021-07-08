# 다국어 인삿말

def sayHello(nation):
    if nation == '1':
        print('안녕하세요')
    elif nation == '2':
        print('Hello')
    elif nation == '3':
        print('Sorry, I am preparing Japanese (;´・`)>')
    elif nation == '4':
        print('Sorry, I am preparing Chinese (;´・`)>')

nation = input('Where are you from? \n'
               '1. 한국, 2. USA, 3. JAPAN, 4. CHINA')

sayHello(nation)
