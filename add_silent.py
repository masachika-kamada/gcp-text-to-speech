# mp3ファイルを読み込んで末尾に無音を追加する
import argparse
import numpy as np
import librosa
import soundfile as sf


def add_silent(src, dst, silent_duration=0.5):
    y, sr = librosa.load(src, sr=None)
    silent = np.zeros(int(sr * silent_duration))
    y = np.concatenate([silent, y, silent])
    sf.write(dst, y, sr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=str, help="source file")
    parser.add_argument("--dst", type=str, help="destination file")
    parser.add_argument("--silent_duration", type=float, default=0.5, help="silent duration")
    args = parser.parse_args()
    add_silent(args.src, args.dst, args.silent_duration)
