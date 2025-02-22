# Quickstart

0. Tested on Python 3.10.0 (see instructions below to setup `pyenv`)

1. Install and start the server

   ```
   python3 -m venv env
   source env/bin/activate
   pip3 install -r requirements.txt
   python3 server.py
   ```

2. Navigate to http://127.0.0.1:7777/index.html

If you run into issues with `pip3 install -r requirements.txt` in step 1., this may be due to a Python version incompatibility issue. Try following "Manual Installion" instead.

# Manual Install

1. Initialize and activate virtual python environment

```
python3 -m venv env
source env/bin/activate
```

2. Install flask

```
pip3 install flask
```

3. Start server

```
python3 server.py
```

4. Navigate to http://127.0.0.1:7777/index.html

# Setting up PyEnv for MacOS

```
brew install pyenv
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
pyenv install 3.10.0
pyenv local
```
