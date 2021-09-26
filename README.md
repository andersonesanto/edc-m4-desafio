# edc-m4-desafio
*** 
# IGTI 
# MBA em Engenharia de Dados
## Bootcamp - Engenheiro de dados Cloud
### Módulo 4 - DDE Desenho de arquiteturas de dados escaláveis
*** 
## Desafio do Bootcamp
Os alunos deverão desempenhar as seguintes atividades:  
1. Criar um cluster Kubernetes para a realização das atividades (local ou baseado em nuvem). Recomendamos utilizar um cluster baseado em nuvem para comportar o volume de dados trabalhado.  
2. Realizar a instalação e configuração do Spark Operator conforme instruções de aulas.  
3. Realizar a instalação e configuração de outas ferramentas que se deseje utilizar (Airflow, Argo CD etc).  
4. Realizar a ingestão dos dados do Enade 2017 no AWS S3 ou outro storage de nuvem de sua escolha.  
    Dados disponíveis em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade  
  Os dados devem ser ingeridos de maneira automatizada na zona raw, zona crua ou zona bronze do seu Data Lake.  
5. Utilizar o SparkOperator no Kubernetes para transformar os dados no formato parquet e escrevê-los na zona staging ou zona silver do seu data lake.  
6. Fazer a integração com alguma engine de data lake. No caso da AWS, você deve
  a. Configurar um Crawler para a pasta onde os arquivos na staging estão depositados.
  b. Validar a disponibilização no Athena.  
7. Caso deseje utilizar o Google, disponibilize os dados para consulta usando o Big Query. Caso utilize outra nuvem, a escolha da engine de Data Lake é livre.  
8. Use a ferramenta de Big Data ou a engine de Data Lake (ou o BigQuery, se escolher trabalhar com Google Cloud) para investigar os dados e responder às perguntas do desafio.  
9. Quando o desenho da arquitetura estiver pronto, crie um repositório no Github (ou Gitlab, ou Bitbucket, ou outro de sua escolha) e coloque os códigos de processos Python e implantação da estrutura Kubernetes.

***
Todo o código foi baseado no repositório:  
https://github.com/neylsoncrepalde/edc_mod4_exercise_igti  