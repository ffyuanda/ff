MODULE_PATH = "C:/Users/ThinkPad/Desktop/pycasbin/casbin/__init__.py"
MODULE_NAME = "casbin"
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
import casbin

# e = casbin.Enforcer("path/to/model.conf", "path/to/policy.csv")