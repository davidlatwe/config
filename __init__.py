import sys
import os
from pyblish import api as pyblish

# Create an default alias "config" for this config package.
# ! This is for better sharing experience.
# When developing/sharing plugins or modules, you can/should import stuff
# which already provided from *vanilla config* with `config` namespace,
# instead of your local config name.
sys.modules["config"] = sys.modules[__package__]


PACKAGE_DIR = os.path.dirname(__file__)
PLUGINS_DIR = os.path.join(PACKAGE_DIR, "plugins")
PUBLISH_PATH = os.path.join(PLUGINS_DIR, "publish")
PYBLISH_DEFAULT = "%s/plugins" % os.path.dirname(pyblish.__file__)


def install():
    print("Registering global plug-ins..")
    pyblish.register_plugin_path(PUBLISH_PATH)
    # Remove pyblish-base default plugins
    pyblish.deregister_plugin_path(PYBLISH_DEFAULT)


def uninstall():
    pyblish.deregister_plugin_path(PUBLISH_PATH)
    # Restore pyblish-base default plugins
    pyblish.register_plugin_path(PYBLISH_DEFAULT)
