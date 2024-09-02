import requests

class Model:
    def __init__(self):
        self.urlBase = 'http://localhost:3000/'

    def getAmbientes(self, endpoint):
        url = self.urlBase + endpoint
        response = requests.get(url)
        return response
    

        # response = requests.get(url)

        # if response.status_code == 200:
        #     data = response.json()
        #     print(data[0]['title'])
        # else:
        #     print(f"Erro ao consultar o servidor: {response.status_code}")