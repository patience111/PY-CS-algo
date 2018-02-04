EtoF={'bread':'pain','wine':'win','with':'avec',
        'I':'Je','eat':'mange','drink':'bois','John':'Jean','friends':'amis','and':'et','of':'du','red':'rouge'}
FtoE={'pain':'bread','win':'wine','avec':'with',
        'Je':'I','mange':'eat','bois':'drink','Jean':'John','amis':'friends','et':'and','du':'of',  'rough':'red'}
dicts={'English to French':EtoF,'French to English':FtoE}
def translateWord(word,dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word !='':
        return '"'+word+'"'
    return word
def translate(phrase,dicts,direction):
    ucletters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lcletters='abcdefghijklmnopqrstuvwxyz'
    letters=ucletters+lcletters
    dictionary=dicts[direction]
    translation=''
    word=''
    for c in phrase:
        if c in letters:
            word=word+c
        else:
            translation=translation+translateWord(word,dictionary)+c
            word=''

    return translation+''+translateWord(word,dictionary)
print(translate('I drink good red wine,and eat bread.',dicts,'English to French'))
print(translate('Je bois du vin rouge.',dicts,'French to English'))
    
