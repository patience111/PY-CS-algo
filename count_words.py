def words_count(filename):
    '''count the approximate number of words in a file'''
    try:
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        msg='The file '+filename+"does't exist."
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print('The file '+filename+' has about '+str(num_words)+' words.')
filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    words_count(filename)

