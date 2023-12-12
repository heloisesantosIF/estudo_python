# No terminal:
"""
pip install requests
"""

#importação de pacotes básicos

from requests import get
from pprint import pprint

base_url_ = 'https://api.openweathermap.org/data/2.5'
chave_acesso = 'f808d8419b3d5d33c997954f4c0f2cfd'

#definir o endpoint
endpoint = f'{base_url_}/weather'

#criar o filtro usando um dicionário com os parametros mínimos
filtro = {
    'q': 'Caraguatatuba, SP, BR',
    'appid': chave_acesso,
    'lang': 'pt_br',
    'units':'metric'
}

#enviar uma requisição GET passando os parametros de filtro
clima = get(endpoint, params=filtro)

#verifica o código de resposta
if clima.status_code != 200:
    print(f'Erro de acesso (código): {clima.status_code}')
else:
    #recupera os dados quando resposta com sucesso (codigo 200)
    resposta = clima.json()
    #exibe todos os dados da resposta
    pprint(resposta)

    #extrair algumas informações relevantes
    #coordenadas que serao usadas em outro momento
    coordenadas = resposta.get('coord')
    latitude = coordenadas.get('lat')
    longitude = coordenadas.get('lon')
    print(f'Latitude: {latitude}, Longitude:{longitude}')

    #descricao do clima atual
    condicao_clima = resposta.get('weather')[0]
    descricao_clima = condicao_clima.get('description')
    print(f'Tempo em Caraguatatuba: {descricao_clima}')

    #temperatura atual
    temperatura = resposta.get('main')
    temperatura = temperatura.get('temp')
    print(f'Temperatura em Caraguatatuba: {temperatura}')

endpoint = f'{base_url_}/air_pollution'

filtro = {
    'lat': latitude,
    'lon': longitude,
    'appid': chave_acesso
}

poluicao = get(endpoint, params=filtro)

if poluicao.status_code != 200:
    print(f'Erro de acesso (código: {poluicao.status_code}')
else:
    resposta = poluicao.json()

    dados = resposta.get('list')[0]
    indice = dados.get('main').get('aqi')

    qualidade_ar = {
        1: 'boa',
        2: 'regular',
        3: 'inadequada',
        4: 'muito ruim',
        5: 'péssima'
    }

    print(f'Qualidade do ar agora: {qualidade_ar[indice]}')

endpoint = f'{base_url_}/forecast'

filtro = {
    'lat': latitude,
    'lon': longitude,
    'appid': chave_acesso,
    'lang': 'pt_br',
    'units':'metric',
    'cnt': 3
}

previsao = get(endpoint, params=filtro)

if previsao.status_code != 200:
    print(f'Erro de acesso (código: {previsao.status_code}')
else:
    resposta = previsao.json()
    previsoes = resposta.get('list')

    for previsao in previsoes:
        data = previsao.get('dt_txt')
        temperatura_maxima = previsao.get('main').get('temperatura_maxima')
        temperatura_minima = previsao.get('main').get('temperatura_minima')
        descricao = previsao.get('weather')[0].get('description')
print(f'Data/Hora: {data}, Temp. Máxima: {temperatura_maxima}°C, Temp. Mínima: {temperatura_minima}°C, Descrição: {descricao}')




