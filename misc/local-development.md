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

In order to avoid commiting (for nothing) the generated site. Paste the 
[pre-commit hook](./pre-commit) into your `.git/hooks` folder.

## Run the project

To run the project :

```sh
python3 src/generator/main.py
python3 -m http.server -d docs/ &
```