import pyblish.api


class SelectExample(pyblish.api.Action):
    label = "Select Example"
    on = "failed"

    def process(self, context, plugin):
        from maya import cmds
        cmds.select(plugin.example_list)


class ValidateExample(pyblish.api.InstancePlugin):
    """Validate instance.data example"""

    label = "Validate Example"
    families = ["config.example"]
    order = pyblish.api.ValidatorOrder
    hosts = ["maya"]
    actions = [
        pyblish.api.Category("Actions"),
        SelectExample,
    ]

    example_list = []

    def process(self, instance):
        self.example_list[:] = instance.data["example"]

        if not self.example_list:
            raise Exception("No example found.")

        if len(self.example_list) != 1:
            self.example_list = '"%s"' % '", "'.join(self.example_list)
            raise Exception(
                "Multiple examples found: %s" % self.example_list
            )
