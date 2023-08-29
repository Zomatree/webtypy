import os
from pathlib import Path

from js_pyi.main_produce import generate_python

def apply_patches():
    os.chdir("js_pyi/w3c_webref")

    for file in os.listdir("ed/idlpatches"):
        os.system(f"git apply ed/idlpatches/{file}")

    os.chdir("../..")

def main():
    apply_patches()

    code = generate_python()
    path = (Path(__file__).parent / 'src/js-stubs/__init__.pyi')
    path.write_text(code)
    print(f'{len(code.splitlines())} lines written in {path}')


if __name__ == '__main__':
    main()
