import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)    # ✅ Fix: Use os.path.join() to create file path
os.makedirs(logs_path,exist_ok=True)  # ✅ Fix: Create logs directory if it doesn't exist



LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)  # ✅ Fix: Use os.path.join() to create file path

logging.basicConfig(filename=LOG_FILE_PATH,level=logging.INFO,
                    format="[%(asctime)s] [%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] [%(message)s]")  # ✅ Fix: Set logging level to DEBUG


                    
                     