Aqui está um modelo de relatório que pode ser utilizado para apresentar o sistema de gerenciamento hospitalar que você desenvolveu:

---

# **Relatório do Sistema de Gerenciamento Hospitalar**

## 1. **Introdução**

Este relatório tem como objetivo apresentar o desenvolvimento e funcionamento de um sistema de gerenciamento hospitalar utilizando estruturas de dados como filas, pilhas e árvores binárias de busca para gerenciar pacientes e prontuários. O sistema foi implementado em Python e visa simular o fluxo de atendimento de pacientes, internações e a organização dos prontuários de maneira eficiente.

## 2. **Objetivos**

O sistema tem como principais objetivos:
- Gerenciar o fluxo de pacientes no hospital, desde a entrada até o atendimento.
- Organizar os prontuários de pacientes atendidos de forma que possam ser acessados e buscados rapidamente.
- Facilitar o processo de internação e busca de pacientes internados utilizando uma estrutura de árvore binária de busca.

## 3. **Estruturas de Dados Utilizadas**

### 3.1 **Fila de Atendimento (`FilaAtendimento`)**

A fila de atendimento foi implementada utilizando uma estrutura de dados FIFO (First In, First Out). Ela permite:
- Adicionar pacientes ao final da fila.
- Atender os pacientes na ordem em que chegaram.
- Verificar se a fila está vazia.

### 3.2 **Pilha de Prontuários (`PilhaProntuario`)**

A pilha foi usada para armazenar os prontuários dos pacientes atendidos, utilizando a estrutura LIFO (Last In, First Out). Isso possibilita:
- Adicionar prontuários ao topo da pilha.
- Acessar o prontuário mais recente.
- Remover prontuários conforme necessário.

### 3.3 **Árvore de Internação (`ArvoreInternacao`)**

Uma árvore binária de busca (BST - Binary Search Tree) foi implementada para gerenciar pacientes internados. Com essa estrutura, o sistema permite:
- Inserir novos pacientes internados de acordo com o ID.
- Buscar pacientes internados de forma eficiente.
- Remover pacientes internados após sua alta ou transferência.

### 3.4 **Quicksort e Busca Binária**

Para a organização e busca eficiente de prontuários, foram implementados os seguintes algoritmos:
- **Quicksort**: Para ordenar os prontuários de pacientes após o atendimento, baseando-se no ID.
- **Busca Binária**: Para realizar buscas rápidas de prontuários ordenados.

## 4. **Funcionalidades Implementadas**

O sistema oferece as seguintes funcionalidades principais:

### 4.1 **Gerenciamento de Fila de Atendimento**
- Adição de pacientes à fila de atendimento.
- Atendimento de pacientes de acordo com a ordem de chegada.
- Verificação se a fila de atendimento está vazia.

### 4.2 **Gerenciamento de Prontuários**
- Adição de prontuários de pacientes atendidos à pilha.
- Acesso ao último prontuário adicionado (último paciente atendido).
- Remoção de prontuários da pilha quando necessário.
- Organização dos prontuários em uma lista utilizando o algoritmo Quicksort.
- Busca de prontuários através da busca binária após a ordenação.

### 4.3 **Gerenciamento de Internações**
- Internação de pacientes utilizando uma árvore binária de busca.
- Busca de pacientes internados de acordo com seu ID.
- Remoção de pacientes internados da árvore após alta ou transferência.

## 5. **Fluxo de Operação do Sistema**

1. **Entrada de Pacientes na Fila**: Os pacientes são inseridos na fila de atendimento à medida que chegam ao hospital.
2. **Atendimento de Pacientes**: Os pacientes são atendidos em ordem de chegada. Após o atendimento, o prontuário do paciente é adicionado à pilha de prontuários.
3. **Internação de Pacientes**: Pacientes que precisam ser internados são adicionados à árvore binária de busca, permitindo buscas rápidas e remoções eficientes.
4. **Organização e Busca de Prontuários**: Os prontuários são organizados utilizando o algoritmo Quicksort, permitindo buscas eficientes com a busca binária.

## 6. **Exemplo de Execução**

Durante a execução do sistema, os seguintes pacientes foram adicionados à fila de atendimento:

- Paciente João, 30 anos, ID 101, Status: Aguardando.
- Paciente Maria, 25 anos, ID 102, Status: Aguardando.
- Paciente Pedro, 45 anos, ID 103, Status: Aguardando.

Após o atendimento de João e Maria, seus prontuários foram armazenados na pilha. Em seguida, os seguintes pacientes foram internados:

- Paciente Ana, 50 anos, ID 104, Status: Internado.
- Paciente Lucas, 60 anos, ID 105, Status: Internado.

A busca pelo paciente Lucas (ID 105) na árvore de internação foi realizada com sucesso.

## 7. **Conclusão**

O sistema de gerenciamento hospitalar desenvolvido demonstrou ser eficiente para o gerenciamento de pacientes, utilizando diferentes estruturas de dados de maneira apropriada para cada cenário. A implementação de algoritmos de busca e ordenação contribuiu para otimizar o acesso e a organização dos prontuários. A modularidade do sistema também facilita futuras expansões, como o controle de mais informações sobre pacientes, relatórios detalhados ou melhorias na interface com o usuário.

---

Este é um modelo básico que você pode adaptar e detalhar conforme necessário, incluindo mais informações sobre testes, resultados e possíveis melhorias.
