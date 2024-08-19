# DuplicateFileDetector

## Overview
DuplicateFileDetector is a Python script that efficiently finds and lists duplicate files within a specified directory and its subdirectories. It uses file size as an initial filter and then calculates MD5 hashes for potential duplicates, providing a fast and accurate method for identifying identical files.

## Installation
To install DuplicateFileDetector, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/daishir0/DuplicateFileDetector.git
   ```
2. Change to the project directory:
   ```
   cd DuplicateFileDetector
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script from the command line, specifying the target directory:

```
python main.py <target_directory>
```

For example:
```
python main.py D:\MyDocuments

:

進行状況: 46400/114558 ファイル処理済み (40.50%) - 経過時間: 908.67秒
進行状況: 46500/114558 ファイル処理済み (40.59%) - 経過時間: 909.37秒
進行状況: 46600/114558 ファイル処理済み (40.68%) - 経過時間: 910.06秒
進行状況: 46700/114558 ファイル処理済み (40.77%) - 経過時間: 910.81秒
進行状況: 46800/114558 ファイル処理済み (40.85%) - 経過時間: 911.77秒
進行状況: 46900/114558 ファイル処理済み (40.94%) - 経過時間: 912.71秒
進行状況: 47000/114558 ファイル処理済み (41.03%) - 経過時間: 913.56秒
進行状況: 47100/114558 ファイル処理済み (41.11%) - 経過時間: 914.26秒
進行状況: 47200/114558 ファイル処理済み (41.20%) - 経過時間: 915.29秒
進行状況: 47300/114558 ファイル処理済み (41.29%) - 経過時間: 916.04秒
進行状況: 47400/114558 ファイル処理済み (41.38%) - 経過時間: 916.98秒
進行状況: 47500/114558 ファイル処理済み (41.46%) - 経過時間: 920.73秒
進行状況: 47600/114558 ファイル処理済み (41.55%) - 経過時間: 1548.94秒
処理が完了しました。結果は output.txt に保存されています。
```

output.txt

```
重複ファイルが見つかりました:

ハッシュ値: 04d72a7064951575b322d2ebfac231e3
  D:\MyDocuments\2017-09-10 07.51.05.jpg
  D:\MyDocuments\hoge\hoge.jpg

ハッシュ値: dd46d8d428a05c193940a1ec71576407
  D:\MyDocuments\2018-09-10 07.51.05.jpg
  D:\MyDocuments\hoge2\hoge2.jpg

合計 2 組の重複ファイルが見つかりました。

処理完了までの時間: 0.79秒
```

The script will process all files in the specified directory and its subdirectories. Progress will be displayed in the console, and the final results will be saved in `output.txt` in the current directory.

## Notes
- Processing a large number of files may take considerable time.
- The script uses MD5 hashing, which is fast but may have rare collisions. For critical applications, consider using a stronger hash function.
- Ensure you have read permissions for all files and directories you want to scan.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# DuplicateFileDetector

## 概要
DuplicateFileDetectorは、指定されたディレクトリとそのサブディレクトリ内の重複ファイルを効率的に検索してリストアップするPythonスクリプトです。ファイルサイズを初期フィルターとして使用し、その後潜在的な重複に対してMD5ハッシュを計算することで、同一ファイルを高速かつ正確に識別します。

## インストール方法
DuplicateFileDetectorをインストールするには、以下の手順に従ってください：

1. リポジトリをクローンします：
   ```
   git clone https://github.com/daishir0/DuplicateFileDetector.git
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd DuplicateFileDetector
   ```
3. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

## 使い方
コマンドラインから、対象ディレクトリを指定してスクリプトを実行します：

```
python main.py <対象ディレクトリ>
```

例：
```
python main.py D:\MyDocuments

:

進行状況: 46400/114558 ファイル処理済み (40.50%) - 経過時間: 908.67秒
進行状況: 46500/114558 ファイル処理済み (40.59%) - 経過時間: 909.37秒
進行状況: 46600/114558 ファイル処理済み (40.68%) - 経過時間: 910.06秒
進行状況: 46700/114558 ファイル処理済み (40.77%) - 経過時間: 910.81秒
進行状況: 46800/114558 ファイル処理済み (40.85%) - 経過時間: 911.77秒
進行状況: 46900/114558 ファイル処理済み (40.94%) - 経過時間: 912.71秒
進行状況: 47000/114558 ファイル処理済み (41.03%) - 経過時間: 913.56秒
進行状況: 47100/114558 ファイル処理済み (41.11%) - 経過時間: 914.26秒
進行状況: 47200/114558 ファイル処理済み (41.20%) - 経過時間: 915.29秒
進行状況: 47300/114558 ファイル処理済み (41.29%) - 経過時間: 916.04秒
進行状況: 47400/114558 ファイル処理済み (41.38%) - 経過時間: 916.98秒
進行状況: 47500/114558 ファイル処理済み (41.46%) - 経過時間: 920.73秒
進行状況: 47600/114558 ファイル処理済み (41.55%) - 経過時間: 1548.94秒
処理が完了しました。結果は output.txt に保存されています。
```

output.txt

```
重複ファイルが見つかりました:

ハッシュ値: 04d72a7064951575b322d2ebfac231e3
  D:\MyDocuments\2017-09-10 07.51.05.jpg
  D:\MyDocuments\hoge\hoge.jpg

ハッシュ値: dd46d8d428a05c193940a1ec71576407
  D:\MyDocuments\2018-09-10 07.51.05.jpg
  D:\MyDocuments\hoge2\hoge2.jpg

合計 2 組の重複ファイルが見つかりました。

処理完了までの時間: 0.79秒
```

スクリプトは指定されたディレクトリとそのサブディレクトリ内のすべてのファイルを処理します。進行状況がコンソールに表示され、最終結果はカレントディレクトリの`output.txt`に保存されます。

## 注意点
- 大量のファイルを処理する場合、かなりの時間がかかる可能性があります。
- このスクリプトはMD5ハッシュを使用しています。高速ですが、まれに衝突が発生する可能性があります。重要なアプリケーションでは、より強力なハッシュ関数の使用を検討してください。
- スキャンしたいすべてのファイルとディレクトリに対する読み取り権限があることを確認してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
