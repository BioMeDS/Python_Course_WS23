# Tetris

Goal for the week is an algorithm, that plays Tetris at a level to consistently reach scores above 0.

We use the [PyBoy](https://github.com/Baekalfen/PyBoy) emulator.

The code in this repo uses an old version of `PyBoy`. In order to run it, you can re-create the environment.

```bash
mamba env create -f pyboy.yaml
mamba activate pyboy
# Run interactively
pyboy Tetris.gb
# Run the final algorithm
python 10-putting-it-together.py
```

### Related Literature
1. [*Building Controllers for Tetris*, by Thiery and Scherrer](https://hal.science/inria-00418954)
2. [*Tetris*, by Fahey](https://web.archive.org/web/20110708174753/https://www.colinfahey.com/tetris/tetris_en.html)
3. [*The Game of Tetris in Machine Learning*, by Algorta and Şimşek](https://arxiv.org/abs/1905.01652)
