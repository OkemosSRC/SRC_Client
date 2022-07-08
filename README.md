# SRC_Client

A simple python client for the [SRC_Server](https://github.com/OkemosSRC/SRC_Server).

## Usage

```
python src_client.py speed|battery
```

## Install

##### MacOS/Linux

```bash
git clone https://github.com/OkemosSRC/SRC_Client.git
cd SRC_Client
# create a virtual environment
python3 -m venv venv
source venv/bin/activate
# install dependencies
pip install -r requirements.txt
# add executable permissions
python src_client.py speed
# or 
python src_client.py battery
```

##### Windows

```bash
git clone https://github.com/OkemosSRC/SRC_Client.git
cd SRC_Client
# create a virtual environment
python3 -m venv venv
. venv\Scripts\activate
# install dependencies
pip install -r requirements.txt
python src_client.py speed
# or 
python src_client.py battery
```
