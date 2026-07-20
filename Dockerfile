# استخدام نسخة بايثون خفيفة ورسمية
FROM python:3.11-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المكتبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ بقية ملفات الكود إلى الحاوية
COPY app.py .

# تشغيل التطبيق باستخدام gunicorn وهو خادم الإنتاج الموصى به لـ Flask
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app"]