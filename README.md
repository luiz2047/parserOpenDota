# OpenDota Full Matches Parser

This project is a Python script for parsing full match data from the OpenDota API, using a list of match IDs stored in a text file. The parsed data is saved in a JSON file for further analysis.
## Getting Started

To use this script, you will need to have Python 3.x installed on your system, along with the necessary dependencies. You can install the dependencies by running the following command in your terminal:

```pip install -r requirements.txt```

You will also need to obtain a list of match IDs from OpenDota and save them in a text file named ***`matches_ids.txt`***.
## Usage

To run the script, open a terminal window in the project directory and enter the following command:

```python main.py -n NUM_WORKERS```

Replace **`NUM_WORKERS`** with the desired number of worker processes to use for parsing. The default value is 16.

The script will start parsing the matches using external proxies, which will be obtained automatically. The parsed data will be saved in a file named **`full_matches.json`**.
## Contributing

Contributions to this project are welcome! If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.
## License

This project is licensed under the MIT License - see the LICENSE file for details.
