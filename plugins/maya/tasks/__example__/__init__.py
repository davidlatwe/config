import os
from pyblish import api as pyblish
from avalon import api as avalon


TASK_DIR = os.path.dirname(__file__)
PUBLISH_PATH = os.path.join(TASK_DIR, "publish")
LOAD_PATH = os.path.join(TASK_DIR, "load")
CREATE_PATH = os.path.join(TASK_DIR, "create")


def install():
    pyblish.register_plugin_path(PUBLISH_PATH)
    avalon.register_plugin_path(avalon.Loader, LOAD_PATH)
    avalon.register_plugin_path(avalon.Creator, CREATE_PATH)


def uninstall():
    pyblish.deregister_plugin_path(PUBLISH_PATH)
    avalon.deregister_plugin_path(avalon.Loader, LOAD_PATH)
    avalon.deregister_plugin_path(avalon.Creator, CREATE_PATH)
