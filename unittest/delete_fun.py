import os
import os.path

def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)

class RemovalService(object):
    """
    A Service for removing objects from the filesystem."""

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService(object):

    def __init__(self, removal_service):

        self.removal_service = removal_service


    def upload_complete(self, filename):

        self.removal_service.rm(filename)