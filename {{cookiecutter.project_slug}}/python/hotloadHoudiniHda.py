"""
This is an interesting script that if called from the hou.session module,
which happens automatically, during file startup it will install HDA files
that live in an hda directory.

This method is not necessary if HOUDINI_PATH includes a path to the workspace directory
and there is an otls directory that contains the HDAs, however for a pretty cool for
portability.

Original author: Chris Gardner
Original source: https://gist.github.com/chris-gardner/c9daf34a668c5dddda94b9f6276d8cb8
Referenced: https://www.tokeru.com/cgwiki/index.php?title=HoudiniHDA

hou.session module content (Windows > Python Source Editor):

    import hou
    import os
    import sys
    
    sys.path.append((hou.getenv("HIP") + "/python").replace("\\", "/"))

    from hotloadHoudiniHda import loadHdaLibrary

    debug = False
    hdaLib = (hou.getenv("HIP") + "/hda").replace("\\", "/")

    if os.path.isdir(hdaLib):
        if debug:
            print("Attempting to hot-load HDA library: {}".format(hdaLib))
            
        installed, failed, skipped = loadHdaLibrary(hdaLib)
        for i in installed:
            if debug:
                print("Installed: {}".format(i))
        for f in failed:
            print("Install failed: {}".format(f))
        for s in skipped:
            if debug:
                print("Ignored: {}".format(s))

"""
import hou
import os


def loadHdaLibrary(libPath):
    """
    Loads all the HDA files in the given path

    1) Get all the .otl files in the directory
    2) Install the file if it hasn't been already

    :param str libPath: HDA library file path
    :rtype: list[installed], list[failed], list[skipped]
    """
    if not os.path.isdir(libPath):
        print("Library path '{}' does not exist".format(libPath))
        return
    
    installed, failed = [], []
    loadedFiles = hou.hda.loadedFiles()
    fileTypes = [".otl", ".hda", ".hdanc"]
    installableFiles = [f for f in os.listdir(libPath) if os.path.splitext(f)[-1] in fileTypes]
    skipped = set(os.listdir(libPath)).difference(set(installableFiles))

    for otlPath in installableFiles:
        fullPath = os.path.join(libPath, otlPath).replace("\\", "/")
        if fullPath not in loadedFiles:
            try:
                hou.hda.installFile(fullPath)
            except:
                failed.append(fullPath)
            else:
                installed.append(fullPath)

    return installed, failed, skipped
