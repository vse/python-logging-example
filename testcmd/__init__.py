import logging
log = logging.getLogger(__name__)

# this is never run since we never directly import `testcmd` only `testcmd.sub`
log.debug("initializing testcmd module")