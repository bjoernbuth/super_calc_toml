# super_calc_toml

Small package to try out editable install with pyproject.toml and no setup.py
or setup.cfg. Also meant for experiments using the click library:
[click](https://click.palletsprojects.com/en/8.1.x/)

In order to have short names for some groups and command click-aliases is used:
[click-aliases](https://github.com/click-contrib/click-aliases)

For example:


    suca calc int add 1 2 3   , has a short form
    suca c i a 1 2 3




Keywords: PEP660

## Playground

### Use bash to play with the calculator

This will add the numbers 1 to 2000 together

```bash
echo $(seq 1 2000) | xargs suca calc int  add
```

To compute 10!

```bash
echo $(seq 1 10) | xargs suca calc int mult
Product: 3628800
```


## Click groups

    Usage: suca [OPTIONS] COMMAND [ARGS]...

    Options:
    -h, --help, --h  Show this message and exit.

    Commands:
    bashcomp  Test command for bash completion.
    calc (c)  Click gropup for simple calculations.
    dh        Dump the help to ../docs/dump_help.md.


## calc (c) group
    Usage: suca calc [OPTIONS] COMMAND [ARGS]...

    Click gropup for simple calculations.

    Options:
    --help  Show this message and exit.

    Commands:
    dh       Dump the help to ../docs/dump_help.md.
    fr (fr)  subcommand - fractions
    int (i)  subcommand - Integer operations
    sci (s)  Group for scientific calculations (click help).


For a more detailed help, use the `--help` option with the command
or see the file [./doc/dump_help.md](./doc/dump_help.md)
