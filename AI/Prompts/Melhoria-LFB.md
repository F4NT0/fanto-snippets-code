Vamos fazer alguns ajustes nesse projeto:

# Tarefas

1. Migrar as urls dos repositórios dos recibos, das pesagens e da tabela de preços para estar no arquivo `credenciais.json` já existente.
2. Toda vez que não existir o arquivo `credenciais.json` e ele for ser gerado um novo, deve requisitar também as urls dos repositórios dos recibos, das pesagens, da tabela de preços e do banco de dados.
3. Eles podem ser editados também, que nem os dados do token, do usuário e senha.
4. Garanta que sempre que for feito sincronização(tanto de pesagens, dos recibos, das tabelas de preços e do banco de dados) faça um pull pegando o que tiver externamente não causando uma dessincronização dos dados que existem no meu local quanto no externo.

# Melhorias

1. Ajuste a UI do projeto para que quando ele requisitar a criação do `credenciais.json` ele peça além do token, do usuario e do email requisite também os urls dos repositórios dos recibos, das pesagens, das tabelas de preços e do banco de dados.
2. Altere todo o código para utilizarem essas urls conforme necessidade sem deixar as urls hardcoded no projeto, deve ser pego do arquivo credenciais.json qualquer informação referente ao git.

# Antes de iniciar

1. Leia todas as informações passadas nos tópicos acima antes de começar o desenvolvimento.
2. Me pergunte se tiver qualquer duvidas sobre os tópicos acima.
3. Compile o projeto após os ajustes para ver se não quebrou o projeto.
4. Corrija qualquer erro ou warning na hora de compilar o projeto.
5. Rode o projeto no final dos ajustes para eu avaliar como ficou.
