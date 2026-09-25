.PHONY: ia-dev front-dev ia-down front-down ia-logs front-logs ia-test

ia-dev:
	docker compose -f ai/docker-compose.yml up --build -d

front-dev:
	docker compose -f front/docker-compose.yml up --build -d

ia-down:
	docker compose -f ai/docker-compose.yml down

front-down:
	docker compose -f front/docker-compose.yml down

ia-logs:
	docker compose -f ai/docker-compose.yml logs -f

front-logs:
	docker compose -f front/docker-compose.yml logs -f

ia-test:
	docker compose -f ai/docker-compose.yml run --rm ia pytest