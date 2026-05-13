# CRUSH CLI AI

**Crush** é um assistente de codificação com IA baseado em terminal construído pela Charm que conecta a Large Language Models (LLMs) e dá a eles ferramentas poderosas para ler, escrever e executar código. Ao contrário dos assistentes de codificação baseados na web, o Crush vive diretamente em seu terminal e se integra perfeitamente ao seu fluxo de trabalho de desenvolvimento existente.

## Características

- **Multi-Modelo**: escolha entre uma ampla gama de LLMs ou adicione os seus próprios via APIs compatíveis com OpenAI ou Anthropic
- **Flexível**: alterne LLMs no meio da sessão enquanto preserva o contexto
- **Baseado em Sessões**: mantenha múltiplas sessões de trabalho e contextos por projeto
- **Aprimorado com LSP**: Crush usa LSPs para contexto adicional, assim como você
- **Extensível**: adicione recursos via MCPs (`http`, `stdio`, e `sse`)
- **Funciona em Todo Lugar**: suporte de primeira classe em todos os terminais no macOS, Linux, Windows (PowerShell e WSL), Android, FreeBSD, OpenBSD e NetBSD
- **Grau Industrial**: construído no ecossistema Charm, alimentando 25k+ aplicações, desde projetos open source de ponta até infraestrutura crítica de negócios

## O que é o Crush?

Crush é seu novo parceiro de codificação, agora disponível em seu terminal favorito. Suas ferramentas, seu código e seus fluxos de trabalho, conectados ao LLM de sua escolha.

### Interface de Terminal

O Crush fornece uma bela interface de usuário de terminal (TUI) construída com Bubble Tea, o mesmo framework que alimenta milhares de aplicações de terminal. A interface inclui:

- Streaming de mensagens em tempo real com renderização markdown
- Prompts de permissão de ferramenta interativos
- Gerenciamento de sessões e histórico
- Alternância de modelo e configuração

### Sistema de Ferramentas

O Crush fornece ao LLM um rico conjunto de ferramentas integradas:

- **Operações de arquivo**: `view`, `edit`, `write`, `multiedit`, `ls`, `glob`, `grep`
- **Execução de código**: `bash` (com suporte a jobs em segundo plano)
- **Inteligência de código**: integração LSP para diagnósticos, referências e símbolos
- **Acesso à web**: `fetch`, `download`
- **Integração MCP**: carregamento dinâmico de ferramentas de servidores MCP

## Instalação

### Windows

#### Scoop
```powershell
scoop bucket add charm https://github.com/charmbracelet/scoop-bucket.git
scoop install crush
```

#### Winget
```powershell
winget install charmbracelet.crush
```

### macOS / Linux

#### Homebrew
```bash
brew install charmbracelet/tap/crush
```

#### npm
```bash
npm install -g @charmland/crush
```

#### Go
```bash
go install github.com/charmbracelet/crush@latest
```

#### Arch Linux
```bash
yay -S crush
```

#### Nix (NUR)
```bash
nix profile install github:charmbracelet/nur#crush
```

## Configuração Inicial

### Variáveis de Ambiente

A maneira mais rápida de começar é configurar uma chave de API para seu provedor preferido. O Crush reconhece estas variáveis de ambiente:

| Variável de Ambiente | Provedor |
|---------------------|----------|
| `ANTHROPIC_API_KEY` | Anthropic (Claude) |
| `OPENAI_API_KEY` | OpenAI (GPT) |
| `GEMINI_API_KEY` | Google Gemini |
| `GROQ_API_KEY` | Groq |
| `OPENROUTER_API_KEY` | OpenRouter |
| `VERCEL_API_KEY` | Vercel AI Gateway |
| `HF_TOKEN` | Hugging Face Inference |
| `CEREBRAS_API_KEY` | Cerebras |
| `AWS_ACCESS_KEY_ID` | Amazon Bedrock |
| `AWS_SECRET_ACCESS_KEY` | Amazon Bedrock |
| `AWS_REGION` | Amazon Bedrock |
| `AZURE_OPENAI_API_ENDPOINT` | Azure OpenAI |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI |

Se você não definir uma chave de API, o Crush solicitará que você insira uma quando iniciá-lo pela primeira vez.

## Atalhos de Teclado (Keyboard Shortcuts)

### Globais

| Função | Tecla | Descrição |
|--------|-------|-----------|
| Sair | `ctrl+c` | Fecha o Crush |
| Ajuda | `ctrl+g` | Mostra mais informações |
| Comandos | `ctrl+p` | Abre a paleta de comandos |
| Modelos | `ctrl+m`, `ctrl+l` | Alterna entre modelos |
| Suspender | `ctrl+z` | Suspende a aplicação |
| Sessões | `ctrl+s` | Gerencia sessões |
| Mudar foco | `tab` | Alterna foco entre painéis |

