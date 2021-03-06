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

6. Fazer a integração com alguma engine de data lake. No caso da AWS, você deve:  
  a. Configurar um Crawler para a pasta onde os arquivos na staging estão depositados.  
  b. Validar a disponibilização no Athena.  

7. Caso deseje utilizar o Google, disponibilize os dados para consulta usando o Big Query. Caso utilize outra nuvem, a escolha da engine de Data Lake é livre.  

8. Use a ferramenta de Big Data ou a engine de Data Lake (ou o BigQuery, se escolher trabalhar com Google Cloud) para investigar os dados e responder às perguntas do desafio.  

9. Quando o desenho da arquitetura estiver pronto, crie um repositório no Github (ou Gitlab, ou Bitbucket, ou outro de sua escolha) e coloque os códigos de processos Python e implantação da estrutura Kubernetes.
***
## Execução
#### Criar cluster eks
#### Instalar airflow
#### Instalar spark

#### Preparar DAGS e fluxo no Airflow
- Download e extração do CSV
  - s3://m4-597495568095/landing-zone/MICRODADOS_ENADE_2017.txt
- Conversão CSV para Parquet
- Criar Glue Crawler
    baseado em https://gist.github.com/ejlp12/30d67c07bf9e46b98a350569976f08aa

#### Fluxo de execução do DAG
- enade_converte_parquet >> 
- enade_converte_parquet_sensor >> 
- create_and_trigger_crawler_enade

#### Efetuar consultas no Athena
***
Todo o código foi baseado no repositório:  
https://github.com/neylsoncrepalde/edc_mod4_exercise_igti  

https://www.cncf.io/blog/2021/01/20/spark-operator-and-s3-4-integration-steps-to-operator-flames/

https://stackoverflow.com/questions/34209196/amazon-s3a-returns-400-bad-request-with-spark

https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/docs/user-guide.md

