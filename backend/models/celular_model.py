class CelularModel:
    modelo: str
    desempenho: float
    armazenamento: int
    tamanho_tela: float
    qualidade_tela: float
    camera: float
    bateria: int
    preco: float
    imagem: str
    link_compra: str

    def __init__(
            self,
            modelo: str,
            desempenho: float,
            armazenamento: int,
            tamanho_tela: float,
            qualidade_tela: float,
            camera: float,
            bateria: int,
            preco: float,
            imagem: str,
            link_compra: str,
    ):
        self.modelo = modelo
        self.desempenho = desempenho
        self.armazenamento = armazenamento
        self.tamanho_tela = tamanho_tela
        self.qualidade_tela = qualidade_tela
        self.camera = camera
        self.bateria = bateria
        self.preco = preco
        self.imagem = imagem
        self.link_compra = link_compra
