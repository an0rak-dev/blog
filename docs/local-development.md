# Local development of this blog.

## Prerequisites

You'll need: 
* Python 3 (tested with 3.11)
* Open a terminal in the `generator` folder.

## Setting up your environment

First, you'll need to setup a virtual environment, to avoid messing with your
entire system and the other Python project you may have in it.

```sh
export VENV_LOCATION=<...> # Replace this value with the location where you want your venv to be saved.
python3 -m venv $VENV_LOCATION
source ${VENV_LOCATION}/bin/activate
cd src
python3 -m pip install -r requirements.txt
```

## Run the project

To run the project :

```sh
python3 src/generator/main.py http://localhost:8000
python3 -m http.server -d dist/ &
```