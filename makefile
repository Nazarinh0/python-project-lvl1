#makefile

install:
	poetry install #установка через poetry

brain-games:
	poetry run brain-games #запуск игры

brain-even:
	poetry run brain-even #запуск игры Even

brain-calc:
	poetry run brain-calc #запуск игры Calculation

build:
	poetry build #собираем пакет

publish:
	poetry publish --dry-run #отладка публикации

package-install:
	python3.10 -m pip install --user dist/*.whl #установка пакета

lint:
	poetry run flake8 brain_games #проверка линтером
