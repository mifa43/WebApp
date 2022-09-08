
class ValueInputException(Exception):

    def __init__(self, param: str, msg: str) -> None:

        self.param = param

        self.msg = msg

        super().__init__(msg)

    def __str__(self) -> str:

        return f"The entered value  is not valid and cannot be processed typeOFF=={type(self.param)}:length({len(self.param)}), msg={self.msg}"


