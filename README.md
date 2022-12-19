# Python | Flask | URL-Shortener | File storage website

The app will allow users to generate a reduced version by entering a URL and a special code. Users will also have the option of uploading files.

## Getting Started

- Python 3.7+
- [Pipenv](https://pypi.org/project/pipenv/)

## Quickstart

1. Clone the application using the following command:

   ```bash
   git clone https://github.com/henrymbuguak/flask-url-shortener.git
   ```

1. To navigate to the project directory, use the following command:

   ```bash
   cd flask-url-shortener
   ```

1. Execute the following command to create and activate a virtual environment:

   ```bash
   pipenv shell
   ```

1. To install the required PyGithub package, execute the following command:

   ```bash
   pipenv install
   ```

1. In `flask-url-shortener/url_short/url_short.py` file, update line 30 to your project directory.
1. Set the `FLASK_APP` environment by executing the following command:

   ```bash
   export FLASK_APP=url_short
   ```

1. Set Flask's environment to development mode by executing the following command:

   ```bash
   export FLASK_DEBUG=true
   ```

1. To test the app, execute the following command:

   ```bash
   flask run
   ```

1. In your browser, navigate to `http://127.0.0.1:5000`.
