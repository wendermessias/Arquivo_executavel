<h1>Arquivo Executável em Python</h1>

  <h3>Primeiro instale essa biblioteca abaixo no cmd com as teclas
    " Win + R = Executar “ 'cmd' + Enter "</h3>

  <p><b> No 'cmd' digite "pip install pyinstaller" e aperte enter</b></p>
  <p><b>Depois que a biblioteca já estiver instalada faremos o código em python abaixo: </b></p>
  <p> "import time from datetime import datetime </p>
  <p>def generate_years(): for ano in range(1, int(datetime.now().year) + 1):</p>
  <p>print(f'Estamos no ano {ano}') should_run_again()</p>
  <p>def should_run_again(): answer = input('Executar novamente?(y/n) : ')</p>
  <p>if answer == 'y': generate_years() if answer == 'n':</p>
  <p>print('Saindo do programa agora... Tchau :)'</p>
  <p>if __name__ == '__main__': generate_years()"</p>
  <p>Caso o codigo não esteja devidamente identado, aperte as seguintes teclas <b> 'shfit'  'Alt'+ 'F'.</b></p>
  <p><b>Depois já com esse código acima salvo, dentro do VSCode iremos ao terminal é usaremos esse código:</b></p>
  <p><b>No 'cmd do vcCode' digite "pyinstaller --onefile year-counter-generator.py"</b></p>
  <p>Assim que executarmos esse código ira gerar uma pasta como o nome de dist, criando assim um arquivo executável.</p>
  <p>Agora vamos fazer para não aparecer no console rodando em segundo plano.</p>
  <p><b>Depois que a biblioteca já estiver instalada faremos o código em python abaixo:</b></p>
  <p>import os class FileGenerator:</p>
  <p>def __init__(self): pass</p>
  <p>def Start(self):self.make_initial_folders()</p>
  <p>self.create_files_per_folders()</p>
  <p>def make_initial_folders(self):</p>
  <p>os.mkdir('Folder 1')os.mkdir('Folder 2')</p>
  <p>os.mkdir('Folder 3')os.mkdir('Folder 4')</p>
  <p>def create_files_per_folders(self):</p>
  <p>base_directory = os.getcwd()</p>
  <p>os.chdir('Folder 1')with open('text_file.txt', 'w') as file:</p>
  <p>file.write('Hello Pythonista')pass</p>
  <p>os.chdir(base_directory)os.chdir('Folder 2')</p>
  <p>with open('text_file.txt', 'w') as file:</p>
  <p>file.write('Hello Pythonista')pass</p>
  <p>os.chdir(base_directory)os.chdir('Folder 3')</p>
  <p>with open('text_file.txt', 'w') as file:</p>
  <p>file.write('Hello Pythonista')pass</p>
  <p>os.chdir(base_directory)os.chdir('Folder 4')</p>
  <p>with open('text_file.txt', 'w') as file:</p>
  <p>file.write('Hello Pythonista')pass</p>
  <p>generator = FileGenerator()generator.Start()</p>
  <p>Caso o codigo não esteja devidamente identado, aperte as seguintes teclas <b> 'shfit'  'Alt'+ 'F'.</b></p>
  <p><b>Depois que a biblioteca já estiver instalada faremos o código em python abaixo:</b></p>
  <p><b>No 'cmd do vcCode' digite "pyinstaller --onefile --noconsole .\file-generator.py"</b></p>
  <p>Gerando assim 4 pastas sem mostrar o código rodando.</p>