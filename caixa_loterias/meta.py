import urllib


API_BASE_URL  = (
    "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados"
    "?modalidade={}"
)

DATASETS = {
    "megasena": {
        "name": "Mega-Sena",
    },
    "quina": {
        "name": "Quina",
    },
    "lotofacil": {
        "name": "Lotofácil",
    },
    "lotomania": {
        "name": "Lotomania",
    },
    "duplasena": {
        "name": "Dupla Sena",
    },
    "timemania": {
        "name": "Timemania",
    },
    "loteca": {
        "name": "Loteca",
    },
    "federal": {
        "name": "Federal",
    },
    "diadesorte": {
        "name": "Dia de Sorte",
    },
    "supersete": {
        "name": "Super Sete",
    },
}


def get_url(dataset):
    # Modalidade URL encoded
    modalidade = urllib.parse.quote(DATASETS[dataset]["name"])
    return API_BASE_URL.format(modalidade)
