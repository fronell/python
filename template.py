#!python
################################# DESCRIPTION #################################
"""
This is a template that can be used for writing new scripts
"""


################################### IMPORTS ###################################
import datetime
import logging
from optparse import OptionParser
import os
import pprint
import sys


################################## CONSTANTS ##################################
EXE_VERSION = "0.0.1"
# basename is used to strip the ./ if the script is executed from the local dir
EXE_NAME    = os.path.basename(sys.argv[0])
LOG_LEVELS  = ("debug", "info", "warn", "error")


################################### GLOBALS ###################################
pp = pprint.PrettyPrinter(indent = 2)


################################### CLASSES ###################################


################################## FUNCTIONS ##################################
def init_log(log_level, verbose):
    logger = logging.getLogger("logger")

    if log_level == "debug":
        logger.setLevel(logging.DEBUG)
    elif log_level == "info":
        logger.setLevel(logging.INFO)
    elif log_level == "warn":
        logger.setLevel(logging.WARN)
    elif log_level == "error":
        logger.setLevel(logging.ERROR)
    
    if verbose:
        log_format  = "%(asctime)s.%(msecs)d | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s"
        #log_format = "%(asctime)s.%(msecs)d | %(levelname)s | %(module)s | %(funcName)s:%(lineno)d | %(message)s"
    else:
        # -5s for levelname left justifies so INFO,DEBUG,ERROR columns line up
        log_format  = "%(asctime)s.%(msecs)d | %(levelname)-5s | %(message)s"
        
    date_format = "%Y-%m-%d %I:%M:%S"
    formatter   = logging.Formatter(log_format, date_format)
    console     = logging.StreamHandler()
    
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger


############################### OPTION PARSING ################################
opts_parser = OptionParser(version="%prog {}".format(EXE_VERSION))
opts_parser.add_option("-l", 
                       "--log_level", 
                       choices=LOG_LEVELS, 
                       default="debug", 
                       help="choices are {} [default: %default]".format(LOG_LEVELS))
opts_parser.add_option("-v", 
                       "--verbose", 
                       action="store_true", 
                       default=False,
                       help="Add additional info to each log line [default: %default]")
(opts, args) = opts_parser.parse_args()

num_args_required = 0
num_args_passed   = len(args)

if num_args_passed != num_args_required:
    opts_parser.error("Args passed={}, Args required={}".format(num_args_passed, num_args_required))
    
log = init_log(opts.log_level, opts.verbose)


#################################### MAIN #####################################
startTime = datetime.datetime.now()

log.info("action=App:Start app_name=%s app_version=%s", EXE_NAME, EXE_VERSION)
log.debug("arguments=%s", sys.argv[1:])
log.warn("This is a warning")
log.error("This is an error")

duration = datetime.datetime.now() - startTime
log.info("action=App:End duration_seconds=%d", duration.seconds)
