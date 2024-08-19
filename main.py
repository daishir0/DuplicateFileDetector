import os
import hashlib
from collections import defaultdict
import concurrent.futures
import time
import sys

def get_file_hash(filepath):
    """ファイルのMD5ハッシュを計算する"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def find_duplicates(directory):
    """指定されたディレクトリ内の重複ファイルを見つける"""
    file_size_dict = defaultdict(list)
    total_files = 0
    processed_files = 0
    start_time = time.time()

    print("ファイルの列挙を開始します...")
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                file_size = os.path.getsize(filepath)
                file_size_dict[file_size].append(filepath)
                total_files += 1
            except Exception as e:
                print(f"エラー: {filepath} の処理中に問題が発生しました - {str(e)}")

    print(f"合計 {total_files} 個のファイルを見つけました。重複チェックを開始します...")

    duplicates = defaultdict(list)
    potential_duplicates = {size: files for size, files in file_size_dict.items() if len(files) > 1}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {}
        for size, files in potential_duplicates.items():
            for file in files:
                future = executor.submit(get_file_hash, file)
                future_to_file[future] = (file, size)

        for future in concurrent.futures.as_completed(future_to_file):
            file, size = future_to_file[future]
            try:
                file_hash = future.result()
                duplicates[file_hash].append(file)
            except Exception as exc:
                print(f'{file} でエラーが発生しました: {exc}')
            
            processed_files += 1
            if processed_files % 100 == 0 or processed_files == total_files:
                elapsed_time = time.time() - start_time
                print(f"進行状況: {processed_files}/{total_files} ファイル処理済み ({processed_files/total_files*100:.2f}%) - 経過時間: {elapsed_time:.2f}秒")

    return {k: v for k, v in duplicates.items() if len(v) > 1}

def main(directory):
    start_time = time.time()
    duplicates = find_duplicates(directory)

    with open('output.txt', 'w', encoding='utf-8') as f:
        if duplicates:
            f.write("重複ファイルが見つかりました:\n")
            for hash_value, file_list in duplicates.items():
                f.write(f"\nハッシュ値: {hash_value}\n")
                for file in file_list:
                    f.write(f"  {file}\n")
            f.write(f"\n合計 {len(duplicates)} 組の重複ファイルが見つかりました。\n")
        else:
            f.write("重複ファイルは見つかりませんでした。\n")

        end_time = time.time()
        f.write(f"\n処理完了までの時間: {end_time - start_time:.2f}秒\n")

    print(f"処理が完了しました。結果は output.txt に保存されています。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python main.py <対象のディレクトリ名>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"エラー: {directory} は有効なディレクトリではありません。")
        sys.exit(1)
    
    main(directory)
