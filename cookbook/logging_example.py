#!python

# References: 
# http://cheesehead-techblog.blogspot.com/2013/01/logging-in-python-3.html
# https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/
# Adding colors:
# https://gist.github.com/juancarlospaco/eec9beddb03b34127f1a 
# Good logging practice in Python:
# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

import logging, os, sys

EXE_VERSION = '0.0.1'
EXE_NAME    = os.path.basename(sys.argv[0])

LOG_LEVEL = 'debug'

def init_log():
    # Ran into a bug where if I didn't define a name for getLogger, then log
    # output from other modules would start showing up.  Ran into this with
    # requests where log statements started showing up when I didn't have a name
    logger = logging.getLogger('logger')

    if LOG_LEVEL == 'debug':
        logger.setLevel(logging.DEBUG)
        # log_format = '%(asctime)s.%(msecs)d | %(module)s | %(funcName)s:%(lineno)d | %(levelname)s | %(message)s'
        log_format  = '%(asctime)s.%(msecs)d | %(funcName)s:%(lineno)d | %(levelname)s | %(message)s'
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

def main():
    log = init_log()

    log.info("[=============== BEGIN ===============]")
    log.info("%s %s starting...", EXE_NAME, EXE_VERSION)
    log.debug("Arguments passed: %s", sys.argv[1:])

    log.debug('debug message')
    log.info('info message')
    log.warning('warn message')
    log.error('error message')
    log.critical('critical message')

    log.info("%s finished, exitCode=0", EXE_NAME)
    log.info("[================ END ================]")

if __name__ == "__main__":
    main()
