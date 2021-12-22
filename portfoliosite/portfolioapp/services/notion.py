import requests, json

database_id = "616319df9d0e4d2398a691faa01ebcd6"

token = "secret_TXQWDUtoSVb9DtxYE58zoMa6ZWsRDBHgXeUOce3vK35"



def save_contact_at_notion_database(email: str,
                                    message: str,
                                    subject: str,
                                    database_id: str = "616319df9d0e4d2398a691faa01ebcd6",
                                    token: str = "secret_TXQWDUtoSVb9DtxYE58zoMa6ZWsRDBHgXeUOce3vK35") -> None:
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




email = "sels2.0.3.1@gmail.com"
print(email.split("@")[0])

# save_at_notion_database_contact(database_id, token)
