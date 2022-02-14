from Lexem import Lexem

class Lexer:

    BUFFER_SIZE = 1024

    def __init__(self, filepath: str) -> None:
        self.input = open(filepath, 'r')
        self.line = 1
        self.col = 1
        self.bufferIndex = 0
        self.buffer = self.input.read(Lexer.BUFFER_SIZE)
    
    def readNextChar(self):
        if self.bufferIndex == Lexer.BUFFER_SIZE:
            self.buffer = ''
            self.buffer = self.input.read(Lexer.BUFFER_SIZE)
            self.bufferIndex = 0

        currentChar = self.buffer[self.bufferIndex]
        self.bufferIndex += 1

        if currentChar == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        
        return currentChar

    def getNextLexem(self):
        currentLexem = ''

        while self.isWhitespace():
            self.readNextChar()

        line = self.line
        col = self.col

        while self.bufferIndex < len(self.buffer) and not self.isWhitespace():
            currentLexem += self.readNextChar()

        print(currentLexem)
        return Lexem(currentLexem, line, col)

    def isWhitespace(self):
        return self.buffer[self.bufferIndex] in [' ', '\t', '\n']
