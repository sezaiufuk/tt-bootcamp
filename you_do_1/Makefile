all: data/binge.tar.gz


data/binge.tar.gz: 
	curl -L -o $@  https://storage.googleapis.com/sadedegel/dataset/binge.tar.gz

fix:
	uv run isort *.py
	uv run ruff check *.py  --fix
	uv run ruff format *.py