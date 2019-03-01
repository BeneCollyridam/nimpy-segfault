# nimpy-segfault
Minimal example of a segfault in Django using a compiled Nimpy binary

# Setup
- Install [Python](https://python.org), [pip](https://pip.pypa.io/en/stable/installing/), and [Nim](http://nim-lang.org/)
- Install the requirements with `pip install -r requirements.txt`
- Run the following command to create the database `python manage.py migrate`
- cd to the folder testapp/compiled and run the command:
  -  `nim c --app:lib --out:mylib.so mylib`
- Start the server by running `python manage.py runserver`

The service should now be available on [http://localhost:8000](http://localhost:8000)

# Models
Two models have been created in the database. They are from the official Django tutorial.
- `Question`: has two fields: `question_text` and `pub_date`
- `Choice`: has three fields: `question` - a foreign key to a `Question`, `choice_text`, and `votes`.

# Endpoints
Three endpoints should now be available at [http://localhost:8000](http://localhost:8000)
- `/test` - Shows  all `Question`s
- `/generate-questions` - Generates 10 `Question`s with 1-5 `Choice`s
- `/nim` - Runs the endpoint that uses Nim
