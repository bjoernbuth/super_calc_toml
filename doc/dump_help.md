# 1  suca 

```
Options:
  -h, --help, --h  Show this message and exit.

Commands:
  bashcomp  Test command for bash completion.
  calc      Click gropup for simple calculations.
  dh        Dump the help to ../docs/dump_help.md.
```

## 1.1  suca.bashcomp - command

```
Test command for bash completion.

Options:
  -h, --h, --help                 Show this message and exit.
  --long_argument_name_01 INTEGER
                                  First number
  --long_argument_name_02 INTEGER
                                  Second number
```

## 1.2  suca.calc - group

```
Click gropup for simple calculations.

Options:
  --help  Show this message and exit.

Commands:
  cos      Calculate cosine of x
  fr (fr)  subcommand - fractions
  int (i)  subcommand - Integer operations
  log      Calculate natural logarithm of x
  sin      Calculate sine of a number.
  sqrt     Calculate square root of x
  tan      Calculate tangent of x
```

### 1.2.1  suca.calc.fr - group

```
subcommand - fractions

Options:
  -h, --help  Show this message and exit.

Commands:
  add  Add two fractions
```

#### 1.2.1.1  suca.calc.fr.add - command

```
Add two fractions

Options:
  --help  Show this message and exit.
```

### 1.2.2  suca.calc.int - group

```
subcommand - Integer operations

Options:
  -h, --help  Show this message and exit.

Commands:
  add (a)   Add 2 integers, (group int but also main group).
  div (d)   Divide two numbers
  exp (e)   Exponentiation
  mod       Modulo operation
  mult (m)  Multiply integers, arbitrary number of args.
  sub (s)   Subtract 2 integers (group int but also main group)
```

#### 1.2.2.1  suca.calc.int.add - command

```
Add 2 integers, (group int but also  main group).

Options:
  --help  Show this message and exit.
```

#### 1.2.2.2  suca.calc.int.sub - command

```
Subtract 2 integers (group int but also  main group)

Options:
  --help  Show this message and exit.
```

#### 1.2.2.3  suca.calc.int.mult - command

```
Multiply integers, arbitrary number of args.

Options:
  --help  Show this message and exit.
```

#### 1.2.2.4  suca.calc.int.div - command

```
Divide two numbers

Options:
  --help  Show this message and exit.
```

#### 1.2.2.5  suca.calc.int.exp - command

```
Exponentiation

Options:
  --help  Show this message and exit.
```

#### 1.2.2.6  suca.calc.int.mod - command

```
Modulo operation

Options:
  --help  Show this message and exit.
```

### 1.2.3  suca.calc.sin - command

```
Calculate sine of a number.

Options:
  -r, --rad  Calculate sin in radians (default mode)
  -d, --deg  Calculate sin in degrees
  --help     Show this message and exit.
```

### 1.2.4  suca.calc.cos - command

```
Calculate cosine of x

Options:
  --help  Show this message and exit.
```

### 1.2.5  suca.calc.tan - command

```
Calculate tangent of x

Options:
  --help  Show this message and exit.
```

### 1.2.6  suca.calc.log - command

```
Calculate natural logarithm of x

Options:
  --help  Show this message and exit.
```

### 1.2.7  suca.calc.sqrt - command

```
Calculate square root of x

Options:
  --help  Show this message and exit.
```

## 1.3  suca.dumphelp-to-file - command

```
Dump the help to ../docs/dump_help.md.

Options:
  -c, --copy_to_clipboard / --noc
                                  Copy the result of the command to the
                                  clipboard.  [default: copy_to_clipboard]
  --help, --h                     Show this message and exit.
  --print_result, --p / --nop, --q
                                  Print the result to the console.  [default:
                                  print_result]
  --number_sections, --ns / --no_number_sections, --nons
                                  Print result to console.  [default:
                                  no_number_sections]
```
