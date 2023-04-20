# Instructions
# Complete the TODOs in this DAG so that it runs once a day. Once you’ve done that, run "/opt/airflow/start.sh" command to start the web server. Once the Airflow web server is ready,  open the Airflow UI using the "Access Airflow" button. Turn the previous exercise off, then turn this exercise on. Wait a moment and refresh the UI to see Airflow automatically run your DAG. If you get stuck, you can take a look at the solution file in the workspace/airflow/dags folder in the workspace and the video walkthrough on the next page.

import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def hello_world():
    logging.info("Hello World")

#
# TODO: Add a daily `schedule_interval` argument to the following DAG
#
dag = DAG(
        "lesson1.exercise2",
        start_date=datetime.datetime.now() - datetime.timedelta(days=60),
schedule_interval='@monthly')

task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
        dag=dag)
