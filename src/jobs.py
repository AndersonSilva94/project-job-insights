from functools import lru_cache
import csv


@lru_cache
def read(path):
    # commit inicial
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        list_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = [
            job for job in list_csv
        ]
        return jobs_list
