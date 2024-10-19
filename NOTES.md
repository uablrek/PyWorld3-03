# My World3-03 model fork

This model is taken from [pyworld3](https://github.com/cvanwynsberghe/pyworld3)
and upgraded to `-03` (for some reason it's not a fork). The model was used
to recalibrate parameters to ["match empirical data on world development"](
https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.13442). I want to
learn more, see with my own eyes, and tweak parameters myself.


### Prepare and run on Ubuntu 24.04

The results are overlaid on top of the original graphs for validation
(same as in [pyworld3](https://github.com/cvanwynsberghe/pyworld3))
```
apt install -y python3-pip python3-full python3-numpy python3-scipy \
  python3-matplotlib
# (edit run_different_standard_configurations.py to select scenario)
python3 run_different_standard_configurations.py
#git status -u --ignored (to see what's generated)
```


