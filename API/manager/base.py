class Request:
    @classmethod
    def handle_errors(cls, fun, **kwargs):
        try:
            return fun(**kwargs)
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