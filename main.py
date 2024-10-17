class Paciente:
    def __init__(self, nome, idade, id, status):
        
        self.nome = nome
        self.idade = idade
        self.id = id
        self.status = status  # 'Aguardando', 'Internado', 'Alta'

    def __str__(self):
        return f"Paciente(nome={self.nome}, idade={self.idade}, id={self.id}, status={self.status})"
class NodoFila:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None

class FilaAtendimento:
    def __init__(self):
        self.frente = None
        self.tras = None

    def adicionar_paciente(self, paciente):
        novo_nodo = NodoFila(paciente)
        if self.tras is None:
            self.frente = self.tras = novo_nodo
        else:
            self.tras.proximo = novo_nodo
            self.tras = novo_nodo

    def atender_paciente(self):
        if self.frente is None:
            return None
        paciente_atendido = self.frente.paciente
        self.frente = self.frente.proximo
        if self.frente is None:
            self.tras = None
        return paciente_atendido

    def fila_vazia(self):
        return self.frente is None
class NodoPilha:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None

class PilhaProntuario:
    def __init__(self):
        self.topo = None

    def adicionar_prontuario(self, paciente):
        novo_nodo = NodoPilha(paciente)
        novo_nodo.proximo = self.topo
        self.topo = novo_nodo

    def acessar_ultimo_prontuario(self):
        if self.topo is None:
            return None
        return self.topo.paciente

    def remover_ultimo_prontuario(self):
        if self.topo is None:
            return None
        paciente_removido = self.topo.paciente
        self.topo = self.topo.proximo
        return paciente_removido

    def pilha_vazia(self):
        return self.topo is None
class NodoArvore:
    def __init__(self, paciente):
        self.paciente = paciente
        self.esquerda = None
        self.direita = None

class ArvoreInternacao:
    def __init__(self):
        self.raiz = None

    def inserir_paciente(self, paciente):
        if self.raiz is None:
            self.raiz = NodoArvore(paciente)
        else:
            self._inserir_recursivo(self.raiz, paciente)

    def _inserir_recursivo(self, atual, paciente):
        if paciente.id < atual.paciente.id:
            if atual.esquerda is None:
                atual.esquerda = NodoArvore(paciente)
            else:
                self._inserir_recursivo(atual.esquerda, paciente)
        elif paciente.id > atual.paciente.id:
            if atual.direita is None:
                atual.direita = NodoArvore(paciente)
            else:
                self._inserir_recursivo(atual.direita, paciente)

    def buscar_paciente(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, atual, id):
        if atual is None or atual.paciente.id == id:
            return atual.paciente if atual else None
        if id < atual.paciente.id:
            return self._buscar_recursivo(atual.esquerda, id)
        else:
            return self._buscar_recursivo(atual.direita, id)

    def remover_paciente(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, atual, id):
        if atual is None:
            return None
        if id < atual.paciente.id:
            atual.esquerda = self._remover_recursivo(atual.esquerda, id)
        elif id > atual.paciente.id:
            atual.direita = self._remover_recursivo(atual.direita, id)
        else:
            if atual.esquerda is None:
                return atual.direita
            elif atual.direita is None:
                return atual.esquerda

            menor_maior = self._minimo(atual.direita)
            atual.paciente = menor_maior.paciente
            atual.direita = self._remover_recursivo(atual.direita, menor_maior.paciente.id)

        return atual

    def _minimo(self, nodo):
        while nodo.esquerda is not None:
            nodo = nodo.esquerda
        return nodo
def busca_binaria(lista, id):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio].id == id:
            return lista[meio]
        elif lista[meio].id < id:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x.id < pivo.id]
    iguais = [x for x in lista if x.id == pivo.id]
    maiores = [x for x in lista if x.id > pivo.id]
    return quicksort(menores) + iguais + quicksort(maiores)
class Hospital:
    def __init__(self):
        self.fila_atendimento = FilaAtendimento()
        self.pilha_prontuario = PilhaProntuario()
        self.arvore_internacao = ArvoreInternacao()
        self.prontuarios = []  # Lista de prontuários para ordenação e busca

    def adicionar_paciente_fila(self, paciente):
        self.fila_atendimento.adicionar_paciente(paciente)

    def atender_paciente(self):
        paciente = self.fila_atendimento.atender_paciente()
        if paciente:
            self.pilha_prontuario.adicionar_prontuario(paciente)
            self.prontuarios.append(paciente)
        return paciente

    def acessar_ultimo_prontuario(self):
        return self.pilha_prontuario.acessar_ultimo_prontuario()

    def internar_paciente(self, paciente):
        self.arvore_internacao.inserir_paciente(paciente)

    def buscar_paciente_internado(self, id):
        return self.arvore_internacao.buscar_paciente(id)

    def ordenar_prontuarios(self):
        self.prontuarios = quicksort(self.prontuarios)

    def buscar_prontuario(self, id):
        self.ordenar_prontuarios()  # Ordenar antes de buscar
        return busca_binaria(self.prontuarios, id)
if __name__ == "__main__":
    hospital = Hospital()

    # Adicionar pacientes à fila
    hospital.adicionar_paciente_fila(Paciente("João", 30, 101, "Aguardando"))
    hospital.adicionar_paciente_fila(Paciente("Maria", 25, 102, "Aguardando"))
    hospital.adicionar_paciente_fila(Paciente("Pedro", 45, 103, "Aguardando"))

    # Atender pacientes e adicionar à pilha de prontuários
    hospital.atender_paciente()  # João atendido
    hospital.atender_paciente()  # Maria atendida

    # Acessar último prontuário
    print(hospital.acessar_ultimo_prontuario())

    # Internar pacientes
    hospital.internar_paciente(Paciente("Ana", 50, 104, "Internado"))
    hospital.internar_paciente(Paciente("Lucas", 60, 105, "Internado"))

    # Buscar paciente internado
    print(hospital.buscar_paciente_internado(105))  # Lucas

    # Ordenar prontuários e buscar
    hospital.ordenar_prontuarios()
    print(hospital.buscar_prontuario(102))  # Maria
