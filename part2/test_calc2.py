import unittest


class CalcTestCase(unittest.TestCase):

    def makeInterpreter(self, text):
        from calc2 import Interpreter
        interpreter = Interpreter(text)
        return interpreter

    def test_lexer_integer(self):
        from calc2 import INTEGER
        lexer = self.makeInterpreter('234')
        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 234)

    def test_lexer_plus(self):
        from calc2 import PLUS
        lexer = self.makeInterpreter('+')
        token = lexer.get_next_token()
        self.assertEqual(token.type, PLUS)
        self.assertEqual(token.value, '+')

    def test_lexer_minus(self):
        from calc2 import MINUS
        lexer = self.makeInterpreter('-')
        token = lexer.get_next_token()
        self.assertEqual(token.type, MINUS)
        self.assertEqual(token.value, '-')

    def test_lexer_eof(self):
        from calc2 import EOF
        lexer = self.makeInterpreter('-')
        token = lexer.get_next_token()
        token = lexer.get_next_token()
        self.assertEqual(token.type, EOF)

    def test_lexer_whitespace(self):
        from calc2 import INTEGER
        lexer = self.makeInterpreter('  23')
        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 23)

    def test_lexer_addition(self):
        from calc2 import INTEGER, PLUS, EOF
        lexer = self.makeInterpreter('2+3')

        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 2)

        token = lexer.get_next_token()
        self.assertEqual(token.type, PLUS)
        self.assertEqual(token.value, '+')

        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 3)

        token = lexer.get_next_token()
        self.assertEqual(token.type, EOF)

    def test_lexer_subtraction(self):
        from calc2 import INTEGER, MINUS, EOF
        lexer = self.makeInterpreter(' 27   -  7  ')

        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 27)

        token = lexer.get_next_token()
        self.assertEqual(token.type, MINUS)
        self.assertEqual(token.value, '-')

        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 7)

        token = lexer.get_next_token()
        self.assertEqual(token.type, EOF)

    def test_interpreter_addition(self):
        interpreter = self.makeInterpreter(' 23 + 7')
        result = interpreter.expr()
        self.assertEqual(result, 30)

    def test_interpreter_subtraction(self):
        interpreter = self.makeInterpreter(' 27   -  7  ')
        result = interpreter.expr()
        self.assertEqual(result, 20)

    # Extend the calculator to handle multiplication of two integers
    def test_interpreter_multiplication(self):
        interpreter = self.makeInterpreter('2 * 3')
        result = interpreter.expr()
        self.assertEqual(result, 6)

        interpreter = self.makeInterpreter(' 4 *  5')
        result = interpreter.expr()
        self.assertEqual(result, 20)

    # Extend the calculator to handle division of two integers
    def test_interpreter_division(self):
        interpreter = self.makeInterpreter('4 / 2')
        result = interpreter.expr()
        self.assertEqual(result, 2)

        interpreter = self.makeInterpreter(' 20 /  5')
        result = interpreter.expr()
        self.assertEqual(result, 4)

    # Modify the code to interpret expressions containing an arbitrary number of additions and subtractions
    def test_interpreter_arbitrary(self):
        interpreter = self.makeInterpreter('1 + 2 + 3 + 4  ')
        result = interpreter.expr()
        self.assertEqual(result, 10)

        interpreter = self.makeInterpreter('9 - 5 + 3 + 11')
        result = interpreter.expr()
        self.assertEqual(result, 18)

if __name__ == '__main__':
    unittest.main()
