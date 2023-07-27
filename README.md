# # Project Description

This Python script is designed to fetch an XML file from a specified URL, modify specific XML tags and save the updated XML content into a new file.

## Features

- Fetches an XML file from a specified URL using `requests`.
- Uses `BeautifulSoup` for parsing and manipulating the XML content.
- Modifies the content of the `g:item_group_id` tags to a specified value.
- Modifies the content of the `g:google_product_category` tags to a specified value.
- Saves the modified XML content into a new file with utf-8 encoding.

## Usage

1. Ensure that you have Python 3.x installed on your machine. The script was written and tested with Python 3.10, but it should work with other Python 3 versions.

2. Install the required Python packages if you have not done so already. You can do this by running the following command in your terminal:

```
pip install beautifulsoup4 requests
```

3. Clone the project or download the Python script file to your local machine.

4. Run the script by navigating to the directory containing the script and typing the following in your terminal:

```
python your_script.py
```
Replace `your_script.py` with the name of the script file.

The script will download the XML file, perform the modifications, and save the updated content into a new file named 'new_file.xml'.

## Scheduled Execution

If you want to run this script automatically on a schedule (e.g., every hour), you can use a tool like cron on Unix/Linux systems or Task Scheduler on Windows systems. Please refer to the documentation for these tools for detailed instructions on how to set this up.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
