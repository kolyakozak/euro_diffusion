INPUT_FILE = "input.txt"

INITIAL_CITY_MOTIF = 1_000_000
FULL_PORTION = 1_000

COLORS = [
    "\x1b[31m" , # F_Red
    "\x1b[32m", # F_Green
    "\x1b[33m", # F_Yellow
    "\x1b[34m", # F_Blue
    "\x1b[35m", # F_Magenta
    "\x1b[36m", # F_Cyan
    "\x1b[37m", # F_LightGray
    "\x1b[91m", # F_LightRed
    "\x1b[92m", # F_LightGreen
    "\x1b[90m", # F_DarkGray
    "\x1b[93m", # F_LightYellow
    "\x1b[94m", # F_LightBlue
    "\x1b[95m", # F_LightMagenta
    "\x1b[96m", # F_LightCyan
    "\x1b[97m" # F_White
]
END_COLOR = "\033[0m"

MAX_COUNTRIES = len(COLORS)