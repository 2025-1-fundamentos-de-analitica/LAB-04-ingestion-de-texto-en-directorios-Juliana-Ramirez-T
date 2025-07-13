import os
import zipfile
import pandas as pd

# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

def pregunta_01():
    #Crear las rutasss
    zip_path = "files/input.zip"
    #creara la carpeta "input" en la raiz del repositorio
    repo_dir = "files/input_tmp"
    output_dir = "files/output"

    #Crear carpetas que no existen
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(repo_dir, exist_ok=True)

    #Se descomprime el zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(repo_dir)

    #ubica raiz
    for root, dirs, files in os.walk(repo_dir):
        if 'train' in dirs and 'test' in dirs:
            data_root = root
            break
    else:
        print("Error. No se encontró la info.")
        return

    
    def proceso(x):
        registro = []
        base_path = os.path.join(data_root, x)
        for i in os.listdir(base_path):
            carp = os.path.join(base_path, i)
            for j in os.listdir(carp):
                ruta = os.path.join(carp, j)
                with open(ruta, encoding='utf-8') as f:
                    texto = f.read().strip()
                    registro.append({'phrase': texto, 'target': i}) 
        return pd.DataFrame(registro)

    df_train = proceso("train")
    df_test = proceso("test")

    #Guardar resultados
    df_train.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)
    df_test.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)



    """"
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
