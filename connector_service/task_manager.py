from webhook_handler import WebhookHandler
from rest_sync_handler import RestSyncHandler

class TaskManager:
    def __init__(self):
        self.webhook_handler = WebhookHandler()
        self.rest_sync_handler = RestSyncHandler()

    def assign_task(self, task_id, enterprise_id, saas_application, table, sync_type):
        """
        Assign tasks to worker nodes based on the sync type (realtime or on_demand)
        """
        if sync_type == "realtime":
            self.webhook_handler.handle_webhook_sync(task_id, enterprise_id, saas_application, table)
        else:
            self.rest_sync_handler.handle_rest_sync(task_id, enterprise_id, saas_application, table)
