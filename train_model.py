from mxnet.symbol.gen_op import argsort
import settings
from train import start_train, parse_args

args = parse_args()
start_train(args)