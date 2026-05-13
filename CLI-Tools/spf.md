# Superfile

Superfile é um gerenciador de arquivos de terminal moderno e sofisticado, projetado para desenvolvedores que vivem no terminal. Construído com Go e Bubble Tea, combina uma interface de usuário obsessivamente refinada com a velocidade e o poder das ferramentas de terminal.

## Características

- **Interface bonita**: Cada pixel elaborado obsessivamente. O superfile parece tão bom quanto seus aplicativos favoritos, mas vive inteiramente em seu terminal.
- **Funções completas**: Cópia de arquivo, movimentação, exclusão, renomeação, busca fuzzy, operações em massa, visualização de imagem. Tudo o que você precisa, nada que você não precisa.
- **Totalmente personalizável**: Remapeie cada tecla de atalho. Escolha qualquer tema. Ajuste cada borda e cor. O superfile se adapta ao seu fluxo de trabalho exato.
- **Múltiplos painéis**: Divida em vários painéis de diretório simultaneamente. Copie e cole entre painéis com apenas alguns pressionamentos de tecla.
- **Suporte a plugins**: Estenda com plugins da comunidade: integração de status do Git, monitoramento do sistema, comandos personalizados e muito mais.
- **Temas ricos**: 20+ temas integrados: Catppuccin, Nord, Tokyo Night, Dracula, Gruvbox, Rose Pine e muitos mais.

## Instalação

### Pré-requisitos

