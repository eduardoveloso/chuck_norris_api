# Projeto chucknorris.io

![Chuck Norris](https://api.chucknorris.io/img/chucknorris_logo_coloured_small@2x.png "Chuck Norris")

Chucknorris.io é uma API JSON gratuita para fatos de Chuck Norris com curadoria manual.

Os fatos de Chuck Norris são fatos satíricos sobre o artista marcial e ator Chuck Norris que se tornaram um fenômeno da Internet e, como resultado, se espalharam na cultura popular. Os 'fatos' são normalmente afirmações hiperbólicas absurdas sobre a resistência, atitude, virilidade, sofisticação e masculinidade de Norris.

Os fatos de Chuck Norris se espalharam pelo mundo, levando não apenas a versões traduzidas, mas também a versões localizadas mencionando anúncios específicos do país e outros fenômenos da Internet. Às vezes, também são feitas insinuações ao seu uso de chutes roundhouse para realizar aparentemente qualquer tarefa, sua grande quantidade de pêlos no corpo com relação específica à sua barba e seu papel na série de televisão de ação Walker, Texas Ranger.

https://api.chucknorris.io/#!

# Arquitetura

![Arquitetura](https://www.tridant.com/wp-content/uploads/2022/08/MS-Architecture-1.jpg "Arquitetura")

* Ingestao de dados e armazenamento na camada raw (salvo no formato json, conforme retorno da API)
* Tratativas e enriquecimento de dados a cada etapa

# Tecnologias

* Data Factory - orquestrador do pipeline
* Databricks - engine de processamento de dados
* Blobstorage - datalake para armazenamento dados
