from lark import Lark
from lark import Transformer

class _Internal:
    class TransformToFormat(Transformer):
        def value(self, s):
            values = ""
            for i in s:
                values += i
            return values

        def key(self, s):
            return (s[0], s[1])

    def __init__(self):
        self.grammar = '''start: key*

            COMMENT: />.*/
            
            SYMBOL: "|" | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | ">" | "=" | "<" | "?" | "@" | "[" | "\\"" | "]" | "^" | "_" | "`" | "{" | "}" | "~"
            
            ?string: (WORD | SYMBOL)
            value: ESCAPED_STRING*  | NUMBER+
            key: WORD "=" value
            
            %import common.WORD
            %import common.ESCAPED_STRING
            %import common.NUMBER
            %import common.DIGIT
            %import common.WS
            %ignore COMMENT
            %ignore WS
            '''
        self.parser = Lark(self.grammar, parser='lalr', transformer=self.TransformToFormat())

def load(fileobj):
    result = {}
    lang = _Internal()
    for line in fileobj:
        tree = lang.parser.parse(line)
        for node in tree.children:
            name = node[0]
            value = node[1].rstrip()

            result[str(name)] = value
    return result

def loads(string: str):
    result = {}
    lang = _Internal()
    for line in string.split("\n"):
        tree = lang.parser.parse(line)
        for node in tree.children:
            name = node[0]
            value = node[1].rstrip()

            result[str(name)] = value
    return result

def dump(object: dict, fileobj):
    result = ""
    final = ""
    for x in object:
        result += x + "="
        value = object.get(x)
        if isinstance(value, str):
            value = '"' + value + '"'
        result += str(value)
        final += result + "\n"
        result = ""
    fileobj.write(final)