.PHONY: tests clean

setup:
	pip install uv 
	uv sync
	uv run hello.py

test:
	uv run -m unittest discover -s tests -p "*_test.py"