#! /usr/bin/env python3

import argparse
import subprocess
import os

parser = argparse.ArgumentParser()

parser.add_argument("themesDir", help="Path to the directory containing Base16 themes.")
parser.add_argument("previewScript", help="Path to the script that converts a theme to SVG.")

args = parser.parse_args()

def genREADME(themesDir, previewScript):
    with open("README.md", "w") as readme:
        readme.write("# Base16 colorschemes collection\n\n")

        for themeFile in os.listdir(themesDir):
            themeName = os.path.splitext(themeFile)[0]
            previewPath = os.path.join("./previews", f"{themeName}.svg")

            subprocess.run([previewScript, os.path.join(themesDir, themeFile), "-o", previewPath])

            readme.write(f"## [{themeName}]({os.path.join(themesDir, themeFile)})\n")
            readme.write(f"![{themeName} preview]({previewPath})\n\n")

genREADME(args.themesDir, args.previewScript)