### Editor (Input)

| Função | Tecla | Descrição |
|--------|-------|-----------|
| Adicionar arquivo | `/` | Adiciona arquivo ao contexto |
| Enviar mensagem | `enter` | Envia a mensagem |
| Abrir editor | `ctrl+o` | Abre editor externo |
| Nova linha | `shift+enter`, `ctrl+j` | Adiciona nova linha |
| Adicionar imagem | `ctrl+f` | Adiciona imagem |
| Colar imagem | `ctrl+v` | Cola imagem da área de transferência |
| Mencionar arquivo | `@` | Menciona arquivo específico |
| Comandos | `/` | Abre comandos |
| Modo de exclusão de anexo | `ctrl+r` | Entra no modo de exclusão |
| Cancelar modo de exclusão | `esc`, `alt+esc` | Cancela modo de exclusão |
| Excluir todos os anexos | `ctrl+r+r` | Exclui todos os anexos |
| Histórico anterior | `up` | Navega para mensagem anterior |
| Histórico próximo | `down` | Navega para próxima mensagem |

### Chat (Visualização)

| Função | Tecla | Descrição |
|--------|-------|-----------|
| Nova sessão | `ctrl+n` | Cria nova sessão |
| Adicionar anexo | `ctrl+f` | Adiciona anexo |
| Cancelar | `esc`, `alt+esc` | Cancela operação |
| Detalhes | `ctrl+d` | Alterna painel de detalhes |
| Alternar tasks | `ctrl+t`, `ctrl+space` | Alterna tasks/pills |
| Seção esquerda | `left` | Move para seção anterior |
| Seção direita | `right` | Move para próxima seção |
| Para baixo | `down`, `ctrl+j`, `j` | Scroll para baixo |
| Para cima | `up`, `ctrl+k`, `k` | Scroll para cima |
| Um item para cima | `shift+up`, `K` | Move um item para cima |
| Um item para baixo | `shift+down`, `J` | Move um item para baixo |
| Meia página para baixo | `d` | Scroll meia página para baixo |
| Página para baixo | `pgdown`, `space`, `f` | Scroll página para baixo |
| Página para cima | `pgup`, `b` | Scroll página para cima |
| Meia página para cima | `u` | Scroll meia página para cima |
| Início | `g`, `home` | Vai para o início |
| Fim | `G`, `end` | Vai para o fim |
| Copiar | `c`, `y`, `C`, `Y` | Copia texto selecionado |
| Limpar seleção | `esc`, `alt+esc` | Limpa seleção |
| Expandir/Recolher | `space` | Expande/recolhe código |

### Inicialização

| Função | Tecla | Descrição |
|--------|-------|-----------|
| Sim | `y`, `Y` | Confirma ação |
| Não | `n`, `N`, `esc`, `alt+esc` | Cancela ação |
| Selecionar | `enter` | Seleciona opção |
| Alternar | `left`, `right`, `tab` | Alterna entre opções |

### Atalhos Essenciais

Durante o chat com o Crush:
- `Ctrl+C`: Cancela operação atual ou sai
- `Ctrl+D`: Envia mensagem (alternativa ao Enter)
- `Setas Cima/Baixo`: Navega pelo histórico de mensagens
- `Ctrl+L`: Limpa a tela
- `Ctrl+R`: Reinicia servidores LSP

## Customização e Configuração

### Arquivos de Configuração

O Crush procura configuração nestes locais (em ordem de prioridade):

1. `.crush.json` (oculto, no diretório atual)
2. `crush.json` (no diretório atual)
3. `~/.config/crush/crush.json` (configuração global - Unix/Linux/macOS)
4. `%LOCALAPPDATA%\crush\crush.json` (configuração global - Windows)

A configuração específica do projeto (`.crush.json` ou `crush.json`) tem precedência sobre a configuração global. As configurações de múltiplos arquivos são mescladas, com arquivos mais específicos sobrescrevendo configurações globais.

### Estrutura Básica de Configuração

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "openai": {
      "api_key": "$OPENAI_API_KEY"
    }
  },
  "options": {
    "debug": false
  }
}
```

Inclua o campo `$schema` para habilitar autocompletar e validação em editores que suportam JSON Schema.

### Exemplo de Configuração Mínima

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "context_paths": ["AGENTS.md", "docs/"],
    "debug": false
  },
  "permissions": {
    "allowed_tools": ["view", "ls", "grep"]
  }
}
```

