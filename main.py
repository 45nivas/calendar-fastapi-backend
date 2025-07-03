from fastapi import FastAPI, Query
from googleapiclient.discovery import build
from google.oauth2 import service_account
from typing import List
import os
import json

app = FastAPI()

# Setup Google Credentials
def get_calendar_service():
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    SERVICE_ACCOUNT_FILE = "credentials.json"

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build("calendar", "v3", credentials=creds)
    return service

CALENDAR_ID = "my-maps-project@potent-howl-456013-k9.iam.gserviceaccount.com"

@app.get("/check")
def check_availability(date: str = Query(..., description="YYYY-MM-DD")):
    service = get_calendar_service()

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=f"{date}T00:00:00+05:30",
        timeMax=f"{date}T23:59:59+05:30",
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    if not events:
        return {"message": f"✅ No events on {date}"}
    
    result = []
    for event in events:
        summary = event.get("summary", "No Title")
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        result.append({"summary": summary, "start": start, "end": end})

    return {"date": date, "events": result}
