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
```

スクリプトは指定されたディレクトリとそのサブディレクトリ内のすべてのファイルを処理します。進行状況がコンソールに表示され、最終結果はカレントディレクトリの`output.txt`に保存されます。

## 注意点
- 大量のファイルを処理する場合、かなりの時間がかかる可能性があります。
- このスクリプトはMD5ハッシュを使用しています。高速ですが、まれに衝突が発生する可能性があります。重要なアプリケーションでは、より強力なハッシュ関数の使用を検討してください。
- スキャンしたいすべてのファイルとディレクトリに対する読み取り権限があることを確認してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
