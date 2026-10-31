#### 1. Nome do projeto;
Spotypobre

#### 2. Tema escolhido; 
Sistema de música.

#### 3. Integrantes do grupo;
- Eloá Costa de Araujo - 20241101110008
- Guilherme de Medeiros Dantas - 20241101110029
- Jamily Gabrielle de Medeiros - 20241101110012
- Maria Vitória Santos Silva - 20241101110024 

#### 4. Responsabilidade principal de cada integrante; 
- Eloá Costa - CRUD
- Guilherme Medeiros- Readme e Especificações Solicitadas
- Jamily Gabrielle - Modelagem/Implementação do BD
- Maria Vitória - Rotas Básicas e Templates
#### 5. Descrição do sistema;
O sistema permite ao usuário registrar e acompanhar sua músicas favoritas; os artistas que mais lhe apetecem; Além, claro, dos albuns que mais gosta.
    
#### 6. Entidades do sistema;
    Entidade 1: Álbum
    Entidade 2: Faixa 
    Entidade 3: Artista

#### 7. Explicação do relacionamento 1:N ;
O relacionamento 1:N ocorre entre álbum e faixa. Pois, um álbum possui várias faixas.

#### 8. Explicação do relacionamento N:N ;
Já o relacionamento N:N está presente no relacionamento entre Artista e Álbum. Um artista possui vários albuns.

#### 9. Instruções para instalar dependências;
Na pasta raiz do projeto, execute:
```bash
pip install -r requirements.txt
```

#### 10. Instruções para criar ou popular o banco;
Na pasta raiz do projeto, execute os comandos abaixo. O script cria o banco SQLite e as tabelas, se ainda não existirem, e adiciona os dados de demonstração:

```powershell
cd projeto
python seed.py
```

O banco `spotypobre.db` será criado dentro da pasta `projeto`. Use `demo` e a senha `demo123`. Se esse usuário já existir, o script avisa que os dados já foram inseridos.

#### 11. Instruções para executar o sistema;
Após instalar as dependências, na pasta raiz do projeto execute:
```bash
cd projeto
python app.py
```

Em seguida, acesse http://127.0.0.1:5000 no navegador.

#### 12. Principais dificuldades encontradas;
O uso de sessões; Indetificação de erros inésperados; Como modelar o relacionamento N:N no código e usar a tabela intermediaria.

#### 13. Declaração de autoria.
Declaração de autoria:
Declaro que desenvolvi este projeto compreendendo o código entregue e que sou
capaz de explicar e modificar suas partes principais.

Uso de IA:
[ ] Não utilizei IA generativa.
[x] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.

Descrição do uso, se houver: Usamos a IA para nos auxiliar a detectar erros, entender quais conteudos precisariamos mobilizar para resolver ou o que ainda estava faltando implementar para que o projeto funcionasse. Utilizamos para nos ajudar a popular o banco também. 