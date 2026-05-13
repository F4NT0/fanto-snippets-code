# Guia de Configuração do PowerShell

Este documento mostra passo a passo como configurar o PowerShell com as mesmas configurações utilizadas neste ambiente.

## 📋 Visão Geral da Configuração

- **Prompt**: Starship (configurado no profile)
- **Tema**: Starship com configuração personalizada
- **Módulos PowerShell**: PSReadLine, Terminal-Icons, oh-my-posh-core, chocolateyProfile
- **Gerenciador de Pacotes**: Scoop, Winget, Chocolatey
- **Shell**: PowerShell 7 (preview)

## 🚀 Passo a Passo da Configuração

### 1. Instalar PowerShell 7

```powershell
# Via Winget
winget install Microsoft.PowerShell

# Ou via Scoop
scoop install pwsh
```

### 2. Instalar Scoop (Gerenciador de Pacotes)

```powershell
# Executar no PowerShell normal (não como administrador)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

### 3. Instalar Pacotes via Scoop

```powershell
# Ferramentas úteis
scoop install bat          # cat com realce de sintaxe
scoop install fzf          # fuzzy finder
scoop install ripgrep      # grep rápido
scoop install neovim       # editor moderno
scoop install gh           # GitHub CLI
scoop install glab         # GitLab CLI
scoop install lazydocker   # interface para Docker
scoop install glow         # leitor de markdown
scoop install atac         # cliente TUI para AWS
scoop install chafa        # visualizador de imagens
scoop install charm-gum    # ferramentas Charm
scoop install crush        # compressor de arquivos
```

### 4. Instalar Oh-My-Posh

```powershell
# Via Winget
winget install JanDeDobbeleer.OhMyPosh

# Ou manualmente
winget install oh-my-posh
```

### 5. Instalar Starship (Prompt)

```powershell
# Via Winget
winget install starship

# Ou via Scoop
scoop install starship

# Ou via Cargo (se tiver Rust instalado)
cargo install starship
```

### 6. Instalar Módulos do PowerShell

```powershell
# Terminal-Icons (ícones para arquivos)
Install-Module -Name Terminal-Icons -Repository PSGallery -Force

# PSReadLine (geralmente já vem instalado)
Install-Module -Name PSReadLine -Repository PSGallery -Force -SkipPublisherCheck
```

### 7. Configurar o Profile do PowerShell

O arquivo de profile está localizado em:
```
C:\Users\SEU_USUARIO\OneDrive - Dell Technologies\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

Se não existir, crie o diretório e o arquivo:

```powershell
# Criar diretório se não existir
New-Item -ItemType Directory -Path "$HOME\Documents\PowerShell" -Force

# Criar arquivo de profile
New-Item -ItemType File -Path "$PROFILE" -Force

# Editar o profile
notepad $PROFILE
```

#### Conteúdo do Profile

```powershell
#================================
#    POWERSHELL CONFIGURATION
#================================

#------------
#   STARSHIP
#------------

$ENV:STARSHIP_CONFIG = "$HOME\.config\starship.toml"
Invoke-Expression (&starship init powershell)
```

### 8. Configurar o Starship

Crie o arquivo de configuração do Starship:

```powershell
# Criar diretório de configuração
New-Item -ItemType Directory -Path "$HOME\.config" -Force

# Criar arquivo de configuração
New-Item -ItemType File -Path "$HOME\.config\starship.toml" -Force

# Editar configuração
notepad "$HOME\.config\starship.toml"
```

#### Conteúdo do starship.toml

```toml
# ~/.config/starship.toml

add_newline = true
format = """$os$username$hostname$kubernetes$directory$git_branch$git_status"""

# Drop ugly default prompt characters
[character]
success_symbol = ''
error_symbol = ''

# ---

[os]
format = '[$symbol](bold white) '   
disabled = false

[os.symbols]
Windows = ''
Arch = '󰣇'
Ubuntu = ''
Macos = '󰀵'

# ---

# Shows the username
[username]
style_user = 'white bold'
style_root = 'black bold'
format = '[$user]($style) '
disabled = false
show_always = true

# Shows current directory
[directory]
truncation_length = 1
truncation_symbol = '…/'
home_symbol = '󰋜 ~'
read_only_style = '197'
read_only = '  '
format = ' [$path]($style)[$read_only]($read_only_style) '

# Shows current git branch
[git_branch]
symbol = ' '
format = 'via [$symbol$branch]($style)'
style = 'bold green'

# Shows current git status
[git_status]
format = '[$all_status$ahead_behind]($style) '
style = 'bold green'
conflicted = '🏳'
up_to_date = ''
untracked = ' '
ahead = '⇡${count}'
diverged = '⇕⇡${ahead_count}⇣${behind_count}'
behind = '⇣${count}'
stashed = ' '
modified = ' '
staged = '[++\($count\)](green)'
renamed = '襁 '
deleted = ' '

# Shows kubernetes context and namespace
[kubernetes]
format = 'via [󱃾 $context\($namespace\)](bold purple) '
disabled = false

# ---

[vagrant]
disabled = true

[docker_context]
disabled = true

[helm]
disabled = true

[python]
disabled = true

[nodejs]
disabled = true

[ruby]
disabled = true

[terraform]
disabled = true
```

