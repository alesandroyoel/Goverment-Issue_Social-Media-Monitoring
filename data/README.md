# Data

The raw dataset and the sentiment lexicons are **not included** in this repository.

| File | What it is | Where it comes from |
|---|---|---|
| `Data Test_Assigment Tahap 1.xlsx` (sheet `Posts`) | 15,134 social media posts (Instagram, Facebook, TikTok), 28 columns | Provided as part of a data analyst internship selection case study. Not redistributable. |
| `kamus_positive.xlsx`, `kamus_negative.xlsx` | Weighted positive / negative word lists (columns `word`, `weight`) | InSet lexicon (see citation in the main README) |
| `kamuskatabaku.xlsx` | Slang -> formal word normalization (columns `slang`, `formal`) | Indonesian normalization dictionary |
| `stopwordbahasa.txt` | Indonesian stopword list, one word per line | Public Indonesian stopword list |

## Running the notebook

The notebook was written for **Google Colab**. It reads the dataset temporary from
`/content/Data Test_Assigment Tahap 1.xlsx` and the other four files from the working directory (`/content/`).

- **Colab:** upload all five files to the runtime, keeping the file names above, then run all cells.
- **Local Jupyter:** put the five files in one folder, start Jupyter from that folder, and change `FILE_NAME` in the setup cell to the local path of the dataset.
