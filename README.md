# TextRecognitionDataGeneratorVietnamese

A synthetic data generator for text recognition


### Setup

- To create enviroment: 
```bash
pip install -r requirements.txt
```

### Data Generation

```bash
cd trdg/
```

- To generate text files from dict files:

```
python3 gen_corpus.py
```

```
python3 run.py \
--count 50000 \
--language vi \
--format 26 \
--name_format 2 \
--current_idx 0 \
--output_dir ./out/dataset/ \
--font_dir ./fonts/vi \
--input_file ./texts/corpus.txt \
--background 3 \
--image_dir ./images/ \
--margins "0,0,0,0" \
--blur 1 \
--random_blur \
--skew_angle 1 \
--random_skew \
--case upper \
```

or 
```bash 
bash run.sh
```

- Flag:
    - `--count`: The number of images to be created
    - `--language`: The language to use (must have in `fonts` and `dicts`)
    - `--format`: Define the height of the produced images if horizontal, else the width
    - `--name_format`: Select name format - 0: [TEXT]_[ID].[EXT], 1: [ID]_[TEXT].[EXT] 2: [ID].[EXT] + one file labels.txt containing id-to-label mappings
    - `--current_idx`: Define the begin index of `--name_format` for saving `ID`.
    - `--output_dir`: Output directory
    - `--font_dir`: Select the fonts coresponding to the `--language`
    - `--input_file`: Select text file as source for the text
    - `--background`: Select background - 0: Gaussian Noise, 1: Plain white, 2: Quasicrystal, 3: Image
    - `--image_dir`: Define an image directory to use when `--background` is set to 3
    - `--margin`: Define the margins around the text when rendered. In pixels
    - `--blur`: Apply gaussian blur to the resulting sample. Should be an integer defining the blur radius
    - `--random_blur`: the blur radius will be randomized between 0 and `--blur`
    - `--skew_angle`: Define skewing angle of the generated text. In positive degrees
    - `--random_skew`: the skew angle will be randomized between the value set with `--skew_angle` and it's opposite
    - `--case`: Select (`upper`, `lower`, `capwords`)

- Read more arguments on `trdg/run.py`


### 


### Contributions

- Add vietnamese fonts, dicts and corpus.
- Add new function `trdg/gen_corpus.py` to generate text files from dict files.
- Update features `--case` with `capwords`.
- Update save each text labels corresponding to each images if `--name_format` is set to 2.
