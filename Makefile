.PHONY: setup synthetic validate test quality train-smoke api demo build clean
setup:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"
synthetic:
	cpathlab generate-synthetic --output data/example --samples 40
validate:
	cpathlab validate-data --image-dir data/example/images --labels data/example/labels.csv
train-smoke: synthetic
	cpathlab train-synthetic --data-dir data/example --epochs 1 --output models/demo.pt

test:
	pytest -q
quality:
	ruff check src tests scripts
	mypy src/cpathlab --ignore-missing-imports
api:
	uvicorn cpathlab.api.main:app --host 0.0.0.0 --port 8000
demo:
	streamlit run app/streamlit_app.py
build:
	python -m build
clean:
	python -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in map(pathlib.Path, ['build','dist','.pytest_cache','.mypy_cache','.ruff_cache','htmlcov'])]"
