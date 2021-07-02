import logging
log = logging.getLogger(__name__)


log.warn('using old submodule')
log.debug('lots of debug stuff happening here..')
log.debug('even more debug stuff..')

def func_from_sub(args):
    log.debug('called func_from_sub')
    log.debug('we are inside a func in testcmd.sub and debug')
    pass