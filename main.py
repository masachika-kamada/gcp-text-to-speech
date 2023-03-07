import argparse
import os
import yaml
from tqdm import tqdm
from tts_class import TTS


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=str, help="source file")
    parser.add_argument("--config", type=str, default="config.yaml", help="config file")
    args = parser.parse_args()
    config = yaml.load(open(args.config, "r"), Loader=yaml.SafeLoader)
    print(config)
    tts = TTS(**config)

    with open(args.src, "r", encoding="utf-8") as f:
        text = f.read()

    # separate text into sentences
    if config["lang"] == "ja-JP":
        sentences = text.split("。")
    else:
        sentences = text.split(".")[:-1]
    sentences = [s + "." for s in sentences]

    basename_without_ext = os.path.splitext(os.path.basename(args.src))[0]
    os.makedirs(f"dst/{basename_without_ext}", exist_ok=True)
    for i, s in tqdm(enumerate(sentences)):
        # 最後の文だけ無音を追加する
        silent = True if i == len(sentences) - 1 else False
        tts.run(s, f"dst/{basename_without_ext}/{i + 1}.mp3", silent=silent)
