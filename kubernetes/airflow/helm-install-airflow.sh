# prepara o ambiente para airflow e executa a instalação
kubectl create namespace airflow
kubectl apply -f airflow/rolebinding_for_airflow.yaml
helm install airflow apache-airflow/airflow -f airflow/myvalues.yaml -n airflow --debug