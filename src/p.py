import base64
import os.path


def dataURIschemebase64_input(path):
    '''
    pathのファイルをbase64エンコードして入力する
    '''

    s = 'data:image/{};base64,{}'

    ext = os.path.splitext(path)[1]
    if ext.startswith('.'):
        ext = ext[1:]

    b = dataURIschemebase64_encode(path)
    if not b == '':
        m = s.format(ext, b)
        vim.command(":normal a{}".format(m))
    else:
        print('dataURIschemebase64: Error')

def dataURIschemebase64_encode(path):
    '''
    pathのファイルを開いてbase64でエンコードしてstrを返す
    '''
    try:
        with open(path, 'rb') as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')
    except(IOError):
        encoded_string = ''
    return encoded_string
