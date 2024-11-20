################################### Start a Car ################################################
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
    
def fuel_level(litres):
    if litres >= 10 and litres <= 65:
        logging.info(f"Fuel level is {litres}")
        return True
    elif litres > 65:
        logging.debug("Too much fuel. Please enter a number bellow 65")
    elif litres < 10:
        logging.warning("Fuel low. Please refil")
        return True
    else:
        logging.critical("No fuel left. Please refil")
        return False
       
def oil_level(litres):
    if litres >= 2 and litres < 8:
        logging.info(f"Oil level is {litres}")
        return True
    elif litres <= 2:
        logging.warning("Oil level low.")
        return True
    elif litres > 8:
        logging.debug("Too much oil. Please enter a number bellow 8")
    else:
        logging.critical("No oil left.")
        return False

def engine_status(condition): 
    if condition == "okay":
        logging.info("Engine condition is okay")
        return True
    elif condition == "bad":
        logging.critical("Engine condition critical. Can't start the car.")
        return False

def start_car(fuel_litres: int, oil_litres: int, engine_condition: str ):
    fuel = fuel_level(fuel_litres)
    oil = oil_level (oil_litres)
    engine = engine_status(engine_condition)

    if fuel is True and oil is True and engine is True:
        logging.info("Engine has started. Good Trip!")
    if fuel is False:
        logging.info("Engine hasn't started.")
    elif engine == False:
        logging.info("Engine hasn't started")

start_car(8, 1, "okay")