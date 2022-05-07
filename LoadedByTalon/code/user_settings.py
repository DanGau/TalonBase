import csv
import glob
from pathlib import Path
from pickle import TRUE
from typing import Dict, List, Tuple
from talon import resource

# NOTE: This method requires this file to be two directories down from the talon user folder
USER_DIR = Path(__file__).parents[2]

def read_mapping_from_csv(
    filename: str, 
    expectedHeaders: Tuple[str, str]
):
    """Retrieves a mapping of spoken form to output from specified CSV file(s)"""

    # Search for all CSV files within settings folders that match the filename
    matchingFiles = glob.glob(str(USER_DIR) + '/**/settings/' + filename, recursive=TRUE)

    # Create our mapping out of the matched files
    mapping = {}
    for filepath in matchingFiles:
        # Open via talon's resource helper so this script is reloaded if the CSV is edited
        with resource.open(str(filepath), "r") as f:
            rows = list(csv.reader(f))
    
        # Convert the contents of the file into a mapping
        if len(rows) >= 2:
            # validate the headers are what we expect
            actual_headers = rows[0]
            if not actual_headers == list(expectedHeaders):
                print(
                    f'"{filename}": Malformed headers - {actual_headers}.'
                    + f" Should be {list(expectedHeaders)}. Ignoring row."
                )

            for row in rows[1:]:
                if len(row) > 0:
                    if row[0].startswith('#'):
                        # This line is a comment, Ignore it.
                        continue
                    if len(row) == 1:
                        # Single phrase entries represent both the spoken form and output
                        output = row[0]
                        spoken_form = row[0]
                    if len(row) == 2:
                        # Comma separated entries represent the output and then the spoken form 
                        output = row[0]
                        spoken_form = row[1]

                # Leading/trailing whitespace in spoken form can prevent recognition.
                spoken_form = spoken_form.strip()
                mapping[spoken_form] = output

    return mapping
