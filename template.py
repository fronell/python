#!python
################################# DESCRIPTION #################################
'''
'''


################################### IMPORTS ###################################
import datetime, logging, os, pprint, sys
from optparse import OptionParser


################################## CONSTANTS ##################################
EXE_VERSION = '0.0.1'
# basename is used to strip the ./ if the script is executed from the local dir
EXE_NAME    = os.path.basename(sys.argv[0])


################################### GLOBALS ###################################
pp = pprint.PrettyPrinter(indent = 2)


################################## FUNCTIONS ##################################
def init_log(log_level):
    logger = logging.getLogger('logger')

    if log_level == 'DEBUG':
        logger.setLevel(logging.DEBUG)
        # log_format = '%(asctime)s.%(msecs)d | %(module)s | %(funcName)s:%(lineno)d | %(levelname)s | %(message)s'
        log_format  = '%(asctime)s.%(msecs)d | %(funcName)s:%(lineno)d | %(levelname)-5s | %(message)s'
        date_format = '%Y-%m-%d %I:%M:%S'
        formatter   = logging.Formatter(log_format, date_format)
    else:
        logger.setLevel(logging.INFO)
        log_format  = '%(asctime)s.%(msecs)d | %(levelname)s | %(message)s'
        date_format = '%Y-%m-%d %I:%M:%S'
        formatter   = logging.Formatter(log_format, date_format)

    # Console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger


############################### OPTION PARSING ################################
opts_parser = OptionParser(version="%prog " + EXE_VERSION)
opts_parser.add_option('-d', '--debug', action='store_true', 
                       help='Enable debug logging')
(opts, args) = opts_parser.parse_args()

#if len(args) != 1:
#    parser.error("incorrect number of arguments")
if opts.debug:
    log = init_log('DEBUG')
else:
    log = init_log('INFO')


#################################### MAIN #####################################
startTime = datetime.datetime.now()

log.info("[=============== BEGIN ===============]")
log.info("%s %s starting...", EXE_NAME, EXE_VERSION)
log.debug("Arguments passed: %s", sys.argv[1:])

duration = datetime.datetime.now() - startTime
log.info("status=Complete duration_seconds=%d", duration.seconds)
log.info("[================ END ================]")
