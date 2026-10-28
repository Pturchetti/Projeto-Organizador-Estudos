# Organizador de Estudos

Aplicação desktop desenvolvida em Python com Tkinter para auxiliar estudantes na organização da rotina acadêmica. O sistema reúne ferramentas para gerenciamento de disciplinas e tarefas, planejamento semanal, controle de sessões de estudo e acompanhamento do progresso individual.

O projeto foi desenvolvido por estudantes do segundo semestre do curso de **Engenharia de Computação da Universidade Federal de Santa Maria (UFSM)**, no contexto da disciplina de **Projeto Integrador**, com o objetivo de aplicar conceitos de programação e desenvolvimento de software na construção de uma solução voltada a uma necessidade cotidiana dos estudantes.

## 1. Sobre o projeto

A organização da rotina acadêmica envolve diferentes atividades, como acompanhar prazos, distribuir tarefas ao longo da semana, reservar períodos para cada disciplina e avaliar o tempo dedicado aos estudos. Quando essas informações ficam dispersas entre diferentes ferramentas ou registros, pode ser mais difícil acompanhar as atividades e manter uma rotina organizada.

O Organizador de Estudos propõe reunir essas funcionalidades em uma única aplicação desktop, permitindo que o estudante gerencie suas atividades acadêmicas e acompanhe os próprios registros de estudo em um ambiente integrado.

A aplicação utiliza armazenamento local, dispensando a necessidade de um servidor externo para guardar as informações. Dessa forma, os dados podem ser mantidos entre diferentes execuções do programa no mesmo computador.

## 2. Funcionalidades

### 2.1. Gerenciamento de disciplinas

Permite cadastrar e organizar as disciplinas cursadas pelo estudante, mantendo suas informações disponíveis para utilização nas demais funcionalidades da aplicação.

### 2.2. Gerenciamento de tarefas acadêmicas

Possibilita registrar atividades, como trabalhos, listas de exercícios e provas, associando-as às respectivas disciplinas quando aplicável. O acompanhamento do estado de cada tarefa permite distinguir atividades pendentes daquelas já concluídas.

### 2.3. Cronômetro de estudos

Disponibiliza um temporizador baseado na técnica Pomodoro, que alterna períodos de foco e descanso. A duração dos períodos pode ser configurada pelo usuário, e o tempo de estudo é registrado conforme as regras de contabilização implementadas na aplicação.

### 2.4. Planejamento semanal

Permite organizar períodos de estudo ao longo da semana, distribuindo as atividades previstas entre os dias disponíveis. O planejamento funciona como uma referência para a organização da rotina, distinguindo o tempo planejado daquele efetivamente registrado.

### 2.5. Histórico de estudos

Reúne registros das sessões de estudo concluídas, permitindo consultar informações sobre as atividades realizadas e o tempo dedicado aos estudos.

### 2.6. Estatísticas de estudo

Apresenta indicadores calculados a partir dos registros disponíveis, oferecendo uma visão geral do tempo dedicado aos estudos e do progresso registrado ao longo do tempo.

### 2.7. Persistência de dados

Armazena localmente as informações da aplicação em arquivos JSON, permitindo recuperá-las em execuções posteriores sem depender de um serviço externo de banco de dados.

> A disponibilidade e o comportamento de cada funcionalidade correspondem ao estado atual da implementação no repositório.

## 3. Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Implementação da lógica e das funcionalidades. |
| Tkinter | Construção da interface gráfica desktop. |
| JSON | Organização e armazenamento local dos dados. |
| Git | Controle de versão do código-fonte. |
| GitHub | Hospedagem do repositório e colaboração no desenvolvimento. |

A escolha dessas tecnologias permite desenvolver uma aplicação desktop sem depender de um framework gráfico externo de grande porte ou de uma infraestrutura de servidor.

## 4. Organização do código

O projeto utiliza uma estrutura modular, na qual os arquivos Python são organizados de acordo com as responsabilidades principais da aplicação.

```text
Projeto-Organizador-Estudos/
├── main.py
├── interface.py
├── gerenciamento_materias.py
├── gerenciamento_tarefas.py
├── cronometro.py
├── planejamento_semanal.py
├── historico.py
├── estatisticas.py
├── persistencia.py
├── imagens/
├── fontes/
└── dados/
```

Os principais módulos são:

