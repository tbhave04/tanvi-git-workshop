.PHONY: tests clean

setup:
	pip install uv 
	uv sync
	uv run hello.py

test:
	uv run -m unittest competition/test_code.py