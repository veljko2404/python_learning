# 3. Napisati program koji formira direktorijum tmp_dat i sve .dat fajlove iz radnog direktorijuma prebacuje u tmp_dat direktorijum.

import os
import shutil


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def move_files(source, dest):
    for filename in os.listdir(source):
        if filename.endswith(".dat"):
            source_path = os.path.join(source, filename)
            dest_path = os.path.join(dest, filename)
            shutil.move(source_path, dest_path)
            print(f"Moved {source_path} to {dest_path}")


src = os.getcwd()
dst = os.path.join(src, "tmp_dat")
create_dir(dst)
move_files(src, dst)
