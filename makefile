#makefile

install: #установка через poetry
	poetry install

brain-games: #запуск игры
	poetry run brain-games

build:
	poetry build #собираем пакет

publish:
	poetry publish --dry-run #отладка публикации

package-install:
	python3.10 -m pip install --user dist/*.whl #установка пакета

lint: #проверка линтером
	poetry run flake8 brain_games
