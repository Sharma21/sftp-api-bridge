from fastapi import FastAPI, BackgroundTasks
from sftp_client import fetch_file_from_sftp
from file_parser import parse_csv_file
from api_client import post_data_to_api

app = FastAPI()

@app.post("/sync/")
def sync_sftp_to_api(
    background_tasks: BackgroundTasks,
    sftp_host: str,
    sftp_port: int,
    sftp_username: str,
    sftp_password: str,
    sftp_file_path: str,
    api_url: str
):
    local_file = "/tmp/sftp_file.csv"
    def process():
        fetch_file_from_sftp(
            host=sftp_host,
            port=sftp_port,
            username=sftp_username,
            password=sftp_password,
            remote_path=sftp_file_path,
            local_path=local_file,
        )
        data = parse_csv_file(local_file)
        for item in data:
            post_data_to_api(api_url, item)
    background_tasks.add_task(process)
    return {"detail": "Sync started in background"}