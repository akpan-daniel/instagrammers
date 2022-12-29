[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Instagrammers

Instagrammers is an instagram influencer search portal.

## Setup
Clone this repo
```bash
git clone git@github.com/roronoazor/instagrammers.git
```
Create a virtual environment using an env manager of your choice(virtualenv, conda, pipenv etc), activate your environment and install project requirements using `pip`

```bash
pip install -r requirements.txt
```

Create .env file with .env.example reference
```bash
# migrate db
alembic upgrade head
```


## Running

```bash
# run on port 8000 by default
uvicorn app.main:app
# visit 127.0.0.1:8000/docs
```

Prefer to use docker?
```bash
docker compose up -d
docker exec ig_api alembic upgrade head
```

# Testing
```bash
# install test requirements
pip install requirements.test.txt

# run test
pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
```bash
# install dev dependecies
pip install requirements.local.txt

# install pre-commit
pre-commit install
```

Please make sure to update tests as appropriate.
