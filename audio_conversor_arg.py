import os
import sys
import argparse
from pydub import AudioSegment

def convert_m4a_to_mp3(input_dir, output_dir):
    # percorrer todos os diretórios e subdiretórios
    for subdir, dirs, files in os.walk(input_dir):
        # gerar o caminho para o diretório de saída correspondente
        output_subdir = os.path.join(output_dir, os.path.relpath(subdir, input_dir))
        
        # criar o diretório de saída se não existir
        os.makedirs(output_subdir, exist_ok=True)
        
        for file in files:
            # verificar se o arquivo é do formato m4a
            if file.endswith('.m4a'):
                # abrir o arquivo de áudio usando pydub
                sound = AudioSegment.from_file(os.path.join(subdir, file))
                
                # gerar o caminho para salvar o arquivo mp3
                mp3_file_path = os.path.join(output_subdir, os.path.splitext(file)[0] + '.mp3')
                
                # converter o arquivo m4a para mp3 e salvar
                sound.export(mp3_file_path, format='mp3')

if __name__ == '__main__':
    # Parsing dos argumentos de linha de comando
    parser = argparse.ArgumentParser(description='Converte arquivos M4A em MP3.')
    parser.add_argument('input_dir', help='input directory')
    parser.add_argument('output_dir', help='output directory')
    args = parser.parse_args()
	
    # Executa a conversão de .M4A para .MP3
    convert_m4a_to_mp3(args.input_dir, args.output_dir)
