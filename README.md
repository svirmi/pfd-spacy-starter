# pfd-spacy-starter
 Poetry, FastAPI, Docker, Spacy starter template

```bash
$HOME/.poetry/bin/poetry shell
(inside-shell) ~/pfd-spacy-starter/src$ uvicorn src.main:app --reload
```

Swagger http://127.0.0.1:8000/docs

```bash
docker build -t pfd-spacy-starter .
docker run -d -p 8888:8888 pfd-spacy-starter
```