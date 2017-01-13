class PyElectroError(Exception):
    def __init__(self, message=None):
        super(PyElectroError, self).__init__(message)

        self.message = message


class InvalidAngleError(PyElectroError):
        """
        Invalid Angle Provided for an action
        """
        pass


class InvalidShapeError(PyElectroError):
        """
        Invalid Shape Provided
        """
        pass

