import avalon.maya


class ExampleLoader(avalon.maya.Loader):
    """Load Example"""

    families = ["config.example"]
    representations = ["ma"]

    def load(self, context, name=None, namespace=None, data=None):
        import maya.cmds as cmds

        from avalon import maya
        from avalon.maya import lib
        from avalon.maya.pipeline import containerise

        asset = context['asset']
        namespace = namespace or lib.unique_namespace(
            asset["name"] + "_",
            prefix="_" if asset["name"][0].isdigit() else "",
            suffix="_",
        )
        with maya.maintained_selection():
            nodes = cmds.file(self.fname,
                              i=True,
                              namespace=namespace,
                              returnNewNodes=True,
                              groupReference=True,
                              groupName="{}:{}".format(namespace, name))
        # Only containerize if any nodes were loaded by the Loader
        if not nodes:
            return
        self[:] = nodes
        return containerise(
            name=name,
            namespace=namespace,
            nodes=nodes,
            context=context,
            loader=self.__class__.__name__)

    def update(self, container, representation):
        pass

    def remove(self, container):
        from maya import cmds

        namespace = container["namespace"]
        self.log.info("Removing '%s' from Maya.." % container["name"])
        cmds.namespace(removeNamespace=namespace, deleteNamespaceContent=True)
