<div align="center">
  <h1>White Dove Chess Engine</h1>
  <img src="thumbnail.png" alt="White Dove Chess Engine Logo" width="600">
</div>


**White Dove** is a chess engine developed entirely within the [Scratch programming language](https://scratch.mit.edu), leveraging the enhanced capabilities of [TurboWarp](https://turbowarp.org). Recognized as one of the top five chess engines in the Scratch/TurboWarp community.

Rating: ~2300 elo

## Features

- **Alpha-Beta**: Implements MiniMax with Alpha-Beta Pruning to efficiently evaluate potential moves.
- **Quiescence Search**: Enhances move evaluation by extending searches beyond standard depths to avoid overlooking critical moves.
- **Late Move Reductions (LMR)**: Optimizes search efficiency by reducing the depth of less promising moves, allowing deeper exploration of critical lines.
- **NNUE**: An "Efficiently Updatable Neural Network" is included, and can be accessed via the command line interface within the project, it is noticably weaker than the standard HCE (hand-crafted evaluation) due to poor training, but is still quite strong, and serves as a pretty cool technical demo! The net was trained with [the NNUE / ML Bullet Trainer](https://github.com/jw1912/bullet)
  - (768 => 128)x2 => 1

## Getting Started

To experience White Dove:

1. **Access the Project**: You can use the [web version on Turbowarp](https://turbowarp.org/858052938/fullscreen?turbo) or the [Scratch one](https://scratch.mit.edu/projects/858052938/).

OR

1. **Download the .sb3 file**: After downloading the .sb3 file, you can also download the [Turbowarp desktop environment](https://desktop.turbowarp.org/), next you can simply import and use!


## Scratch vs Turbowarp

[Scratch](https://scratch.mit.edu) is a block-based coding environment designed primarily to make teaching coding easy for absolute beginners. However, it is very very slow, due to various traits of the langauge itself.

So, various engine creators on Scratch also use [Turbowarp](https://turbowarp.org/) (which is around 40x faster than Scratch), which is another developement environment, that *still* uses the Scratch programming language. The reason that it is much much faster is because it first compiles the code to Javascript before running it. Even then, it is still incredible inefficient (and slow compared to other languages, such as C++ or Rust), due to needing to have backwards compatibility with default Scratch.

## License

GNU General Public License v3.0

---

*Note: White Dove's development has been influenced by discussions and collaborations within the Scratch community. Special thanks to contributors such as [@ArnoHu](https://scratch.mit.edu/users/ArnoHu/) and [@birdracerthree](https://scratch.mit.edu/users/birdracerthree/) for their insights and support. A lot of code and techniques were also taken from various engines and resources including but not limited to the Chess Programming Wiki, the [Stockfish Chess Engine](https://github.com/official-stockfish/Stockfish) (for a lot of the HCE elements, from SF11),[Smallbrain](https://github.com/Disservin/Smallbrain), [GoK](https://scratch.mit.edu/projects/148769358/), [bullet NNUE trainer](https://github.com/jw1912/bullet), [lc0](https://github.com/LeelaChessZero/lc0), and many more. This project would not have been possible without them!*


