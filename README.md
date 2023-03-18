# OpenDota Match Data Parser

This Python script uses the OpenDota API to parse full matches data and save it as JSON files. It includes proxy support to avoid rate limiting and enhance performance.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies using pip: ```pip install -r requirements.txt```
3. Create a file named ```matches_ids.txt``` in the same directory as the main.py file. Put each match ID on a separate line in this file.
4. Run the script with the desired number of workers: ```python main.py -n [num_workers]```

## Arguments

- -n, --num_workers: the number of workers to use for parsing. Default is 128.

## Output

The parsed JSON files will be saved in the `data` folder, with filenames corresponding to the match IDs.

## Proxy Support

This script includes proxy support to avoid rate limiting and enhance performance. The script will automatically cycle through a list of free proxies obtained from the `proxy` module. If a proxy fails, the script will try the next one in the list.

## Logging

The script logs debugging and error messages to the `logs.log` file in the same directory as the `main.py` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
