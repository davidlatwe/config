import pyblish.api
import tempfile


class ExtractExample(pyblish.api.InstancePlugin):
    """Extract eample Maya scene file"""

    label = "Extract Example"
    families = ["config.example"]
    order = pyblish.api.ExtractorOrder
    hosts = ["maya"]

    def process(self, instance):
        import os
        from maya import cmds
        from avalon import maya

        dirname = tempfile.mkdtemp()
        filename = "{name}.ma".format(**instance.data)
        path = os.path.join(dirname, filename)

        # Perform extraction
        self.log.info("Performing extraction..")
        with maya.maintained_selection(), maya.without_extension():
            self.log.info("Extracting %s" % str(list(instance)))
            cmds.select(instance, noExpand=True)
            cmds.file(path,
                      force=True,
                      typ="mayaAscii",
                      exportSelected=True,
                      preserveReferences=False
                      )

        # Store reference for integration
        if "files" not in instance.data:
            instance.data["files"] = list()

        instance.data["files"].append(filename)
        instance.data["stagingDir"] = dirname

        self.log.info("Extracted {instance} to {path}".format(**locals()))
