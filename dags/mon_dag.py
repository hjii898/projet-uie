from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # prend le répertoire du DAG

default_args = {
    'owner': 'wanehaoua21-eng',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),   # à ajuster
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='pipeline_hdfs_hive',
    default_args=default_args,
    description='Orchestration collecte -> load HDFS -> archive -> TL Hive',
    schedule='@daily',        # planification quotidienne
    catchup=False,
    tags=['hdfs', 'hive'],
) as dag:

    t_collecte = BashOperator(
        task_id='collecte',
        bash_command=f'python {SCRIPT_DIR}/collecte.py',
    )

    t_load_hdfs = BashOperator(
        task_id='load_hdfs',
        bash_command=f'python {SCRIPT_DIR}/loadhdfs.py',
    )

    t_archive = BashOperator(
        task_id='archive_hdfs',
        bash_command=f'python {SCRIPT_DIR}/archivehdfs.py',
    )

    t_tl_hive = BashOperator(
        task_id='tl_hive',
        bash_command=f'python {SCRIPT_DIR}/tlhive.py',
    )

    # Ordre d'exécution : collecte → load HDFS → archive → TL Hive
    t_collecte >> t_load_hdfs >> t_archive >> t_tl_hive
