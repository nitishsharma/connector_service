from task_manager import TaskManager
from kafka_producer import KafkaProducer
from zookeeper_manager import ZookeeperManager

class ConnectorManager:
    def __init__(self):
        self.task_manager = TaskManager()
        self.kafka_producer = KafkaProducer()
        self.zookeeper = ZookeeperManager()

    def start_realtime_sync(self, enterprise_id, saas_application, table):
        """
        Start real-time syncing using webhook/GRPC
        """
        task_id = self.zookeeper.create_task(enterprise_id, saas_application, table, "realtime")
        self.task_manager.assign_task(task_id, enterprise_id, saas_application, table, sync_type="realtime")
        return task_id

    def start_on_demand_sync(self, enterprise_id, saas_application, table):
        """
        Start on-demand syncing using REST API calls
        """
        task_id = self.zookeeper.create_task(enterprise_id, saas_application, table, "on_demand")
        self.kafka_producer.enqueue_task(task_id, enterprise_id, saas_application, table, sync_type="on_demand")
        return task_id
