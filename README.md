# Talk2API
This project demonstrates the execution of APIs using queries typed in natural language

## What we did?
In this project we are going to Talk to the [Genderize.io](https://genderize.io/), [Nationalize.io](https://nationalize.io/) and [Agify.io](https://agify.io/) APIs using plain english language. Also, convert the responses back into human readiable english language

## Why we did?
This project is done to explore the possibility of applying latest AI progress in NLP in creating domain driven, goal oriented chat bots with a flexibility of even going out of domain if required.

## How we did?

### High Level Design

![Talk2APIArhcitecture](./figures/Talk2API_Architecture.jpg)

### Mid Level Design

* An agent driven by 3 tools.
* Tools detect the intent of the user
* Each tool will be using the extraction chain to extract the necessary information and call its respective API
* Once the response is got from the respective API, separate prompts are constructed to generate a natural response

## Getting started with development

### Pre-requisites

[Anaconda Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

> conda create --name talk2api python

> conda activate talk2api

### Setup, Build and Run

> git clone https://github.com/sheikirfanbasha/Talk2API.git

> cd Talk2API

> pip install -r requirements.txt

> export OPENAI_API_KEY=<your_openai_api_key>

> streamlit run talk2api

### Known Issues and Fixes

| Error      | Fix |
| ----------- | ----------- |
| ModuleNotFoundError: No module named 'langchain.chat_models'   | pip install langchain --upgrade        |


## Useful for stepwise understanding

### Extraction of Entities

> python experiments/extractEntities.py

```
[{'name': 'Alex', 'height': 5, 'hair_color': 'blonde'}, {'name': 'Claudia', 'height': 6, 'hair_color': 'brunette'}]
```