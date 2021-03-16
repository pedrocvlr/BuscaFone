from database.models import get_connection
from models.celular_model import CelularModel
from models.parametros_busca_celular import ParametrosBuscaCelulares


def buscar_celulares(parametros_da_busca: ParametrosBuscaCelulares):
    connection = get_connection()
    resultado = connection.execute("select "
                                       "c.modelo, "
                                       "c.desempenho, "
                                       "c.armazenamento, "
                                       "c.tamanho_tela, "
                                       " c.qualidade_tela, "
                                       "c.camera,c.bateria, "
                                       "c.preco, "
                                       "c.imagem, "
                                       "c.link_compra"
                                   " from celular c "
                                   "where c.modelo = 'Iphone 12'")
    celulares = []
    for row in resultado:
        celular_model = CelularModel(**row)
        celulares.append(celular_model)

    return celulares
