class ParametrosBuscaCelulares():
    potencia: str
    armazenamento: str
    tamanho: str
    qualidadeTela: str
    camera: str
    bateria: str
    preco: float

    def __init__(
            self,
            potencia: str,
            armazenamento: str,
            tamanho: str,
            qualidadeTela: str,
            camera: str,
            bateria: str,
            preco: float
    ):
        self.potencia = potencia
        self.armazenamento = armazenamento
        self.tamanho = tamanho
        self.qualidadeTela = qualidadeTela
        self.camera = camera
        self.bateria = bateria
        self.preco = preco
