from urllib import request
import os

downloade = {
    'gitconfig':{'url':'https://raw.githubusercontent.com/Loki69/Settings-under-me/master/git/gitconfig',
                'save':'~/.gitconfig'
                },
    'terminal':{'url':'https://raw.githubusercontent.com/Loki69/Settings-under-me/master/terminal/git-prompt.sh',
                'save':'~/.git-prompt.sh',
                'apply':{
                    'file':'~/.bashrc',
                    'text':'source ~/.git-prompt.sh'
                }
                },
    'promt':{'url':'https://raw.githubusercontent.com/Loki69/Settings-under-me/master/terminal/view.sh',
                'save':'~/.view.sh',
                'apply':{
                    'file':'~/.bashrc',
                    'text':'source ~/.view.sh'
                }
                },
}

def absolute_path(path):
    return os.path.expanduser(path)

def rename_file(file, number_of_copies=1):
    new_name = file +' ('+str(number_of_copies)+')'
    if os.path.exists(new_name):
        rename_file(file, number_of_copies=number_of_copies+1)
    else:
        os.rename(file, new_name)



for key, value in downloade.items():
    file = absolute_path(value.get('save'))
    if os.path.exists(file):
        rename_file(file)
    request.urlretrieve(value.get('url'), file)

    if value.get('apply') != None:
        file = absolute_path(value['apply']['file'])
        with open(file, 'a') as apply:
            text = str(value['apply']['text'])+'\n'
            apply.write(text)
