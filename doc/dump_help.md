#  suca 

```
Options:
  -h, --help, --h  Show this message and exit.

Commands:
  bashcomp  Test command for bash completion.
  dh        Dump the help to ../docs/dump_help.md.
  si        Click gropup for simple calculations.
```

##  suca.bashcomp - command

```
Test command for bash completion.

Options:
  -h, --h, --help                 Show this message and exit.
  --long_argument_name_01 INTEGER
                                  First number
  --long_argument_name_02 INTEGER
                                  Second number
```

##  suca.si - group

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

###  suca.si.fr - group

```
subcommand - fractions

Options:
  -h, --help  Show this message and exit.

Commands:
  add  Add two fractions
```

####  suca.si.fr.add - command

```
Add two fractions

Options:
  --help  Show this message and exit.
```

###  suca.si.int - group

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

####  suca.si.int.add - command

```
Add 2 integers, (group int but also  main group).

Options:
  --help  Show this message and exit.
```

####  suca.si.int.sub - command

```
Subtract 2 integers (group int but also  main group)

Options:
  --help  Show this message and exit.
```

####  suca.si.int.mult - command

```
Multiply integers, arbitrary number of args.

Options:
  --help  Show this message and exit.
```

####  suca.si.int.div - command

```
Divide two numbers

Options:
  --help  Show this message and exit.
```

####  suca.si.int.exp - command

```
Exponentiation

Options:
  --help  Show this message and exit.
```

####  suca.si.int.mod - command

```
Modulo operation

Options:
  --help  Show this message and exit.
```

###  suca.si.sin - command

```
Calculate sine of a number.

Options:
  -r, --rad  Calculate sin in radians (default mode)
  -d, --deg  Calculate sin in degrees
  --help     Show this message and exit.
```

###  suca.si.cos - command

```
Calculate cosine of x

Options:
  --help  Show this message and exit.
```

###  suca.si.tan - command

```
Calculate tangent of x

Options:
  --help  Show this message and exit.
```

###  suca.si.log - command

```
Calculate natural logarithm of x

Options:
  --help  Show this message and exit.
```

###  suca.si.sqrt - command

```
Calculate square root of x

Options:
  --help  Show this message and exit.
```

##  suca.dumphelp-to-file - command

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
