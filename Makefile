run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
enter:
	docker-compose exec django /bin/bash
start:
	docker-compose exec django pipenv run start
lint:
	docker-compose exec django pipenv run lint
format:
	docker-compose exec django pipenv run format
log:
	docker-compose logs -f django
