class Request:
    @classmethod
    def handle_errors(cls, fun, **kwargs):
        try:
            return fun(**kwargs)
        except BaseException as exc:
            return exc.format_exc()
        except Exception as exc:
            return cls.format_exc("Internal server error: {}".format(exc), 500) 

    @staticmethod
    def format_exc(msg: str, status_code: int) -> object:
        return {"error": [{"status": str(status_code), "message": msg}]}, status_code

class GetRequest(Request):
    @classmethod
    def get(cls, **kwargs):
        return cls.handle_errors(cls.handle_get, **kwargs)

    @classmethod
    def handle_get(cls, **kwargs):
        raise NotImplementedError

class BaseException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__()

    def format_exc(self):
        return Request.format_exc(self.message, self.status_code)