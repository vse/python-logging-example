import logging
import logging.config


# configure the logging module before module/submodule loggers get instanciated
# basicConfig configures a bare minumum root logger that dumps the stream to stdout
# logging.basicConfig()  

# logging.basicConfig(level='INFO')

# logging.config.fileConfig('logging_config.cfg', disable_existing_loggers=True)

# overwrite settings from `basicConfig`
logging.config.fileConfig('logging_config.cfg', disable_existing_loggers=True)

log = logging.getLogger(__name__)

log.debug("initializing main")

from .util import func_from_util
from .sub import func_from_sub

def main():
    log.info('in main')
    func_from_util('arg')
    func_from_sub('arg')
    
if __name__ == '__main__':
    log.info('running main from global scope')
    main()
    log.info('main finished')