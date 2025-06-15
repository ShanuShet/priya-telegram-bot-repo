# Django Project with DRF, Celery, and Telegram Bot

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=False
   DATABASE_URL=your_database_url
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

- `SECRET_KEY`: Django secret key for security.
- `DEBUG`: Set to `False` for production.
- `DATABASE_URL`: Database connection URL.
- `TELEGRAM_BOT_TOKEN`: Token for your Telegram bot.

## How to Run Locally

1. Ensure your virtual environment is activated.
2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Access the API at `http://localhost:8000/api/`.

## API Documentation

### Public Endpoint
- **URL**: `/api/public/`
- **Method**: GET
- **Description**: Accessible to everyone.

### Protected Endpoint
- **URL**: `/api/protected/`
- **Method**: GET
- **Description**: Accessible only to authenticated users. Requires a valid token. 