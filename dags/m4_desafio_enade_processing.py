from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
import boto3


aws_access_key_id = Variable.get('aws_access_key_id')
aws_secret_access_key = Variable.get('aws_secret_access_key')
glue = boto3.client('glue', region_name='us-east-2',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)


def create_and_trigger_crawler_enade_m4_enade():
    try:
        glue.get_crawler(Name='crawler_m4_enade')
    except glue.exceptions.EntityNotFoundException:
        glue.create_crawler(
            Name='crawler_m4_enade',
            Role='arn:aws:iam::597495568095:role/santo-glue-service-role',
            DatabaseName='enade2017',
            Description='Crawler enade 2017 ',
            Targets={
                'S3Targets': [
                    {
                        'Path': 's3://m4-597495568095/processing-zone/enade/',
                        'Exclusions': []
                    },
                ]
            }
        )

    glue.start_crawler(
        Name='crawler_m4_enade'
    )


with DAG(
    'enade_batch',
    default_args={
        'owner': 'Santo',
        'depends_on_past': False,
        'email': ['andersonesanto@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'max_active_runs': 1,
    },
    description='submit spark-pi as sparkApplication on kubernetes',
    schedule_interval="0 */2 * * *",
    start_date=days_ago(1),
    catchup=False,
    tags=['spark', 'kubernetes', 'batch', 'enade', 'igti', 'm4'],
) as dag:
    enade_converte_parquet = SparkKubernetesOperator(
        task_id='enade_converte_parquet',
        namespace="airflow",
        application_file="enade_converte_parquet.yaml",
        kubernetes_conn_id="kubernetes_default",
        do_xcom_push=True,
    )

    enade_converte_parquet_sensor = SparkKubernetesSensor(
        task_id='enade_converte_parquet_sensor',
        namespace="airflow",
        application_name="{{ task_instance.xcom_pull(task_ids='enade_converte_parquet')['metadata']['name'] }}",
        kubernetes_conn_id="kubernetes_default",
    )

    create_and_trigger_crawler_enade = PythonOperator(
        task_id='create_and_trigger_crawler_enade',
        python_callable=create_and_trigger_crawler_enade_m4_enade
    )


enade_converte_parquet >> enade_converte_parquet_sensor >> create_and_trigger_crawler_enade
