import time
import os
class CommonUtil:

  @staticmethod
  def setup_logger(logging, log_file):
    os.environ['TZ'] = 'Asia/Jakarta'
    time.tzset()
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)sz %(name)s %(levelname)s: %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=log_file,
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s: %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    logging.Formatter.converter = time.gmtime
    # add the handler to the root logger
    logging.getLogger().addHandler(console)  