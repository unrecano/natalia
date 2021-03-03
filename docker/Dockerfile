FROM python:3.8
RUN mkdir /code
WORKDIR /code
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
RUN python -m nltk.downloader -d /usr/local/share/nltk_data all-nltk
CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:5000"]