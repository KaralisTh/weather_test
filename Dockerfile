# Επιλέξτε μια εικόνα βάσης για το Python
FROM python:3.9-slim

# Ορίστε το Working Directory στο Docker Container
WORKDIR /app

# Αντιγράψτε το αρχείο requirements.txt στον Container
COPY requirements.txt .

# Εγκαταστήστε τις βιβλιοθήκες που απαιτούνται
RUN pip install --no-cache-dir -r requirements.txt

# Αντιγράψτε τον υπόλοιπο κώδικα στον Container
COPY . .

# Ορίστε την εντολή που θα εκτελείται όταν ξεκινήσει ο container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
