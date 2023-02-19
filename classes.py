from datetime import datetime
import requests
import telegram


class CoinGeckoAPI:
    
    def __init__(self, url_base: str):
        self.url_base = url_base


    def ping(self) -> bool:
        print('Verificando status da API...')
        url = f'{self.url_base}/ping'
        return requests.get(url).status_code == 200


    def consulta_precos(self, id_moeda: str) -> tuple:
        print('Consultando precos...')
        url = f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=BRL&include_last_updated_at=true'
        response = requests.get(url)
        
        if response.status_code == 200:
            moeda = response.json().get(id_moeda, None)
            preco = moeda.get('brl', None)
            att = datetime.fromtimestamp(moeda.get('last_updated_at', None)).strftime('%x %X')
            
            return preco, att
        
        else:
            raise ValueError('Código de resposta HTTP diferent de 200 OK')




class TelegramBot:
    def __init__(self, token: str, chat_id: str):
        self.chat_id = chat_id
        self.bot = telegram.Bot(token=token)
        
    
    def envia_mensagem(self, texto: str):
        self.bot.send_message(
            text=texto, 
            chat_id = self.chat_id, 
            parse_mode=telegram.ParseMode.MARKDOWN
        )
        print('Mensagem enviada com sucesso!!')