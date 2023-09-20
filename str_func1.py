def title_alpha():
    '''Усусь решать конфликы'''
    user = input()
    return ' '.join(word[0].title + word[1:].lower for word in user.split())



