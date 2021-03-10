install:
	pip install --upgrade pip
	pip install -r src/requirements.txt

download:
	python -m nltk.downloader -d $(PWD)/nltk_data all-nltk

run:
	cd src && gunicorn app:app -w 4 -b 0.0.0.0:5000