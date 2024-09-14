import requests

class Model:
    def __init__(self, urlBase):
        self.urlBase = urlBase

    def getDadosApi(self, endpoint):
        url = self.urlBase + endpoint
        return requests.get(url)
    

        # response = requests.get(url)

        # if response.status_code == 200:
        #     data = response.json()
        #     print(data[0]['title'])
        # else:
        #     print(f"Erro ao consultar o servidor: {response.status_code}")