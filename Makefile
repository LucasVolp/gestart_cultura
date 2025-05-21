.PHONY: venv install clean

VENV_DIR=venv

venv:
    python -m venv $(VENV_DIR)

install: venv
    $(VENV_DIR)/bin/python -m pip install --upgrade pip
    $(VENV_DIR)/bin/python -m pip install -r requirements.txt

clean:
    rm -rf $(VENV_DIR)