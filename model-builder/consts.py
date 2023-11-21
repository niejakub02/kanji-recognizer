# VARIABLES
# Make sure to install "Noto Sans JP" font before hand
# as it's the font that displays nearly all of the
# japanese characters
matplotlib_title_font = {"fontname": "Noto Sans JP", "fontsize": 20}


# CONSTANTS
EPOCHS_COUNT = 30
CLASSES_COUNT = 20
LEARNING_RATE = 1e-4
BATCH_SIZE = 32


# CLASSES
class text_emphasis:
    CYAN = "\033[96m"
    PINK = "\033[95m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    UNDERLINE = "\033[4m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
