# dogs-vs-catsのデータセットをロードし、リサイズして、新しいnpy形式で保存
from os import listdir
from numpy import asarray
from numpy import save
from numpy import savetxt
import cv2
import os
import argparse
print(os.getcwd())
# from tensorflow.keras.utils import load_img
# from tensorflow.keras.utils import img_to_array

parser = argparse.ArgumentParser()
# データセットの格納場所を設定
parser.add_argument(
    "--data-folder",
    type=str,
    dest="data_folder",
    default="data",
    help="data folder mounting point",
)
args = parser.parse_args()
data_folder = args.data_folder
print("======================================================")
print(data_folder)
