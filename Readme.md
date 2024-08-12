# super_calc_toml

Small package to try out editable install with pyproject.toml and no setup.py
or setup.cfg.

Keywords: PEP660

## Playground

### Use bash to play with the calculator

This will add the numbers 1 to 2000 together

```bash
echo $(seq 1 2000) | xargs suca add
```

Factorials are also supported

```bash
echo $(seq 1 10) | xargs suca factorial
```


## Click groups

    Usage: suca [OPTIONS] COMMAND [ARGS]...

    Options:
    -h, --help, --h  Show this message and exit.

    Commands:
    sc                            Group for scientific calculations (click...
    si                            Click gropup for simple calculations.
    test-bash-completion-command  Test command for bash completion.



## Simple (si)
    Usage: suca si [OPTIONS] COMMAND [ARGS]...

    Click gropup for simple calculations.

    Options:
    --help  Show this message and exit.

    Commands:
    float (fl)  subcommand - Float operations
    fr (fr)     subcommand - fractions
    int (i)     subcommand - Integer operations


### simple.fractions
    Usage: suca si fr [OPTIONS] COMMAND [ARGS]...

    subcommand - fractions

    Options:
    -h, --help  Show this message and exit.

    Commands:
    add  Add two fractions

### simple.float

    Usage: suca si float [OPTIONS] COMMAND [ARGS]...

    subcommand - Float operations

    Options:
    -h, --help  Show this message and exit.

    Commands:
    add   Add two numbers
    mult  Multiply numbers

## scientific (sc)

    Usage: suca sc [OPTIONS] COMMAND [ARGS]...

    Group for scientific calculations (click help).

    Options:
    -h, --h, --help  Show this message and exit.

    Commands:
    cos   Calculate cosine of x
    log   Calculate natural logarithm of x
    sin   Calculate sine of a number.
    sqrt  Calculate square root of x
    tan   Calculate tangent of x
