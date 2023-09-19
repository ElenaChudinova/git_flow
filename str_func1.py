def title_alpha():
    '''Строка с заглавной буквы'''
    user = input()
    return ' '.join(word[0].title + word[1:].lower for word in user.split())



