import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(meaasge)s]"


log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    formate=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHnadler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifier")