import PySimpleGUI as lg

lg.theme('Dark')


janela_principal = [
    [lg.Text('nome'), lg.Input(key='nome')],
    [lg.Text('email'), lg.Input(key='email')],
    [lg.Text('password'), lg.Input(key='password', password_char='*')],
    [lg.FolderBrowse('Confirmaçao de indentidade', target='input_anexo'), lg.Input(key='input_anexo')],
    [lg.Button('logar'), lg.Push()],
    [lg.CBox('lembrar'), ],
]

janela = lg.Window('cadastro', layout=janela_principal)

while True:
    event, values = janela.read()

    if event == lg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'logar':
        nome = values['nome']
        email = values['email']
        password = values['password']
        caminho_anexo = values['input_anexo']
        print(f'Nome: {nome}\nEmail: {email}\nPassword: {password}\n caminho anexo: {caminho_anexo}')