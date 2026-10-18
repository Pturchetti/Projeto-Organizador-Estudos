# Organizador de Estudos

Aplicação desktop desenvolvida em Python com Tkinter para ajudar estudantes a organizar disciplinas, acompanhar tarefas e prazos, planejar a semana, cronometrar sessões de estudo e visualizar o próprio progresso.

O projeto será desenvolvido em equipe e tem escopo inicial pensado para ser concluído em aproximadamente uma semana. Os módulos abaixo definem responsabilidades para orientar a implementação e facilitar a integração, sem determinar como cada integrante deve programar sua parte.

## Módulos Python

### `main.py` — inicialização e integração

Será o ponto de entrada do programa. Deve reunir a inicialização da aplicação e conectar os módulos, sem concentrar nele as regras específicas de cada funcionalidade.

Responsabilidades esperadas:
- iniciar a aplicação e abrir a interface principal;
- preparar ou solicitar o carregamento dos dados necessários;
- conectar a interface aos módulos de matérias, tarefas, cronômetro, planejamento, histórico, estatísticas e persistência;
- coordenar o encerramento da aplicação, quando necessário.

**Limite:** as telas devem ficar em `interface.py`, e as regras específicas devem permanecer nos módulos responsáveis por elas.

### `interface.py` — telas, componentes visuais e navegação

Responsável pela parte visual e pela interação com o usuário usando Tkinter.

Deve contemplar:
- janela principal e organização visual das áreas da aplicação;
- menus, botões, campos de entrada, listas, rótulos e mensagens;
- navegação entre as funcionalidades;
- apresentação dos dados recebidos dos demais módulos;
- captura das ações do usuário e encaminhamento delas ao módulo correspondente;
- avisos de sucesso, erros de preenchimento e situações sem dados cadastrados.

A interface deve permitir acessar as matérias, tarefas, cronômetro, planejamento semanal, histórico e estatísticas.

**Limite:** evitar concentrar na interface regras de cadastro, cálculos estatísticos ou leitura e gravação de arquivos. Ela deve solicitar essas operações aos módulos responsáveis.

### `gerenciamento_materias.py` — cadastro e organização das matérias

Responsável por manter a lista de matérias ou disciplinas que o estudante está cursando.

Deve contemplar:
- cadastrar uma matéria;
- listar e consultar as matérias cadastradas;
- localizar uma matéria específica para uso em tarefas, planejamento e sessões de estudo;
- editar informações de uma matéria, se essa funcionalidade for incluída;
- remover uma matéria, considerando que outros registros podem estar associados a ela;
- validar informações básicas, como evitar um nome vazio e tratar cadastros duplicados.

Uma matéria pode ter, no mínimo, um identificador e um nome. Outros campos, como cor ou descrição, podem ser definidos pela equipe se forem úteis.

**Integração:** tarefas, planejamento e histórico devem conseguir associar seus registros à matéria correspondente de maneira consistente.

### `gerenciamento_tarefas.py` — tarefas, prazos e conclusão

Responsável por registrar e acompanhar atividades acadêmicas, como listas de exercícios, trabalhos e provas.

Deve contemplar:
- cadastrar uma tarefa com título ou descrição;
- associar a tarefa a uma matéria, quando aplicável;
- registrar prazo ou data prevista, quando houver;
- listar tarefas e consultar seus detalhes;
- distinguir tarefas pendentes das concluídas;
- permitir marcar uma tarefa como concluída e, se necessário, atualizar ou excluir um registro;
- oferecer informações que permitam à interface destacar tarefas próximas do prazo ou atrasadas.

Uma tarefa pode conter identificador, título/descrição, matéria associada, prazo e estado de conclusão. A equipe deve manter os mesmos critérios de estado em todo o programa.

**Limite:** este módulo cuida das atividades a realizar; o registro do tempo efetivamente estudado pertence ao cronômetro e ao histórico.

### `cronometro.py` — temporizador de estudo (Pomodoro)

Responsável por controlar o tempo das sessões de estudo.

Deve contemplar:
- iniciar, pausar e retomar a contagem;
- encerrar ou reiniciar uma sessão;
- permitir selecionar a matéria relacionada à sessão;
- definir uma duração de estudo e, se o escopo permitir, intervalos de descanso;
- informar à interface o tempo restante e o estado atual do cronômetro;
- identificar quando a sessão termina e disponibilizar os dados necessários para registrar uma sessão concluída.

A técnica Pomodoro pode ser implementada com períodos de estudo e descanso configuráveis ou com durações predefinidas. Para manter o escopo viável, a equipe pode começar com uma configuração simples.

**Integração:** ao finalizar uma sessão válida, seus dados devem poder ser encaminhados ao histórico. Pausar ou cancelar não deve registrar acidentalmente uma sessão como concluída.

