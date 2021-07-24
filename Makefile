run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
enter:
	docker-compose exec python-prototypes /bin/bash
start:
	docker-compose exec python-prototypes pipenv run start
lint:
	docker-compose exec python-prototypes pipenv run lint
format:
	docker-compose exec python-prototypes pipenv run format
log:
	docker-compose logs -f python-prototypes