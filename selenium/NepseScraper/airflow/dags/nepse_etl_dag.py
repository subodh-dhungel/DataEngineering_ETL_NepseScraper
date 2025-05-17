from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
import pendulum

def run_main_script():
    subprocess.run(["python3", "/opt/airflow/dags/main.py"], check=True)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1,tzinfo=pendulum.timezone('Asia/Kathmandu')),
    'retries': 1,
}

with DAG(
    dag_id='run_main_script_dag',
    default_args=default_args,
    schedule_interval='30 9 * * *', 
    catchup=False,
    tags=['load nepse data to the database'],
) as dag:

    run_script_task = PythonOperator(
        task_id='run_main_py_script',
        python_callable=run_main_script,
    )

    run_script_task
