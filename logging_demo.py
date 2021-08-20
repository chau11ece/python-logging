import logging
import os
import sys
import auxiliary_module as aux

file_dir = os.path.dirname("auxiliary _module.py")
sys.path.append(file_dir)


# sys.path.append("scripting/auxiliary _module.py")

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# create a file handler which logs even debug messages (FILE HANDLER)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level (CONSOLE HANDLER)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = aux.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')

logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')

logger.info('calling auxiliary_module.some_function()')
aux.some_function()
logger.info('done with auxiliary_module.some_function()')

# anh Chau dep trai 123, hehe, haha
# I have changed codes intentionally
