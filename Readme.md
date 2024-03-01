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