import locale, os
from classes import CoinGeckoAPI, TelegramBot
# from dotenv import load_dotenv

# load_dotenv()
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

URL_BASE = "https://api.coingecko.com/api/v3/"
TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

api = CoinGeckoAPI(url_base=URL_BASE)
bot = TelegramBot(token=TOKEN, chat_id=CHAT_ID)

id_moeda = input('Qual o ID da moeda a ser consultada? ').lower()
v_min = int(input('Qual o valor minimo para esta consulta? '))
v_max = int(input('Qual o valor máximo para esta consulta? '))

if api.ping():
    print('API online!!')
    preco, att_in = api.consulta_precos(id_moeda=id_moeda)
    print('Preço obtido com sucesso!!')
    
    mensagem = None
    
    if preco < v_min:
        mensagem = f'*Cotação do {id_moeda.upper()}:* \n\n\t *Preço:* {locale.currency(preco, grouping=True)} \n\t *Atualizado em:* {att_in}' \
                   f'\n\n\t *Motivo:* Valor menor do que o minimo'
    
    elif preco > v_max:
        mensagem = f'*Cotação do {id_moeda.upper()}:* \n\n\t *Preço:* {locale.currency(preco, grouping=True)} \n\t *Atualizado em:* {att_in}' \
                   f'\n\n\t *Motivo:* Valor maior do que o máximo'
                   
    if mensagem:
        bot.envia_mensagem(mensagem)
    
else:
    pass
