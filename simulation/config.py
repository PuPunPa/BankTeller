RANDOM_SEED = 42
MIN_NEW_CUSTOMERS = 10          # Initial total number of customers
MAX_NEW_CUSTOMERS = 100         # Final total number of customers
STEPS = 10                      # Customer Step length
INTERVAL_CUSTOMERS = 3.0        # Generate new customers roughly every x seconds
MIN_PATIENCE = 1                # Min. gen_customer patience
MAX_PATIENCE = 5                # Max. gen_customer patience
MIN_CAPACITY = 2                # The minimum capacity of our resource
MAX_CAPACITY = 6               # The maximum capacity of our resource
C_STEPS = 1                      # Teller Step length
TIME_IN_BANK = 10.0             # The max time an operation can take
REPORT_STEP_BY_STEP = False     # Flag to report step by step events
REPORT_QUEUE = False            # Flag to report step by step the state of the queue
CREATE_SIM_GRAPHS = False        # Flag to create the graphs of the collected data
