# Fast_API_Setup
This provides a basic set up to use the fast API

To set up the virtual environment, in your terminal type
Mac: "python -m venv venv" then "source venv\bin\activate"
windows: "python -m venv venv" then "venv\Scripts\activate"

To install Flask and the uvicorn server:

'pip install fastapi' and 'pip install "uvicorn[standard]"'

after to run the server type in your terminal "uvicorn yourfile:app --reload"

For more info, follow https://fastapi.tiangolo.com/
