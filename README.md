Sure, here is how your `README.md` file might look in English:

```
# XML Feed Modifier
This project is used to modify XML feeds served on a web server. The code is written in Python and uses the BeautifulSoup library for parsing and modifying the files, and the Flask library for setting up the web application.

## Requirements
To run this project, you will need to install the following dependencies:

- Python 3
- BeautifulSoup4
- Flask
- requests

You can install these dependencies using pip:

```
pip install -r requirements.txt
```

## Usage
First, run `generate.py` to download, parse, modify an XML file, and save the result:

```
python generate.py
```

Then, you can run `app.py` to start the application which will serve the modified file when accessed at the root of the application:

```
python app.py
```

The application will be available at `http://localhost:5000` (or whichever IP address you specify).

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
```

Above the code blocks, there should be a blank line for it to be rendered properly on GitHub. Ensure all code and formatted text are between three backticks (\```) for code block marking.
