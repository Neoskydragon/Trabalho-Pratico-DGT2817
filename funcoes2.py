def loginUsuario(perfil):
    # Verifica se o perfil é 'admin', ignorando maiúsculas/minúsculas devido a utilização de lower
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador') #se verdadeiro imprime a mensagem para administrador
    else:
        print('Bem-vindo, Usuário') #senão imprime a mensagem para usuário

# Chamadas da função com diferentes valores de parâmetro
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')