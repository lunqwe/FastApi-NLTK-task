# README

## Project details

This project is an implementation of API for interaction with NTKL library (Natural Language Toolkit)

## Setup

1. Clone repository:
    ```bash
    git clone https://github.com/lunqwe/FastApi-NLTK-task.git
    cd FastApi-NLTK-task
    ```

2. Create and activate venv:
    ```bash
    python -m venv venv
    ```
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        source venv/bin/activate
        ```



4. Встановіть необхідні пакети:
    ```bash
    pip install -r req.txt
    ```

## Run and test

1. Run server using:
    ```bash
    uvicorn main:app --reload
    ```

2. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for project documentation and interactive API preview