### 9. Configurar PSReadLine

Adicione ao seu profile (opcional, já vem com configurações padrão):

```powershell
# Configurações do PSReadLine
Set-PSReadLineOption -EditMode Windows
Set-PSReadLineOption -HistoryNoDuplicates
Set-PSReadLineOption -HistorySearchCursorMovesToEnd
Set-PSReadLineOption -PredictionSource None
Set-PSReadLineOption -ShowToolTips
```

### 10. Configurar Variáveis de Ambiente (PATH)

Adicione ao PATH os diretórios necessários. Isso pode ser feito via:

```powershell
# Adicionar Scoop shims ao PATH
$env:PATH += ";$env:USERPROFILE\scoop\shims"

# Adicionar outros diretórios úteis
$env:PATH += ";$env:USERPROFILE\bin"
$env:PATH += ";$env:USERPROFILE\.local\bin"
```

Para tornar permanente, adicione ao profile ou configure nas variáveis de ambiente do Windows.

### 11. Instalar Ferramentas Adicionais via Winget

```powershell
# Ferramentas de desenvolvimento
winget install Gyan.FFmpeg
winget install jqlang.jq
winget install sharkdp.fd
winget install junegunn.fzf
winget install ajeetdsouza.zoxide
winget install JesseDuffield.lazygit
winget install Fastfetch-cli.Fastfetch
winget install sxyazi.yazi
winget install gokcehan.lf
```

### 12. Configurar Fontes Nerd Font

Para que os ícones funcionem corretamente, instale uma Nerd Font:

1. Baixe uma Nerd Font de https://www.nerdfonts.com/
2. Recomendado: JetBrains Mono Nerd Font, FiraCode Nerd Font, ou Cascadia Code Nerd Font
3. Instale a fonte no Windows
4. Configure seu terminal (Windows Terminal, VS Code, etc.) para usar a fonte instalada

### 13. Configurar Windows Terminal (Opcional)

No Windows Terminal, adicione este perfil ao seu `settings.json`:

```json
{
    "guid": "{...}",
    "name": "PowerShell 7",
    "commandline": "pwsh.exe",
    "fontFace": "JetBrainsMono Nerd Font",
    "fontSize": 12,
    "colorScheme": "Campbell",
    "hidden": false
}
```

## 📦 Pacotes Instalados

### Via Scoop
- bat (0.26.1)
- fzf (0.67.0)
- ripgrep (15.1.0)
- neovim (0.11.0)
- gh (2.92.0)
- glab (1.95.0)
- lazydocker (0.24.1)
- glow (2.1.1)
- atac (0.19.0)
- chafa (1.18.2)
- charm-gum (0.17.0)
- crush (0.66.0)

### Via Winget
- Oh My Posh (24.18.1)
- FFmpeg
- jq
- fd
- fzf
- zoxide
- lazygit
- fastfetch
- yazi
- lf

### Módulos PowerShell
- PSReadLine (2.3.6)
- Terminal-Icons (0.11.0)
- oh-my-posh-core
- chocolateyProfile

## 🔧 Solução de Problemas

### Starship não funciona
Se o Starship não for encontrado, verifique se:
1. Está instalado corretamente
2. Está no PATH
3. O caminho no profile está correto

### Ícones não aparecem
1. Certifique-se de que uma Nerd Font está instalada
2. Configure seu terminal para usar a Nerd Font
3. Reinicie o terminal

### Profile não carrega
1. Verifique se o arquivo de profile existe: `Test-Path $PROFILE`
2. Verifique o caminho do profile: `$PROFILE`
3. Recarregue o profile: `. $PROFILE`

## 📝 Arquivos de Configuração

- **PowerShell Profile**: `$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`
- **Starship Config**: `$HOME\.config\starship.toml`
- **PSReadLine History**: `$HOME\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`

## 🎯 Próximos Passos

Após seguir este guia, você terá um ambiente PowerShell configurado com:
- ✅ Prompt moderno com Starship
- ✅ Ícones para arquivos e diretórios
- ✅ Ferramentas de desenvolvimento modernas
- ✅ Histórico de comandos aprimorado
- ✅ Autocompletar inteligente
- ✅ Suporte a Git integrado

---

**Nota**: Este guia foi baseado na configuração atual do ambiente. Algumas versões de pacotes podem ter sido atualizadas desde então.
