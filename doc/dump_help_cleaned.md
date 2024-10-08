#  suca

```
Commands:
  bashcomp  Test command for bash completion.
  calc (c)  Click gropup for simple calculations.
  dh        Dump the help to ../docs/dump_help.md.
```

##  suca.bashcomp - command

```
Test command for bash completion.

Options:
  --long_argument_name_01 INTEGER
                                  First number
  --long_argument_name_02 INTEGER
                                  Second number
```

##  suca.calc - group

```
Click gropup for simple calculations.

Commands:
  dh       Dump the help to ../docs/dump_help.md.
  fr (fr)  subcommand - fractions
  int (i)  subcommand - Integer operations
  sci (s)  Group for scientific calculations (click help).
```

###  suca.calc.fr - group

```
subcommand - fractions

Commands:
  add  Add two fractions
```

####  suca.calc.fr.add - command

```
Add two fractions

```

###  suca.calc.int - group

```
subcommand - Integer operations

Commands:
  add (a)   Add 2 integers, (group int but also main group).
  div (d)   Divide two numbers
  exp (e)   Exponentiation
  mod       Modulo operation
  mult (m)  Multiply integers, arbitrary number of args.
  sub (s)   Subtract 2 integers (group int but also main group)
```

####  suca.calc.int.add - command

```
Add 2 integers, (group int but also  main group).
```

####  suca.calc.int.sub - command

```
Subtract 2 integers (group int but also  main group)
```

####  suca.calc.int.mult - command

```
Multiply integers, arbitrary number of args.
```

####  suca.calc.int.div - command

```
Divide two numbers
```

####  suca.calc.int.exp - command

```
Exponentiation
```

####  suca.calc.int.mod - command

```
Modulo operation
```

###  suca.calc.sci - group

```
Group for scientific calculations (click help).

Commands:
  cos   Calculate cosine of x
  log   Calculate natural logarithm of x
  sin   Calculate sine of a number.
  sqrt  Calculate square root of x
  tan   Calculate tangent of x
```

####  suca.calc.sci.sin - command

```
Calculate sine of a number.

Options:
  -r, --rad  Calculate sin in radians (default mode)
  -d, --deg  Calculate sin in degrees
```

####  suca.calc.sci.cos - command

```
Calculate cosine of x
```

####  suca.calc.sci.tan - command

```
Calculate tangent of x
```

####  suca.calc.sci.log - command

```
Calculate natural logarithm of x
```

####  suca.calc.sci.sqrt - command

```
Calculate square root of x
```

###  suca.calc.dumphelp-to-file - command

```
Dump the help to ../docs/dump_help.md.

Options:
  --print_result, --p / --nop, --q
                                  Print the result to the console.  [default:
                                  print_result]
  --number_sections, --ns / --no_number_sections, --nons
                                  Print result to console.  [default:
                                  no_number_sections]
```

##  suca.dumphelp-to-file - command

```
Dump the help to ../docs/dump_help.md.

Options:
  --help, --h                     Show this message and exit.
  --print_result, --p / --nop, --q
                                  Print the result to the console.  [default:
                                  print_result]
  --number_sections, --ns / --no_number_sections, --nons
                                  Print result to console.  [default:
                                  no_number_sections]
```
