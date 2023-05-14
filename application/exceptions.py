class BaseFlaskException(Exception):
    status = 500

    def __init__(self, message=None, status=None, payload=None):
        super().__init__(message)
        self.message = message
        if status is not None:
            self.status = status
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


class NotFound(BaseFlaskException):
    status = 404
