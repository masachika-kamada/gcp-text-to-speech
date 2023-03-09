import glob
import os
import sys
import argparse
from pydub import AudioSegment
from natsort import natsorted


def main():
    parser = argparse.ArgumentParser(description="mp3ファイルの長さを秒数で出す")
    parser.add_argument("--src", help="mp3 directory")
    args = parser.parse_args()

    src = args.src
    if not os.path.exists(src):
        print("Error: {} not found.".format(src))
        sys.exit(1)

    if os.path.isfile(src):
        print("Error: {} is not directory.".format(src))
        sys.exit(1)

    mp3_files = glob.glob(os.path.join(src, "*.mp3"))
    for mp3_file in natsorted(mp3_files):
        mp3 = AudioSegment.from_mp3(mp3_file)
        print(f"{mp3_file}: {len(mp3)/1000:.2f} sec")


if __name__ == "__main__":
    main()
