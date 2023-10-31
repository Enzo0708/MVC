# Aplicação de Lista de Tarefas - Padrão MVC

Este é um exemplo simples de uma aplicação de lista de tarefas usando o padrão Model-View-Controller (MVC). O MVC é uma arquitetura de software que divide a aplicação em três componentes principais: Model, View e Controller. Cada componente tem uma função específica na aplicação.

## Padrão MVC

- **Model:** O Model representa a lógica de negócios da aplicação e os dados. Neste projeto, a classe `ToDo` é o Model e é responsável por gerenciar a lista de tarefas, incluindo adicionar, excluir e listar tarefas. Além disso, a classe `Dao` atua como um componente de persistência de dados para interagir com um arquivo de texto para armazenar tarefas.

- **View:** A View é responsável pela apresentação e interface do usuário. Neste projeto, a classe `VIEW` contém o código para exibir um menu de opções para o usuário e receber sua entrada no console.

- **Controller:** O Controller age como um intermediário entre o Model e a View. Ele recebe as entradas do usuário da View, interage com o Model para realizar operações e atualiza a View com os resultados. As classes `ControllerAdicionarTarefa`, `ControllerExcluirTarefa` e `ControllerListarTarefas` controlam a lógica de adicionar, excluir e listar tarefas, respectivamente.

- **DAO (Data Access Object):** O DAO é um componente responsável por acessar e manipular os dados. Neste projeto, a classe `Dao` é responsável por interagir com um arquivo de texto para armazenar e recuperar tarefas.

## Classes

- **ToDo:** Representa o Model da aplicação e é responsável por gerenciar a lista de tarefas.

- **VIEW:** Representa a View da aplicação e é responsável por exibir o menu de opções e receber a entrada do usuário.

- **ControllerAdicionarTarefa:** Um controlador que lida com a adição de tarefas ao Model.

- **ControllerExcluirTarefa:** Um controlador que lida com a exclusão de tarefas com base no índice fornecido pelo usuário.

- **ControllerListarTarefas:** Um controlador que lista todas as tarefas do Model, formatando a exibição para que o ID não seja visível.

- **ControllerAlterarTarefas:** Este controlador lida com a alteração de tarefas existentes. Ele recebe o índice da tarefa a ser alterada e a nova descrição da tarefa do usuário. Em seguida, ele interage com o Model para atualizar a descrição da tarefa.

- **ControllerListarTarefasConcluidas:**  Este controlador é responsável por listar todas as tarefas concluídas. Ele interage com o Model para recuperar todas as tarefas e, em seguida, filtra a lista para incluir apenas as tarefas que foram marcadas como concluídas.

- **ControllerConcluirTarefa:** Este controlador lida com a conclusão de tarefas. Ele recebe o índice da tarefa a ser concluída do usuário e, em seguida, interage com o Model para marcar a tarefa como concluída.

- **Dao:** Uma classe que lida com a persistência de dados, como adicionar, listar e excluir tarefas em um arquivo de texto.

## Uso

Para usar a aplicação, basta executar o arquivo da View no console. A partir daí, você pode escolher entre as opções disponíveis para adicionar, listar ou excluir tarefas.




