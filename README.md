# GCP Text to Speech

## Preparation

* GCP のアカウントを作成する
* GCP のプロジェクトに Text to Speech API を有効化する
* credentials.json を作成する
* TTS のサンプルページから好みの設定を見つけ、config.yaml に記述する

## Usage

### 音声合成

```ps1
python main.py --src {text_file}
```

### 音声の時間計測

```ps1
python measure_time.py --src {dir_path}
```
