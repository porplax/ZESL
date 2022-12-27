<p align="center">
  <img src="https://user-images.githubusercontent.com/66521670/209605632-24e913e6-aa9b-4515-8b27-906b60b7695f.svg" />
</p>

# ***Zayne's Extremely Simple Language***
Inspired by **Tom's Obvious Minimal Language (TOML)** and **YAML**

This project isn't serious btw; This was just a side project 👀.
**ZESL** won't be getting regularly scheduled updates.

## **Grammar**
**ZESL** uses the **BNF** grammar format. It's grammar is as follows:
```bnf
<program> ::= <statement>

<statement> ::= <key>
| <comment>

<letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p"
       | "q" | "r" | "s" | "t" | "u" | "v" | "w"
       | "x" | "y" | "z" 

<digit> ::= "0" | "1" | "2" | "3" | "4" | "5"
	   | "6" | "7" | "8" | "9"

<symbol> ::=  "|" | " " | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | ">" | "=" | "<" | "?" | "@" | "[" | "\\" | "]" | "^" | "_" | "`" | "{" | "}" | "~"

<comment> ::= ">" " "* (<digit> | <letter> | " " | <symbol>)+
<value> ::= "\"" (<digit> | <letter> | " " | <symbol>)* "\"" | <digit>+ | "."* <digit>+ "."* <digit>*
<key> ::= <letter>+ "=" <value> " "* <comment>*
```

## **Syntax**
**ZESL** supports strings, integers, and floats. **ZESL** also support usage of comments.
```
> This is a comment.
city="Salt Lake City, Utah"
area=801
precipitation=50.0
```
There are multiple ways to type a value, however there're some *big* **no-no(s)**.

----

#### The correct way to enclose an string in **ZESL** would be in *double quotes*. Attempting to use single quotes will result in an error.
```
quote='Do not fear mistakes. There are none. (Miles Davis)' > Wrong way to write strings.
quote="Do not fear mistakes. There are none. (Miles Davis)" > Correct way to write strings. Note the double quotes.
```

# Goals

If I do decide to at least dedicate **SOME** of my time to this project, here's what I would do.
- Improve BNF grammar. Adding double-quotes and/or back-ticks for string would be nice. Make context a bit more loose.
- Add `[]` and `{}`, allows for defining dicts and/or lists.
- Syntax sugar!?
