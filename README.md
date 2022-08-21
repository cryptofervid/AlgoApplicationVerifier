# AlgoApplicationVerifier

This is an open source application to verify deployed algorand applications with their source code. In the current version both `Teal` and `PyTeal` based source codes are supported.

## Hosted Application

The application is currently hosted on Heroku Platform and can be accessed using the following url: https://cryptofervid.herokuapp.com/validationapi/applications

## Local Setup

Prerequisites:
- Python 3 must be installed

To setup the application locally perform the following steps:

- Clone the git repository
```
git clone https://github.com/cryptofervid/AlgoApplicationVerifier.git
```
- Go to the directory
```
cd AlgoApplicationVerifier
```
- Create a virtual environment for python
```
python3 -m venv venv
```
- Activate the virtual environment
```
. venv/bin/activate
```
- Install the required dependencies
```
pip3 install -r requirements.txt
```
- Initialize local database
```
python3 init_db.py
```

## Design

The application has been developed using the following:

- Frontend: Flask Templates
- Backend: Flask
- Database: Sqlite3

## Limitations

The application supports `PyTeal` source code but the application expects a source code url and a method name that returns a PyTeal construct that can be compiled into teal code.

## Possible Enhancements

- Support for Reach
- UI/UX improvements
- Better error handling
- Docker Support