### `planejamento_semanal.py` — organização dos estudos da semana

Responsável por organizar e consultar os períodos de estudo planejados para os dias da semana.

Deve contemplar:
- adicionar um período de estudo a um dia;
- associar o período a uma matéria e, se desejado, a uma tarefa;
- registrar dia e horário ou período previsto;
- consultar o planejamento de um dia e visualizar a semana;
- editar ou remover um período planejado;
- tratar conflitos simples de horário, caso essa validação seja implementada.

Cada item do planejamento pode conter identificador, dia/data, horário ou duração prevista, matéria e descrição opcional.

**Distinção importante:** o planejamento representa o que o estudante pretende estudar; o histórico registra o que foi efetivamente realizado. Um período planejado não deve ser tratado automaticamente como uma sessão concluída.

### `historico.py` — registro e consulta das sessões realizadas

Responsável por manter os registros das sessões de estudo concluídas.

Deve contemplar:
- receber os dados de uma sessão finalizada pelo cronômetro;
- registrar matéria, data e duração efetiva da sessão;
- listar e consultar sessões anteriores;
- permitir filtrar ou agrupar os registros por data e matéria, se o escopo permitir;
- fornecer os registros necessários para as estatísticas;
- evitar duplicar uma mesma sessão por causa de múltiplos eventos de encerramento.

Um registro de sessão pode conter identificador, matéria, data/hora e duração efetiva. Se forem usados intervalos de descanso, eles não devem ser somados ao tempo efetivo de estudo.

**Integração:** este módulo mantém os registros; os cálculos de totais e indicadores ficam em `estatisticas.py`.

### `estatisticas.py` — resumo do progresso de estudos

Responsável por calcular indicadores a partir do histórico e, quando pertinente, do planejamento e das tarefas.

Indicadores possíveis para a versão inicial:
- tempo total de estudo;
- tempo estudado por matéria;
- quantidade de sessões concluídas;
- tempo estudado por dia ou semana;
- comparação simples entre tempo planejado e tempo realizado, caso os dados necessários estejam disponíveis.

Deve fornecer resultados que a interface consiga apresentar em textos, tabelas ou gráficos simples. Gráficos são opcionais: primeiro, é importante garantir que os cálculos e os totais estejam corretos.

**Limite:** este módulo calcula os indicadores, mas não deve manter uma segunda cópia independente do histórico nem ser responsável por salvar os dados.

### `persistencia.py` — leitura e gravação dos dados

Responsável por carregar e salvar os dados locais da aplicação, usando arquivos JSON.

Deve contemplar:
- ler os dados existentes ao iniciar a aplicação;
- gravar alterações de matérias, tarefas, planejamento e histórico;
- definir caminhos consistentes para os arquivos armazenados em `dados/`;
- tratar a primeira execução, quando os arquivos ainda não existem;
- lidar com arquivos vazios, inválidos ou com estrutura inesperada sem encerrar a aplicação de forma abrupta;
- manter um formato de dados consistente para que os módulos consigam compartilhar informações.

Os módulos devem combinar previamente quais dados serão salvos, quais campos cada registro terá e como os identificadores e associações serão representados.

**Limite:** a persistência cuida da entrada e saída dos arquivos. As regras de cadastro, contagem de tempo e cálculo de estatísticas permanecem em seus respectivos módulos.

## Organização das pastas

- **`imagens/`** — imagens, ícones e outros recursos visuais usados nas telas.
- **`fontes/`** — arquivos de fontes adicionais, caso sejam necessários.
- **`dados/`** — arquivos JSON com os dados locais da aplicação. Arquivos de dados reais ou pessoais não devem ser adicionados ao repositório sem necessidade.

## Integração entre os módulos

Para evitar incompatibilidades durante o desenvolvimento, a equipe deve combinar antes de integrar:
- quais informações identificam uma matéria, uma tarefa, um período planejado e uma sessão de estudo;
- como tarefas e sessões apontam para uma matéria;
- quais funções e parâmetros cada módulo disponibilizará aos demais;
- em que momentos os dados serão carregados e salvos;
- como erros de validação e falhas de leitura/gravação serão comunicados à interface.

Uma divisão clara de responsabilidades ajuda a evitar que a mesma regra seja implementada em vários arquivos. A implementação pode ser simplificada conforme o tempo disponível, priorizando um fluxo completo e funcional em vez de recursos opcionais.

## Tecnologias

- **Python** — linguagem da aplicação.
- **Tkinter** — criação da interface gráfica.
- **JSON** — armazenamento local dos dados.

Os arquivos Python estão inicialmente vazios. Este README descreve o escopo esperado, mas não contém implementação: as funcionalidades serão programadas pela equipe durante o desenvolvimento.
