import csv
from datetime import datetime
import re
import logging
import sys

logging.basicConfig(
    format='[%(asctime)s][%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
    handlers=[logging.FileHandler("RPA.log"), logging.StreamHandler(sys.stdout)]
)

class Tools:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def to_csv(cls, name:str, header:list= [], rows_to_save:list = [], path:str="", delimiter:str=",") -> bool:
        if not name.endswith(".csv"):
            name += ".csv"

        logging.info("Trying to save csv file")
        try:
            with open(path+name, "w") as file:
                w = csv.writer(file, delimiter=delimiter)

                if header: w.writerow(header)
                w.writerows(rows_to_save)

            logging.info(f"Successfully saved to: {path+name}")
            return True
        except Exception as e:
            logging.error("Error when saving")
            return False
    
    @classmethod
    def is_expired(cls, date:str) -> bool:
        date = re.sub(r"[\-\.\/]", "/", date)
        date = datetime.strptime(date, "%d/%m/%Y")
        return date >= datetime.now()