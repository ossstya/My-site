import requests, json
from dotenv import load_dotenv
import os

load_dotenv()

def save_contact_at_notion_database(email: str,
                                    message: str,
                                    subject: str,
                                    database_id: str = os.environ.get("NOTION_DATABASE_ID"),
                                    token: str = os.environ.get("NOTION_TOKEN")) -> None:
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16"
    }

    notionUrl = f"https://api.notion.com/v1/pages"
    newPageData = {
        "parent": {
            "database_id": database_id
        },
        "properties": {
            "Email": {
                "email": email
            },
            "Subject": {
                "rich_text": [
                    {
                        "text": {
                            "content": subject
                        }
                    }
                ]
            },
            "Message": {
                "rich_text": [
                    {
                        "text": {
                            "content": message
                        }
                    }
                ]
            },
            "Read": {
                "type": "checkbox",
                "checkbox": False
            },
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": email.split("@")[0]
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)
    res = requests.request("POST", notionUrl, headers=headers, data=data)

