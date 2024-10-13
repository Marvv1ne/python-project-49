install:
	poetry install
build:
	poetry build

publish:
	poetry publish --dry-run

poetry package-install:
	pipx install dist/*.whl

brain-games:
	poetry run brain-games