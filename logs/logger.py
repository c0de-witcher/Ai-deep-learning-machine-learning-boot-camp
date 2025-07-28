import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%M-%D %H:%M:%S'
)