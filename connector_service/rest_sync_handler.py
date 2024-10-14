import requests

class RestSyncHandler:
    def handle_rest_sync(self, task_id, enterprise_id, saas_application, table):
        """
        Handles syncing using REST API (Pull mechanism) for on-demand updates
        """
        print(f"Starting on-demand sync for task {task_id}, enterprise {enterprise_id}, app {saas_application}, table {table}")
        
        # Example API call to pull data from SaaS application
        response = requests.get(f"https://{saas_application}/api/data/{table}")
        if response.status_code == 200:
            data = response.json()
            # Push the data to the enterprise database here
        else:
            print(f"Failed to pull data for task {task_id}: {response.status_code}")
