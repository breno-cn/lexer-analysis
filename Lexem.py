class Lexem:

    def __init__(self, value: str, line: int, col: int) -> None:
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self) -> str:
        return f'(value={self.value}, line={self.line}, col={self.col})'
