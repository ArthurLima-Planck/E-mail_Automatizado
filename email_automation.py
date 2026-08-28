
from googleapiclient.discovery import build

service = build("gmail", "v1", credentials=credenciais)
emails = service.users().messages().list(
    userId="me"
).execute()