Esta configuração:
- Adiciona `AGENTS.md` e o diretório `docs/` ao contexto
- Permite ferramentas `view`, `ls`, e `grep` sem prompting

### Configuração de Provedores Customizados

O Crush suporta configurações de provedor customizado para APIs compatíveis com OpenAI e Anthropic.

#### API Compatível com OpenAI

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "deepseek": {
      "type": "openai-compat",
      "base_url": "https://api.deepseek.com/v1",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        {
          "id": "deepseek-chat",
          "name": "Deepseek V3",
          "context_window": 64000
        }
      ]
    }
  }
}
```

> **Nota**: Suportamos dois "tipos" para OpenAI. Escolha o certo para a melhor experiência:
> - `openai`: use quando proxyar ou rotear requisições através da OpenAI
> - `openai-compat`: use para provedores não-OpenAI com APIs compatíveis com OpenAI

#### API Compatível com Anthropic

```json
{
  "$schema": "https://charm.land/crush.json",
  "providers": {
    "custom-anthropic": {
      "type": "anthropic",
      "base_url": "https://custom-anthropic-endpoint.com",
      "api_key": "$CUSTOM_ANTHROPIC_API_KEY"
    }
  }
}
```

### Configuração de Skills

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "skills_paths": [
      "~/.config/crush/skills",
      "./project-skills"
    ]
  }
}
```

### Variáveis de Ambiente de Configuração

Você pode sobrescrever os locais de configuração usando variáveis de ambiente:

- `CRUSH_GLOBAL_CONFIG`: Sobrescreve o local de configuração global
- `CRUSH_GLOBAL_DATA`: Sobrescreve o local de dados global

### Dados Efêmeros

O Crush também armazena dados efêmeros, como estado da aplicação, em:

- Unix: `$HOME/.local/share/crush/crush.json`
- Windows: `%LOCALAPPDATA%\crush\crush.json`

## Como Usar

### Iniciando o Crush

Navegue para o diretório do seu projeto e inicie o Crush:

```bash
cd /path/to/your/project
crush
```

Executar o Crush do diretório do seu projeto permite que ele entenda a estrutura do seu codebase, leia arquivos de configuração e use LSPs para inteligência de código.

### Sessões

O Crush mantém contexto de conversação em sessões. Cada sessão está ligada ao seu diretório atual.

#### Criar nova sessão
```bash
crush --session my-feature
```

#### Listar todas as sessões
```bash
crush sessions
```

#### Retomar sessão
Basta navegar para o mesmo diretório e executar `crush` com o mesmo nome de sessão. O Crush lembra seu histórico de conversação e contexto do projeto.

Use sessões diferentes para diferentes features ou experimentos. Isso mantém seu contexto focado e facilita o rastreamento de mudanças.

### Alternando Modelos Mid-Session

Um dos recursos únicos do Crush é a capacidade de alternar provedores LLM sem perder contexto:

1. Pressione `Ctrl+M` (ou digite `/models`) durante uma sessão
2. Selecione um modelo diferente da lista
3. Continue sua conversa com o novo modelo

Isso é útil para:
- Comparar saídas de modelo na mesma tarefa
- Usar modelos mais rápidos para tarefas simples, mais poderosos para problemas complexos
- Gerenciar custos alternando para modelos mais baratos quando apropriado

### Permissões de Ferramentas

Quando o Crush quer executar ferramentas (como editar arquivos ou executar comandos), ele pedirá sua permissão:

```
Crush wants to use the edit tool:
• Edit src/utils.go

[a]llow  [d]eny  [v]iew  allow [A]ll
```

- Pressione `a` para permitir esta ação específica
- Pressione `A` para permitir todas as ferramentas para esta sessão
- Pressione `v` para ver as mudanças antes de decidir
- Pressione `d` para negar a ação

Você pode pular prompts de permissão inteiramente com a flag `--yolo`, mas use isso com extremo cuidado pois permite que o Crush faça mudanças sem confirmação.

### Skill de Configuração Integrado

> **Dica**: O Crush vem com um skill `crush-config` integrado para configurar a si mesmo. Em muitos casos, você pode simplesmente pedir ao Crush para configurar a si mesmo.

## Links Importantes

- **Repositório GitHub:** https://github.com/charmbracelet/crush
- **Documentação:** https://charmbracelet-crush.mintlify.app/
- **Site Oficial Charm:** https://charm.sh/
- **Discord:** https://charm.sh/discord
- **Slack:** https://charm.sh/slack
