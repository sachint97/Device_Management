FROM python:3.10

WORKDIR /Device_Management
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 
    
COPY . .

# CMD ["python", "manage.py", "makemigrate"]
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "mlt_demo.wsgi:application", "--bind", "0.0.0.0:8000"]
