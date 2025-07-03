# 🗓️ Calendar Booking Backend (FastAPI + Groq + Google Calendar)

This is a FastAPI backend that takes natural language input like:

```
"Book appointment with Shanks on 5th July 2025 from 4pm to 5pm"
```

It extracts the event details using Groq LLM, converts it into a proper datetime format, and adds the event to your Google Calendar using a Service Account.

## 🔧 Features

✅ Accepts natural language prompts for booking  
🧠 Uses Groq LLM to extract summary, date, start, and end time  
📆 Adds events to Google Calendar using service account  
📤 Exposes API endpoints to book and retrieve events by date  

## 🧠 Technologies

- **FastAPI** – Web framework
- **Groq API** – LLM for prompt parsing
- **Google Calendar API** – To insert events
- **Render** – For deployment

## 🚀 How It Works

1. **User says:** `book appointment with nami on 5th july 7pm to 8pm`

2. **LLM (Groq) extracts:**
   ```json
   {
     "summary": "Appointment with Nami",
     "date": "2025-07-05",
     "start": "2025-07-05T13:30:00Z",
     "end": "2025-07-05T14:30:00Z"
   }
   ```

3. **Event is added to Google Calendar.**

## 🔑 Environment Variables

Add the following to your Render → Secrets:

```toml
GROQ_API_KEY = "your_groq_api_key"
GOOGLE_CALENDAR_ID = "primary"

[google_credentials]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
client_email = "your_service_account_email"
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your_email"
universe_domain = "googleapis.com"
```

> **Note:** Escape newlines (`\n`) in `private_key`.

## 🧪 API Endpoints

### 1. 📥 Book Appointment

```bash
POST /book_appointment
```

**Body (JSON):**
```json
{
  "prompt": "book appointment with Zoro on 10th July from 6pm to 7pm"
}
```

**Response:**
```json
{
  "message": "Appointment booked with Zoro on 10 July 2025 from 06:00 PM to 07:00 PM IST."
}
```

### 2. 📅 Get Events by Date

```bash
POST /get_events
```

**Body (JSON):**
```json
{
  "date": "2025-07-10"
}
```

**Response:**
```json
{
  "date": "2025-07-10",
  "events": [
    {
      "summary": "Appointment with Zoro",
      "start": "2025-07-10T12:30:00Z",
      "end": "2025-07-10T13:30:00Z"
    }
  ]
}
```

## 📂 Project Structure

```
calendar-backend/
├── main.py
├── groq_utils.py
├── calendar_utils.py
├── requirements.txt
└── README.md
```

## ⏱ Timezones

- Input times are converted to **UTC (Z format)** for Google Calendar
- Displayed times are returned in **Indian Standard Time (IST)**

## 🌐 Live Deployment

FastAPI backend is deployed on Render:

🔗 **https://calendar-fastapi-backend.onrender.com/**

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Cloud Service Account with Calendar API enabled
- Groq API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd calendar-backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file with your API keys and credentials

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API:**
   - Local: `http://localhost:8000`
   - Documentation: `http://localhost:8000/docs`

## 📝 Usage Examples

### Book a simple appointment:
```bash
curl -X POST "http://localhost:8000/book_appointment" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Meeting with John tomorrow at 3pm for 1 hour"}'
```

### Get events for a specific date:
```bash
curl -X POST "http://localhost:8000/get_events" \
  -H "Content-Type: application/json" \
  -d '{"date": "2025-07-10"}'
```

## 🔧 Configuration

### Google Calendar Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Calendar API
4. Create a Service Account and download the JSON key
5. Share your calendar with the service account email

### Groq API Setup

1. Sign up at [Groq](https://groq.com/)
2. Generate an API key
3. Add it to your environment variables

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
