# Telegram Bot API

## Description
This Django-based backend project demonstrates REST API development, authentication, background task processing, and Telegram bot integration. It includes public and protected API endpoints secured using TokenAuth or JWT. Celery with Redis handles asynchronous tasks like sending welcome emails on user registration. A Telegram bot is integrated via the Telegram Bot API—when a user sends the /start command, their ID and username are saved to the database.


  
<h2>🛠️ Installation Steps:</h2>

1. Clone the repository:

```CMD
git clone https://github.com/aditya-Kumar421/telegram_bot.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install and Create a virtual environment:

```CMD
python -m venv env
```

3. Activate the virtual environment

```CMD
env\Scripts\activate
cd tele_bot
```

4. Install the dependencies:

```CMD
pip install -r requirements.txt
```

5. Set Up Database:

```
python manage.py migrate
```

6. Run the Development Server:

```
python manage.py runserver
```
7. Run Celery Worker (in a separate terminal)

```
celery -A tele_bot worker --pool=solo -l info
```
8. Run Telegram Bot (in another terminal)

```
python manage.py runbot
```


9. Access the Endpoints:


## 🔗 API Routes

| Method | Endpoint            | Description                                  |
|--------|---------------------|----------------------------------------------|
| POST   | `/api/register`     | Register a new user and receive a token.     |
| POST   | `/api/login`        | Login using credentials and get auth token.  |
| GET    | `/api/profile`      | Retrieve the profile of the authenticated user. |
| POST   | `/api/logout`       | Logout the current user (token invalidation). |

### 🤖 Telegram Bot Endpoints

| Method | Endpoint              | Description                                |
|--------|-----------------------|--------------------------------------------|
| GET    | `/telegram/users/`    | Retrieve all Telegram users who started the bot. |

---

## 🛠️ Environment Variables

Create a `.env` file in your project root with the following keys:

```env
SECRET_KEY=your_django_secret_key

UPSTASH_REDIS_HOST=your_upstash_redis_host
UPSTASH_REDIS_PORT=your_redis_port
UPSTASH_REDIS_PASSWORD=your_redis_password

EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```
## 🤖 Using the Telegram Bot

- Go to [@aadi303_bot](https://t.me/aadi303_bot)
- Send `/start`
- The bot will respond and your Telegram **username** + **ID** will be stored in the database.
- To view all users, visit:  
  [`http://127.0.0.1:8000/telegram/users/`](http://127.0.0.1:8000/telegram/users/)

---

## 🔐 Authentication & API Usage

- Register a new user at:  
  `POST /api/register`
- Use the returned **token or JWT** to access protected endpoints.

---

## 📬 API Documentation

- Postman API Collection: [Postman Docs](https://documenter.getpostman.com/view/41200302/2sB2x6msFo)

---

## 🧩 Technologies Used

- Django + Django REST Framework  
- Celery with Redis (Upstash)  
- Telegram Bot API  
- Python-decouple for environment configuration

---

## 📌 Notes

- Ensure **Redis URL** from Upstash is correctly configured.
- Webhook setup for Telegram should be done via [Telegram Bot API](https://core.telegram.org/bots/api#setwebhook).
- Run **Celery** and the **Telegram bot** in separate terminals alongside the Django server.

