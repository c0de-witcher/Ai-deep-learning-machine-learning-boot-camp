import logging

logger = logging.getLogger('ArithmeticLogger')

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s -%(name)s - %(levelname)s - %(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]

)

def add(x,y):
    result = x+y
    logger.debug(f"Adding {x} and {y} gives {result}")
    return result

def subtract(x,y):
    result = x-y
    logger.debug(f"Subtracting {y} from {x} gives {result}")
    return result  

def multiply(x,y):
    result = x*y
    logger.debug(f"Multiplying {x} and {y} gives {result}")
    return result

def divide(x,y):
    if y == 0:
        logger.error("Division by zero attempted")
        return None
    result = x/y
    logger.debug(f"Dividing {x} by {y} gives {result}")
    return result

add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)
divide(10, 5)