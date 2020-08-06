from requests import get

class Clima(object):
    __api_id = ''
    def __init__(self):
        super().__init__()
        self.__api_id = 'ace20b49fb38a51829a45560cbf2311f'

    
    def getclima(self, provincia):
        query = provincia.lower()
            
        solicitud = get('https://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid={}'.format(query, self.__api_id))
        valores = solicitud.json()
        
        if valores["cod"] == '404':
            raise ValueError('Provincia "{}" no encontrada.'.format(provincia))

        return (valores["main"]["temp"], valores["main"]["feels_like"], valores["main"]["humidity"])