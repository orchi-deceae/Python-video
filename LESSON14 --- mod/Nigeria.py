from random import choice

capital = 'Abuja'
bird = 'sparrow'
flower = 'Orchid'
song = 'Old town road'

def randomfunfact():
    funfact = [
        'There are 36 states in Nigeria',
        'There are 9 planets',
        'The surface of the sun is 6000ºc',
        'Liquid plastic is naphtha',
        'I will do it'
    ]
    fact = choice(funfact)
    print(fact)

if __name__ == '__main__':
    randomfunfact()
