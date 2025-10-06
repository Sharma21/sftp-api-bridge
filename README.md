# SFTP to API Bridge (Python FastAPI)

## Overview
A starter template to fetch files from an SFTP server, parse them, and push the data to an API endpoint.

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the server:
   ```
   uvicorn main:app --reload
   ```

3. Trigger sync via API:
   ```
   POST /sync/
   {
     "sftp_host": "example.com",
     "sftp_port": 22,
     "sftp_username": "user",
     "sftp_password": "pass",
     "sftp_file_path": "/remote/path/file.csv",
     "api_url": "https://destination.api/resource"
   }
   ```

## Customization

- Extend `file_parser.py` for your file format (CSV, Excel, etc.).
- Implement authentication and error handling as needed.