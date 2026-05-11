# Criação do sistema de estoque

## Tarefas

1. Crie uma nova localização no projeto focado em controle de estoques(que deve ficar no menu principal em outro local separado das pesagens e dos recibos).
2. Crie um novo diretório na localização onde ficam os recibos e as pesagens chamado banco-de-dados.
3. Toda vez que é criado um novo recibo, ele deve salvar o PDF do recibo no diretório de recibos e um .json no diretório banco-de-dados com a data e todos os pesos de cada item separados pelos seus nomes, como no seguinte exemplo:

```json
"data": "04/05/2026",
"Placa Intermediária B": "0.726",
"Placa Marrom": "0.476",
"Placa de Celular Completa": "0.024"
```
O nome do arquivo json deve ser igual ao nome do recibo, onde é o nome do cliente e a data.

4. No sistema de controle de estoque quando iniciado, deve pegar todos os .json do diretório de recibos e fazer um cálculo de pesos pelo nome, por exemplo: em vários .json tem Placa Marrom, deve ser lido todos os .json e somar todos os Kgs de placas marrons e mostrar o total no controle de estoque.
5. Quando é deletado um recibo, deve ser deletado também o .json que foi gerado, onde ele deve procurar pelo mesmo nome do PDF no diretório do banco de dados e o deletar.
6. Quando o cliente sair do sistema de recibos e ir no controle de estoque ele deve ter atualizado automaticamente, onde se tiver um .json novo ele soma ou se tiver sido deletado um recibo ele remove o .json e vai mostrar a soma sem aquele valor.
7. Faça uma tabela elegante e minimalista com o nome do material e o total dele no estoque, onde fica fácil de ver todos os itens que existem no sistema e os totais deles para entender como está o estoque.
8. Verifique todos os recibos que já foram criados até aqui, crie os .json deles no novo diretório para fazer o total do que já foi criado até agora.

## Antes de iniciar

1. Siga os passos em ordem para não dar problemas na lógica apresentada.
2. Caso tenha alguma duvida, me pergunte antes de começar a cria o novo sistema.


