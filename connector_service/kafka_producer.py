from kafka import KafkaProducer
import json

class KafkaProducer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def enqueue_task(self, task_id, enterprise_id, saas_application, table, sync_type):
        """
        Enqueue a task in Kafka to be processed by worker nodes
        """
        task_message = {
            "task_id": task_id,
            "enterprise_id": enterprise_id,
            "saas_application": saas_application,
            "table": table,
            "sync_type": sync_type
        }
        self.producer.send('task_queue', json.dumps(task_message).encode('utf-8'))
        print(f"Task {task_id} enqueued for processing")