- **`main.py`** — inicialização da aplicação e integração dos componentes.
- **`interface.py`** — construção das telas e gerenciamento da interação com o usuário.
- **`gerenciamento_materias.py`** — operações relacionadas às disciplinas cadastradas.
- **`gerenciamento_tarefas.py`** — gerenciamento das atividades acadêmicas e de seus estados.
- **`cronometro.py`** — controle do temporizador e dos períodos de foco e descanso.
- **`planejamento_semanal.py`** — organização dos períodos de estudo planejados.
- **`historico.py`** — registro e consulta das atividades de estudo realizadas.
- **`estatisticas.py`** — cálculo dos indicadores apresentados pela aplicação.
- **`persistencia.py`** — leitura e gravação dos dados locais.

As pastas de recursos complementam essa organização: `imagens/` reúne os elementos gráficos utilizados pela interface, `fontes/` pode conter fontes adicionais e `dados/` é destinada aos arquivos de armazenamento local.

A separação por módulos busca facilitar a manutenção do código, a compreensão das responsabilidades de cada componente e a evolução das funcionalidades.

## 5. Requisitos

Para executar o projeto, são necessários:

- Python 3 compatível com o código da aplicação;
- Tkinter disponível na instalação do Python;
- Git, caso o repositório seja obtido pela linha de comando.

O programa foi concebido como uma aplicação desktop. Não é necessário configurar um servidor web ou instalar um sistema de gerenciamento de banco de dados externo.

### 5.1. Instalação do Python e do Tkinter

O Python pode ser obtido em [python.org](https://www.python.org/downloads/).

A disponibilidade do Tkinter depende da distribuição do Python e do sistema operacional utilizado.

- **Windows:** recomenda-se uma instalação do Python que inclua o Tcl/Tk.
- **Linux:** algumas distribuições disponibilizam o Tkinter em um pacote separado. O nome e o procedimento de instalação variam conforme a distribuição.
- **macOS:** a disponibilidade do Tkinter depende da distribuição do Python instalada.

## 6. Instalação e execução

### 6.1. Obter o código-fonte

Clone o repositório:

```bash
git clone https://github.com/Pturchetti/Projeto-Organizador-Estudos.git
```

Entre na pasta do projeto:

```bash
cd Projeto-Organizador-Estudos
```

### 6.2. Executar a aplicação

Com o Python e o Tkinter instalados, execute:

```bash
python main.py
```

Em ambientes nos quais o comando `python` não aponta para o Python 3, pode ser necessário utilizar `python3 main.py` no Linux e macOS ou `py main.py` no Windows.

A execução deve ser feita a partir do diretório principal do projeto, para que os caminhos relativos aos recursos e arquivos locais sejam resolvidos conforme esperado.

## 7. Armazenamento e privacidade

Os dados são armazenados localmente em arquivos JSON dentro da pasta `dados/`, conforme a organização adotada pela aplicação.

Como o armazenamento é local, os dados não são automaticamente sincronizados entre computadores. A cópia do projeto para outra máquina também não garante a transferência dos registros existentes, que dependem dos arquivos locais correspondentes.

Recomenda-se não publicar informações pessoais ou registros reais de estudantes no repositório. Arquivos de dados locais devem ser avaliados antes de qualquer envio ao GitHub.

## 8. Contexto acadêmico

O Organizador de Estudos foi desenvolvido por estudantes do **segundo semestre do curso de Engenharia de Computação da Universidade Federal de Santa Maria (UFSM)**, como parte das atividades da disciplina de **Projeto Integrador**.

O projeto tem como objetivo aplicar, de forma prática, os conhecimentos adquiridos ao longo da formação acadêmica, por meio do desenvolvimento colaborativo de uma aplicação desktop voltada à organização da rotina de estudos.

Sua implementação envolve conceitos fundamentais de desenvolvimento de software, incluindo programação, modularização, desenvolvimento de interfaces gráficas, manipulação de dados, persistência local e integração entre componentes.

Além do aprendizado técnico, a proposta busca relacionar os conhecimentos da Engenharia de Computação à solução de uma necessidade cotidiana dos estudantes.

## 9. Licença

O repositório ainda não possui uma licença de software especificada. As condições de uso, modificação e redistribuição do código deverão ser definidas pelos responsáveis pelo projeto.

---

Desenvolvido no contexto da graduação em Engenharia de Computação da Universidade Federal de Santa Maria (UFSM), para a disciplina de Projeto Integrador no segundo semestre.
