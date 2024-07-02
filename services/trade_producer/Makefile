build:
	docker build -t trade-producer .

run:
	docker run --network redpanda_network trade-producer

lint:
	poetry run ruff check --fix

format:
	poetry run ruff format .

lint-and-format:
	lint format
	