# IPP project 2 tests
## Usage:
```
pytest
```
## Before download:
```
Remove remote connection to ipp-core repo first.
git remote remove origin
```
## Download:
```
# Download into ipp-core, NOT student/
git clone git@github.com:Kubikuli/tests2.git tests
```
## Setup:
```
# in root dir
python -m venv .venv # create virtual environment if you don't have one yet
source .venv/bin/activate
pip install -r tests/requirements.txt # install required packages
```
## Update:
```
git pull # in tests directory
```
## Notes:
Tag or DM me if you see any issues. (@Kubikuli)
If you'd like to contribute to tests, create a pull request.
You can find basic skeleton at the start of each test file that you can use to create new tests. 
