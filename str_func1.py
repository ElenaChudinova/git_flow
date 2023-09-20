def title_alpha():
    '''Учусь решать конфликты'''
    user = input()
    return ' '.join(word[0].title + word[1:].lower for word in user.split())
    



