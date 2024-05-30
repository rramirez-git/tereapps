"""
Ejecucion de PyDoc para generar documentos y depositarla en el directorio
./docs/pydoc
"""
import os
import subprocess
import glob
import shutil

def main():
    docs_dir = os.path.join('docs', 'pydoc')
    subprocess.call(
        ['python', '-m', 'pydoc', '-w', './'])
    
    for file in glob.glob("*.html"):
        if "main_app" not in file:
            try:
                os.remove(os.path.join(docs_dir, file))
            except FileNotFoundError:
                pass
            shutil.move(file, docs_dir)
        else:
            os.remove(file)

if __name__ == "__main__":
    main()
