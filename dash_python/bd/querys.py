import pandas as pd

caminho_excel = r'C:\Users\Augus\Desktop\Estudos\Dashboard Python\dash_python\dash_python\bd\querys.xlsx'

def pegar_cartoes_feitos(caminho_excel):
    return pd.read_excel(caminho_excel, sheet_name='CARTOES_FEITOS')


def pegar_usuarios(caminho_excel):
    return pd.read_excel(caminho_excel, sheet_name='USUARIOS')
    
usuarios = pegar_usuarios(caminho_excel)
cartoes_feitos = pegar_cartoes_feitos(caminho_excel)
print(usuarios)
print(cartoes_feitos)