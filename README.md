# Tarefas_Flask
<p>Uma API simples para gerenciar tarefas utilizando Python e Flask.</p>

<h2>Pré-requisitos</h2>
<ol>
<li>Python 3.7 ou superior.</li>
<li>Flask</li>
<li>Postman (ou outra ferramenta para testar APIs)</li>
</ol>

<h2>Configuração</h2>
<ol>
    <li>Clone o repositório para a sua máquina:</li>
</ol>
<code>https://github.com/josephDcostaR/Tarefas_Flask.git</code>
<ol start="2">
    <li>Navegue até o diretório do projeto:</li>
</ol>
<code>cd Tarefas_Flask</code>
<ol start="3">
    <li>Instale as dependências:</li>
</ol>
<code>pip install -r requirements.txt</code>
<ol start="4">
    <li>Inicie o servidor:</li>
</ol>
<code>python app.py</code>
<p>A API estará disponível em <a href="http://localhost:5000">http://localhost:5000</a>.</p>

<h2>Uso</h2>

<h3>Listar Tarefas</h3>

<p><strong>URL:</strong> <a href="http://localhost:5000/tarefas">http://localhost:5000/tarefas</a></p>
<p><strong>Método:</strong> GET</p>
<p><strong>Resposta de Sucesso (200 OK):</strong> Retorna uma lista de tarefas no formato JSON.</p>

<h3>Criar Tarefas</h3>

<p><strong>URL:</strong> <a href="http://localhost:5000/tarefas">http://localhost:5000/tarefas</a></p>
<p><strong>Método:</strong> POST</p>
<p><strong>Corpo da Requisição:</strong> Envie um objeto JSON contendo os dados da tarefa.</p>
<p><strong>Resposta de Sucesso (201 Created):</strong> Retorna a tarefa criada no formato JSON.</p>

<h3>Obter Tarefa por ID</h3>

<p><strong>URL:</strong> <a href="http://localhost:5000/tarefas/{id}">http://localhost:5000/tarefas/{id}</a></p>
<p><strong>Método:</strong> GET</p>
<p><strong>Resposta de Sucesso (200 OK):</strong> Retorna os detalhes da tarefa no formato JSON.</p>
<p><strong>Resposta de Erro (404 Not Found):</strong> Tarefa não encontrada.</p>

<h3>Editar Tarefa</h3>

<p><strong>URL:</strong> <a href="http://localhost:5000/tarefas/{id}">http://localhost:5000/tarefas/{id}</a></p>
<p><strong>Método:</strong> PUT</p>
<p><strong>Corpo da Requisição:</strong> Envie um objeto JSON contendo os dados atualizados da tarefa.</p>
<p><strong>Resposta de Sucesso (200 OK):</strong> Retorna a tarefa editada no formato JSON.</p>
<p><strong>Resposta de Erro (404 Not Found):</strong> Tarefa não encontrada ou dados inválidos.</p>

<h3>Excluir Tarefa</h3>

<p><strong>URL:</strong> <a href="http://localhost:5000/tarefas/{id}">http://localhost:5000/tarefas/{id}</a></p>
<p><strong>Método:</strong> DELETE</p>
<p><strong>Resposta de Sucesso (200 OK):</strong> Tarefa excluída com sucesso.</p>
<p><strong>Resposta de Erro (404 Not Found):</strong> Tarefa não encontrada.</p>

<h2>Testando a API</h2>

<p>Você pode testar a API utilizando o Postman ou outra ferramenta similar. Importe a coleção de requisições do Postman disponível neste repositório para facilitar os testes.</p>

<h2>Contribuindo</h2>

<p>Contribuições são bem-vindas! Se você encontrar um problema ou tiver alguma sugestão, sinta-se à vontade para abrir uma issue ou enviar um pull request.</p>

