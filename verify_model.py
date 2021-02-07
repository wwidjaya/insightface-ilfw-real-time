import settings
from util import CommonUtil as cu
from verification import parse_args, verify_model

args = parse_args()
verify_model(args)
