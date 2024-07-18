# TING (Trybe is not Google) 🔍

Este projeto visa consolidar meus aprendizados em assuntos relacionados a estruturas de dados como, por exemplo, Pilhas, Filas, Deques, Listas ligadas e Listas duplamente ligadas.

Além de reforçar vários conceitos e habilidades que vi durante os estudos. Utilizei também conceitos de manipulação de arquivos TXT.


<details>
  <summary><strong>👨‍💻 O que foi desenvolvido:</strong></summary><br />


Neste projeto implementei um programa que simula um algoritmo de indexação de documentos similar ao do Google. O programa é capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa desenvolvido tem dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.
</details>

<details>
  <summary><strong>🚵 Habilidades exercitadas:</strong></summary><br />

   - Manipular Pilhas;
  
   - Manipular Deque;
  
   - Manipular Nó & Listas Ligadas e;
  
   - Manipular Listas Duplamente Ligadas.

</details>


## Instalando o projeto
<details>
  <summary><strong>📋Passo a passo</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:Mandytrajano90/TING.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd TING`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

Com o seu ambiente virtual ativo as dependências serão instaladas neste ambiente.
  
  :eyes: Caso precise desativar o ambiente virtual execute o comando _"deactivate"_.
  
  :warning: Lembre-se de ativar o ambiente virtual novamente quando voltar a trabalhar no projeto.
</details>


<details>
  <summary><strong>🛠 Testes</strong></summary><br />

 👀 **Para executar os testes certifique-se de que você está com o ambiente virtual ativado.**

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

</details>


## 👁️ Dê uma olhada no códido



https://github.com/user-attachments/assets/ccd754ec-7442-42b9-9f85-6948308f0942


<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
