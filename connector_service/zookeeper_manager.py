from kazoo.client import KazooClient

class ZookeeperManager:
    def __init__(self):
        self.zk = KazooClient(hosts='127.0.0.1:2181')
        self.zk.start()

    def create_task(self, enterprise_id, saas_application, table, sync_type):
        """
        Creates a new task node in Zookeeper to track the state of the task
        """
        task_id = f"{enterprise_id}_{saas_application}_{table}_{sync_type}"
        self.zk.create(f"/tasks/{task_id}", b"Started", ephemeral=True)
        return task_id

    def update_task_state(self, task_id, state):
        """
        Updates the state of a task in Zookeeper
        """
        self.zk.set(f"/tasks/{task_id}", state.encode("utf-8"))

    def check_task_state(self, task_id):
        """
        Checks the current state of a task from Zookeeper
        """
        data, stat = self.zk.get(f"/tasks/{task_id}")
        return data.decode("utf-8")
