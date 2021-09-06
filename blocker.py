
websites = ['facebook.com', 'www.facebook.com', 'reddit.com', 'www.reddit.com']
hosts_path = '/home/alekodimitrov/Documents/hosts'


def listToString(list):
    str1 = ''

    for i in list:
        str1 += i + '\n'
    
    return str1


def websiteBlocker():
    with open(hosts_path, 'r+') as f:
        f_contents = f.read()
        print(f_contents)
        
        if listToString(websites) in f_contents:
            print('It is there')
        else:
            print("Aren't there")
            f.write(listToString(websites))


websiteBlocker()