Antes de instalar, certifique-se de ter as seguintes ferramentas instaladas:
- [Any Nerd-font](https://www.nerdfonts.com/font-downloads), e defina a fonte para seu aplicativo de terminal para usar a fonte Nerd instalada

> **Nota**: Se você não instalar a fonte Nerd, o superfile ainda funcionará, mas a interface pode parecer um pouco estranha. É recomendável desabilitar a opção de fonte Nerd para evitar esse problema.

### Scripts de Instalação

#### Linux / macOS

Com `curl`:
```bash
bash -c "$(curl -sLo- https://superfile.dev/install.sh)"
```

Ou com `wget`:
```bash
bash -c "$(wget -qO- https://superfile.dev/install.sh)"
```

Para especificar uma versão:
```bash
SPF_INSTALL_VERSION=1.2.1 bash -c "$(curl -sLo- https://superfile.dev/install.sh)"
```

#### Windows

Com `powershell`:
```powershell
powershell -ExecutionPolicy Bypass -Command "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/install.ps1'))"
```

Para desinstalar:
```powershell
powershell -ExecutionPolicy Bypass -Command "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/uninstall.ps1'))"
```

Para especificar uma versão:
```powershell
powershell -ExecutionPolicy Bypass -Command "$env:SPF_INSTALL_VERSION=1.2.1; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://superfile.dev/install.ps1'))"
```

Com [Winget](https://winget.run/):
```bash
winget install --id yorukot.superfile
```

Com [Scoop](https://scoop.sh/):
```bash
scoop install superfile
```

### Pacotes mantidos pela comunidade

#### Arch Linux
```bash
sudo pacman -S superfile
```

Versão mais recente do GitHub:
```bash
yay -S superfile-git
```

#### Homebrew
```bash
brew install superfile
```

#### NixOS
```bash
nix profile install github:yorukot/superfile#superfile
```

#### Pixi
```bash
pixi global install superfile
```

#### X-CMD
```bash
x env use superfile
```

### Iniciar o superfile

Após concluir a instalação, reinicie o terminal (se necessário) e execute:
```bash
spf
```

## Atalhos de Teclado (Keyboard Shortcuts)

### Geral

| Função | Tecla | Nome da variável |
|--------|-------|------------------|
| Abrir superfile | `spf` | - |
| Confirmar seleção ou digitação | `enter`, `right` | `confirm_typing` |
| Sair da digitação, modal ou superfile | `esc`, `q` | `quit` |
| Sair do superfile e cd para pasta atual | `Q` | `cd_quit` |
| Cancelar digitação | `ctrl+c`, `esc` | `cancel_typing` |
| Abrir menu de ajuda (lista de atalhos) | `?` | `open_help_menu` |
| Alternar rodapé | `F` | `toggle_footer` |

> **Nota**: "Quit superfile and cd to current folder" (`cd_quit`) requer os mesmos scripts que a configuração "cd_on_quit"

### Navegação de Painel

| Função | Tecla | Nome da variável |
|--------|-------|------------------|
| Criar novo painel de arquivo | `n` | `create_new_file_panel` |
| Dividir painel de arquivo focado | `N` (shift+n) | `split_file_panel` |
| Fechar o painel de arquivo focado | `w` | `close_file_panel` |
| Alternar painel de visualização de arquivo | `f` | `toggle_file_preview_panel` |
| Focar no próximo painel de arquivo | `tab`, `L` (shift+l) | `next_file_panel` |
| Focar no painel de arquivo anterior | `shift+left`, `H` (shift+h) | `previous_file_panel` |
| Focar no painel de barra de processos | `p` | `focus_on_process_bar` |
| Focar na barra lateral | `s` | `focus_on_side_bar` |
| Focar no painel de metadados | `m` | `focus_on_metadata` |
| Abrir prompt no modo shell | `:` | `open_command_line` |
| Abrir prompt no modo spf | `>` | `open_spf_prompt` |
| Abrir modal de navegação zoxide | `z` | `open_zoxide` |

### Movimento de Painel

| Função | Tecla | Nome da variável |
|--------|-------|------------------|
| Para cima | `up`, `k` | `list_up` |
| Para baixo | `down`, `j` | `list_down` |
| Voltar para pasta pai | `h`, `left`, `backspace` | `parent_folder` |
| Alternar menu de opções de ordenação | `o` | `open_sort_options_menu` |
| Selecionar todos os itens no painel de arquivo focado | `A` (shift+a) | `file_panel_select_all_item` (modo de seleção apenas) |
| Selecionar para cima com o cursor | `shift+up`, `K` (shift+k) | `file_panel_select_mode_item_select_up` (modo de seleção apenas) |
| Selecionar para baixo com o cursor | `shift+down`, `J` (shift+j) | `file_panel_select_mode_item_select_down` (modo de seleção apenas) |
| Alternar exibição de arquivo dot | `.` | `toggle_dot_file` |
| Alternar barra de pesquisa ativa | `/` | `search_bar` |
| Alternar entre modo de seleção ou modo normal | `v` | `change_panel_mode` |
| Fixar ou Desfixar pasta na barra lateral (pode ser salvo automaticamente) | `P` (shift+p) | `pinned_folder` |

### Operações de Arquivo

| Função | Tecla | Nome da variável |
|--------|-------|------------------|
| Criar arquivo ou pasta (/ termina criando uma pasta) | `ctrl+n` | `file_panel_item_create` |
| Renomear arquivo ou pasta | `ctrl+r` | `file_panel_item_rename` |
| Copiar arquivo ou pasta (ou ambos) | `ctrl+c` | `copy_single_item` (modo normal) / `file_panel_select_mode_item_copy` (modo de seleção) |
| Cortar arquivo ou pasta (ou ambos) | `ctrl+x` | `file_panel_select_mode_item_cut` |
| Colar todos os itens na área de transferência | `ctrl+v`, `ctrl+w` | `paste_item` |
| Excluir arquivo ou pasta (ou ambos) | `ctrl+d`, `delete` | `delete_item` (modo normal) / `file_panel_select_mode_item_delete` (modo de seleção) |
| Copiar caminho do arquivo ou diretório atual | `ctrl+p` | `copy_path` |
| Extrair arquivo zip | `ctrl+e` | `extract_file` (modo normal) |
| Compactar arquivo ou pasta para arquivo .zip | `ctrl+a` | `compress_file` (modo normal) |
| Abrir arquivo com seu editor padrão | `e` | `open_file_with_editor` (modo normal) |
| Abrir diretório atual com editor padrão | `E` (shift+e) | `current_directory_with_editor` (modo normal) |
| Excluir permanentemente arquivo ou pasta (ou ambos) | `D` (shift+d) | `permanently_delete_items` (modo normal) / `file_panel_select_mode_item_delete` (modo de seleção) |

## Como Usar

### Iniciando

Abra um terminal, digite `spf` e pressione `enter` para iniciar o superfile. Para sair, pressione `q` ou `esc`.

### Navegação de Painel

Quando o superfile está em execução, ele exibe cinco painéis:
- **sidebar** (barra lateral)
- **file** (arquivo)
- **processes** (processos)
- **metadata** (metadados)
- **clipboard** (área de transferência)
- **command execution bar** (barra de execução de comando)

O painel de arquivo é a visualização focada por padrão. Você pode alterar o foco para outros três painéis:

- Pressione `s` para focar na barra lateral
- Pressione `p` para focar nos processos
- Pressione `m` para focar nos metadados
- Pressione `:` para abrir a barra de execução de comando

Para retornar o foco ao painel de arquivo, pressione a mesma tecla novamente. Para a barra de execução de comando, você precisa pressionar `esc` ou `ctrl+c`.

Você também pode pressionar `f` para mostrar ou ocultar a janela de visualização. Pressione `F` para ocultar ou mostrar todos os painéis do rodapé.

### Múltiplos Painéis

Para criar mais painéis de arquivo, pressione `n`. Pressione `w` para fechar o painel de arquivo focado.

Para mover-se através de múltiplos painéis de arquivo, pressione `tab` ou `L` (shift+l). Para mover para o painel anterior, pressione `shift+left` ou `H` (shift+h).

### Movimento de Painel

O superfile fornece múltiplos atalhos para mover-se através de diretórios. O cursor de colchete angular `>` indica onde você está.

Enquanto focado no painel de arquivo, mova o cursor para cima com `up` ou `k` e para baixo com `down` ou `j`.

Depois de navegar para seu arquivo/pasta, pressione `enter` ou `l` para confirmar sua seleção. Arquivos são abertos com seu aplicativo padrão (se nenhum definido, não haverá resposta) e pastas são abertas para visualização. Pressione `h` ou `backspace` para voltar ao diretório pai.

Pastas podem ser fixadas no painel da barra lateral. Navegue e abra sua pasta. Pressione `P` (shift+p) para fixar ou desafixar.

Pressione `o` para abrir o menu de opções de ordenação. Você pode ordenar por:
- Name (Nome)
- Size (Tamanho)
- Date Modified (Data de modificação)

Pressione `enter` para confirmar sua opção de ordenação. Pressione `esc`, `o` ou `ctrl+c` para cancelar. Para inverter a ordem da ordenação, pressione `R` (shift+r).

Pressione `/` para abrir a barra de pesquisa. Digite o nome (você pode precisar primeiro excluir o `/` se ele for preenchido automaticamente). O superfile pesquisa no diretório atual e exibe dinamicamente os resultados. Para sair da barra de pesquisa, pressione `ctrl+c` ou `esc`.

Pressione `.` para mostrar ou ocultar arquivos dot.

### Modo de Seleção

Use o modo de seleção para operações em massa. Se você estiver familiarizado com o Vim, o modo de seleção é similar ao modo visual do Vim.

Pressione `v` para alternar entre o modo de seleção e o modo normal (navegador).

Uma vez no modo de seleção, você pode executar operações de arquivo em todos os arquivos/pastas selecionados. Os atalhos de movimento de painel também funcionam no modo de seleção.

> As seguintes operações só podem ser executadas enquanto estiver no modo de seleção. Seu modo atual é exibido no canto inferior direito do painel de arquivo (Select ou Browser).

Para fazer seleções, navegue para seu arquivo/pasta e pressione `enter` ou `L` (shift+l). Pressione a mesma tecla novamente para desselecionar.

Isso pode se tornar tedioso quando você tem um grande número de itens. Em vez disso, você pode pressionar `shift+up` ou `K` (shift+k) para selecionar tudo acima do cursor. Pressione `shift+down` ou `J` (shift+j) para selecionar tudo abaixo do cursor.

Você também pode pressionar `A` (shift+a) para selecionar tudo no diretório atual.

### Operações de Arquivo

> Apenas copiar, cortar e excluir podem ser usados no modo de seleção.

**Criar um novo arquivo** com `ctrl+n`. Digite o nome do seu novo arquivo e pressione `enter`. Para criar uma nova pasta, adicione `/` ao final do nome.

> Você pode criar um diretório, subdiretório e arquivo em uma string. Por exemplo: `directory/subdirectory/filename`

**Renomear** apontando seu cursor para um arquivo/pasta e pressionando `ctrl+r`.

**Copiar** pressionando `ctrl+c`.

**Cortar** pressionando `ctrl+x`.

Itens cortados e copiados são exibidos no painel da área de transferência (canto inferior direito). O progresso de suas operações é exibido no painel de processos (canto inferior esquerdo).

**Colar** pressionando `ctrl+v`.

> Em alguns terminais, por exemplo Windows Powershell, `ctrl+v` cola a entrada da área de transferência para o terminal. Portanto, `ctrl+v` pode não funcionar para colar. Você pode adicionar o atalho `ctrl+w` para colar, ou substituir o comportamento padrão de `ctrl+v` no seu terminal.

**Excluir** pressionando `ctrl+d`.

> A exclusão aqui não é exclusão direta, mas será colocada na lixeira. No entanto, quando você usa um disco rígido externo, ele será excluído diretamente.

**Compactar** pressionando `ctrl+a`. **Descompactar** pressionando `ctrl+e`.

**Abrir um arquivo com um editor** pressionando `e`.

**Abrir o diretório atual com um editor** pressionando `E` (shift+e).

Para alterar o editor de arquivo padrão, você pode definir a variável de ambiente `EDITOR` no seu terminal ou pode usar a opção de configuração `editor` (tem prioridade sobre a variável de ambiente `EDITOR`). Para alterar o editor de diretório padrão, você pode usar a opção de configuração `dir_editor`.

Por exemplo:
```bash
EDITOR=nvim
```

Isso definirá o Neovim como seu editor padrão. Depois de definir isso, o Neovim será usado ao abrir arquivos com os atalhos de tecla `e`.

No arquivo de configuração:
```toml
editor = "nano"
dir_editor = "vi"
```

Isso definirá `nano` como seu editor padrão, e `vi` como seu editor de diretório padrão.

> Se o seu editor de diretório não suportar abrir o diretório atual com um editor, você pode encontrar um erro ao pressionar `E`.

### SPF Prompt

#### Modo Shell

Pressione `:` para abrir o prompt no modo shell e executar qualquer comando shell no diretório atual.

> Você não receberá nenhuma saída stdout. Por enquanto, isso é destinado a executar manipulações de arquivo mais complexas via shell, em vez de lidar com saídas interativas. Você poderá ver o código de saída do comando.

#### Modo SPF

Pressione `>` para abrir o prompt no modo SPF.

Neste modo, você pode executar estes comandos spf:
- `split` - Abre um novo painel no caminho do painel de arquivo atual
- `open <PATH>` - Abre um novo painel em um caminho especificado
- `cd <PATH>` - Altera o diretório do painel atual

Neste modo, você pode substituir variáveis de ambiente do shell via `${}`, comandos do shell via `$()` e prefixar o caminho com `~` para substituir para o diretório home. Por exemplo:
- `cd ${HOME}` ou `cd ~/xyz`
- `open $(dirname $(which bash))`

Pressione `esc` ou `ctrl+c` para sair do Prompt.

## Temas Disponíveis

O superfile possui 20+ temas integrados:

- 0x96f
- Ayu Dark
- Blood
- Catppuccin Frappe
- Catppuccin Latte
- Catppuccin Macchiato
- Catppuccin Mocha
- Dracula
- Everforest Dark Medium
- Everforest Dark Hard
- Gruvbox
- Gruvbox Dark Hard
- Hacks
- Kaolin
- Monokai
- Nord
- OneDark
- Poimandres
- Rosé Pine
- Sugarplum
- Tokyonight

## Plugins

### Metadata
- **Descrição:** Mostra metadados mais detalhados para arquivos e diretórios
- **Requisitos:** [`exiftool`](https://exiftool.org)
- **Nome da configuração:** `metadata`

### Zoxide
- **Descrição:** Integração de salto inteligente de diretório com zoxide. Navegue para diretórios usados frequentemente rapidamente com uma interface modal pesquisável.
- **Requisitos:** [`zoxide`](https://github.com/ajeetdsouza/zoxide)
- **Nome da configuração:** `zoxide_support`
- **Uso:** Pressione `z` para abrir o modal de navegação zoxide. Comece a digitar para pesquisar diretórios, use as setas para navegar pelos resultados e pressione Enter para pular para um diretório.

## Configuração

### Caminho do Arquivo de Configuração

O superfile usa arquivos de configuração para personalizar atalhos, temas e outras opções.

#### Linux
- `~/.config/superfile/hotkeys.toml`
- `~/.config/superfile/config.toml`

#### macOS
- `~/Library/Application Support/superfile/hotkeys.toml`
- `~/Library/Application Support/superfile/config.toml`

#### Windows
- `%LOCALAPPDATA%/superfile/hotkeys.toml`
- `%LOCALAPPDATA%/superfile/config.toml`

Você pode usar a flag `--hotkey-file` para especificar um caminho diferente para o arquivo `hotkeys.toml`:
```bash
spf --hotkey-file /path/to/your/hotkey.toml
```

### Personalizar Atalhos

Todos os atalhos podem ser personalizados editando o arquivo `hotkeys.toml`. O design dos atalhos segue estes princípios:
- Todos os atalhos que alterarão arquivos usam `ctrl+key` (contanto que você não pressione ctrl, seus arquivos estarão sempre seguros)
- Classes de arquivo não-control usam as primeiras letras das palavras como atalhos

### Personalizar Temas

Você pode personalizar temas editando o arquivo de configuração ou escolhendo entre os temas integrados.

## Links Importantes

- **Site oficial:** https://superfile.dev/
- **Repositório GitHub:** https://github.com/yorukot/superfile
- **Documentação:** https://superfile.dev/overview
- **Discord:** https://discord.gg/YYtJ23Du7B
- **Licença:** MIT
