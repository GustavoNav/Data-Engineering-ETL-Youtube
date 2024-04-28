import datetime
from src.contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract(
    load_content=[
        {'title': 'PALMEIRAS 1 X 0 NOVORIZONTINO | MELHORES MOMENTOS | SEMIFINAL | PAULISTÃO 2024', 'link': 'https://www.youtube.com//watch?v=vg7cSVeTOzg', 'views': '649.861', 'video_time': '5:34', 'time_online': '20 horas 5 minutos e 34 segundos', 'extraction_date': datetime.date(2024, 3, 29)}, 
        {'title': "j-hope 'NEURON (with 개코, 윤미래)' Official Motion Picture", 'link': 'https://www.youtube.com//watch?v=z4Rg_VgOlJU', 'views': '729.580', 'video_time': '4:37', 'time_online': '19 horas 4 minutos e 37 segundos', 'extraction_date': datetime.date(2024, 3, 29)}, 
        {'title': 'Nilson Neto - LUA (Clipe Oficial)', 'link': 'https://www.youtube.com//watch?v=sTyqGuPv458', 'views': '246.276', 'video_time': '3:29', 'time_online': '22 horas 3 minutos e 29 segundos', 'extraction_date': datetime.date(2024, 3, 29)}
    ]
)