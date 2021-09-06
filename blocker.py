
websites = ['facebook.com', 'www.facebook.com', 'reddit.com', 'www.reddit.com']
hosts_path = '/etc/hosts'


def listToString(list):
    str1 = ''

    for i in list:
        str1 += '127.0.0.1 ' + i + '\n'
    
    return str1


def websiteBlocker():
    with open(hosts_path, 'r+') as f:
        f_contents = f.read()
        
        if listToString(websites) in f_contents:
            print('Unblocking sites...')
            f.seek(0)
            f.truncate()
            f.write('127.0.0.1   localhost localhost.localdomain '
                    'localhost4 localhost4.localdomain4\n'
                    '::1         localhost localhost.localdomain ' 
                    'localhost6 localhost6.localdomain6\n')
        else:
            print("Blocking sites...")
            f.write(listToString(websites))


websiteBlocker()