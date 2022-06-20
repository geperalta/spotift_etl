from datetime import timedelta
from airflow import DAG
##from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from spotify_etl import run_spotify_etl
#from example import myfunc ##testing the imports, needed to create the plugin subfolder

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag', ##name of our dag
    default_args=default_args,
    description='My first DAG with ETL process with Spotify data!',
    schedule_interval=timedelta(days=1),
)

def dummy_function(): ##Was a dummy function to test and know all is working fine
    print("All is working fine in the DAG :)")

run_etl = PythonOperator(  ##what actually gets done by a task, 1 operator 1 TASK
    task_id='whole_spotify_etl',
    python_callable=run_spotify_etl,#dummy_function#mydummyfunc
    dag=dag,
)

##We define the order of excetution of the TASKs at the end of the code
##IF we have multiple tasks we use arrows as: t1 >> [t2, t3]
run_etl