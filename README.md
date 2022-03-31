RenamePy é uma ferramenta para renomear automaticamente arquivos .PDF, por meio do reconhecimento de seus conteúdos e
seguindo um padrão pré-estabelecido de nomenclatura para cada tipo de documento.

Por meio de conexão com o banco de dados o programa compara os valores de texto encontrados no arquivo e verifica
em um dicionário a qual categoria o documento pertence, Fiscal, Contábil ou Departamento Pessoal, sendo possivel adicionar
quantos tipos forem necessários.

RenamePy utiliza Watchdog para monitorar um diretório, sempre que um arquivo é criado neste diretório o sistema,
lê, identifica, renomeia e move o arquivo para uma pasta de saída.

Arquivos não identificados ou que não sejam do tipo PDF são movidos para um diretório de arquivos não identificados.

Arquivos repetidos recebem mais um campo a seus nomes, além da data atual recebem também hora, minuto e segundo no final
do nome.
