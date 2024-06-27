#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `zsh` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos para configurar/instalar/usar o `zsh` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands for configuring/installing/use `zsh` on `Linux Ubuntu`._

# ## Revisão(ões)/Versão(ões)
# 
# | Revisão número | Data da revisão | Descrição da revisão                                    | Autor da revisão                                |
# |:--------------:|:---------------:|:--------------------------------------------------------|:------------------------------------------------|
# | 0              | 07/12/2023      | <ul><li>Revisão inicial/criação do documento.</li></ul> | <ul><li>Eden Denis F. da S. L. Santos</ul></li> |
# 

# ## Controle de configuração/instalação nos Sistemas Operacionais (SO) vs. Computador
# 
# | Número | Computador          | Sistema Operacional (SO) | Status da configuração/instalação |
# |:------:|:-------------------:|:------------------------:|:---------------------------------:|
# | 1      | Dell Precision 7520 |Kali Linux                | N/A                               |
# | 2      | Dell Precision 7520 |Linux Ubuntu              | N/A                               |
# | 3      | Dell Precision 7520 |Linux Xubuntu             | OK                                |
# | 4      | Dell Precision 7520 |Windows                   | Pendente                          |
# | 5      | Asus                |Kali Linux                | N/A                               |
# | 6      | Asus                |Linux Ubuntu              | Pendente                          |
# | 7      | Asus                |Linux Xubuntu             | OK                                |
# | 8      | Asus                |Windows                   | Pendente                          |
#  
# ### Legenda
# 
# - **N/A:** Not applicable
# - **OK:** Zero killed

# ## Descrição [2]
# 
# ### `shell`
# 
# Um shell é uma interface de linha de comando que permite aos usuários interagirem com um sistema operacional por meio de comandos de texto. Ele interpreta os comandos inseridos pelo usuário e os executa, facilitando a manipulação de arquivos, a execução de programas e outras tarefas do sistema. Além disso, os shells também oferecem recursos avançados, como redirecionamento de entrada e saída, expansão de comandos e controle de processos. Exemplos comuns incluem o Bash, o Zsh e o PowerShell.
# 
# ### `bash`
# 
# Bash, ou Bourne Again Shell, é um shell de linha de comando amplamente utilizado em sistemas operacionais Unix e Linux. Ele oferece uma variedade de recursos, como expansão de comandos, redirecionamento de entrada/saída, scripts de shell e controle de processos. O Bash é altamente personalizável e suporta automação de tarefas por meio de scripts, tornando-o uma ferramenta poderosa para usuários avançados e administradores de sistemas. Sua sintaxe simples e intuitiva o torna acessível para iniciantes, enquanto sua flexibilidade e extensibilidade o tornam uma escolha popular entre profissionais de TI.
# 
# ### `zsh`
# 
# O `zsh`, ou Z Shell, é um interpretador de `shell` de código aberto e uma alternativa avançada ao bash (Bourne Again Shell), que é comumente usado em sistemas Unix e Linux. O `zsh` oferece uma série de recursos avançados, como autocompletamento poderoso, histórico de comandos expandido, personalização flexível da aparência e do comportamento do `shell`, além de suporte a plugins e temas. Sua interface de linha de comando aprimorada e recursos de automação tornam-no uma escolha popular entre desenvolvedores, administradores de sistema e entusiastas de terminal que desejam uma experiência de linha de comando mais produtiva e personalizável. O `zsh` é altamente configurável e pode ser estendido por meio de plugins, tornando-o uma ferramenta versátil para trabalhar com eficiência no ambiente Unix e Linux.
# 
# 

# ## 1. Como configurar/instalar/usar o `zsh` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `zsh` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para configurar/instalar/usar o `zsh` em um sistema `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Primeiro, instale o `zsh` com o comando: `sudo apt install zsh -y`    

# ### 1.1 Mudar o tema do `zsh` 
# 
# 1. **Mudar o tema:** Dentro do arquivo `~/.zshrc`, substitua o código atual pelo código abaixo:
# 
#     1.1 **Para (novo código):** Existe o código (novo) abaixo e também um arquivo chamado `.zshrc` ou `.zshrc_linux_ubuntu` (pressionar `Ctrl + H` dentro da pasta, pois são arquivos ocultos) que precisará ser renomeado para `.zshrc` e substituído na pasta `~/`:
# 
#     ```
#     # Created by newuser for 5.8.1
#     # ~/.zshrc file for zsh interactive shells.
#     # see /usr/$USER/doc/zsh/examples/zshrc for examples
# 
#     setopt autocd              # change directory just by typing its name
#     #setopt correct            # auto correct mistakes
#     setopt interactivecomments # allow comments in interactive mode
#     setopt magicequalsubst     # enable filename expansion for arguments of the form ‘anything=expression’
#     setopt nonomatch           # hide error message if there is no match for the pattern
#     setopt notify              # report the status of background jobs immediately
#     setopt numericglobsort     # sort filenames numerically when it makes sense
#     setopt promptsubst         # enable command substitution in prompt
# 
#     WORDCHARS=${WORDCHARS//\/} # Don't consider certain characters part of the word
# 
#     # hide EOL sign ('%')
#     PROMPT_EOL_MARK=""
# 
#     # configure key keybindings
#     bindkey -e                                        # emacs key bindings
#     bindkey ' ' magic-space                           # do history expansion on space
#     bindkey '^U' backward-kill-line                   # ctrl + U
#     bindkey '^[[3;5~' kill-word                       # ctrl + Supr
#     bindkey '^[[3~' delete-char                       # delete
#     bindkey '^[[1;5C' forward-word                    # ctrl + ->
#     bindkey '^[[1;5D' backward-word                   # ctrl + <-
#     bindkey '^[[5~' beginning-of-buffer-or-history    # page up
#     bindkey '^[[6~' end-of-buffer-or-history          # page down
#     bindkey '^[[H' beginning-of-line                  # home
#     bindkey '^[[F' end-of-line                        # end
#     bindkey '^[[Z' undo                               # shift + tab undo last action
# 
#     # enable completion features
#     autoload -Uz compinit
#     compinit -d ~/.cache/zcompdump
#     zstyle ':completion:*:*:*:*:*' menu select
#     zstyle ':completion:*' auto-description 'specify: %d'
#     zstyle ':completion:*' completer _expand _complete
#     zstyle ':completion:*' format 'Completing %d'
#     zstyle ':completion:*' group-name ''
#     zstyle ':completion:*' list-colors ''
#     zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
#     zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
#     zstyle ':completion:*' rehash true
#     zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
#     zstyle ':completion:*' use-compctl false
#     zstyle ':completion:*' verbose true
#     zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'
# 
#     # History configurations
#     HISTFILE=~/.zsh_history
#     HISTSIZE=1000
#     SAVEHIST=2000
#     setopt hist_expire_dups_first # delete duplicates first when HISTFILE size exceeds HISTSIZE
#     setopt hist_ignore_dups       # ignore duplicated commands history list
#     setopt hist_ignore_space      # ignore commands that start with space
#     setopt hist_verify            # show command with history expansion to user before running it
#     #setopt edenedfsls_history         # $USER command history data
# 
#     # force zsh to show the complete history
#     alias history="history 0"
# 
#     # configure `time` format
#     TIMEFMT=$'\nreal\t%E\nuser\t%U\nsys\t%S\ncpu\t%P'
# 
#     # make less more friendly for non-text input files, see lesspipe(1)
#     #[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
# 
#     # set variable identifying the chroot you work in (used in the prompt below)
#     if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
#         debian_chroot=$(cat /etc/debian_chroot)
#     fi
# 
#     # set a fancy prompt (non-color, unless we know we "want" color)
#     case "$TERM" in
#         xterm-color|*-256color) color_prompt=yes;;
#     esac
# 
#     # uncomment for a colored prompt, if the terminal has the capability; turned
#     # off by default to not distract the user: the focus in a terminal window
#     # should be on the output of commands, not on the prompt
#     force_color_prompt=yes
# 
#     if [ -n "$force_color_prompt" ]; then
#         if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
#             # We have color support; assume it's compliant with Ecma-48
#             # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
#             # a case would tend to support setf rather than setaf.)
#             color_prompt=yes
#         else
#             color_prompt=
#         fi
#     fi
# 
#     configure_prompt() {
#         prompt_symbol=@
#         # Skull emoji for root terminal
#         #[ "$EUID" -eq 0 ] && prompt_symbol=💀
#         case "$PROMPT_ALTERNATIVE" in
#             twoline)
#                 PROMPT=$'%F{%(#.blue.green)}┌──${debian_chroot:+($debian_chroot)─}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))─}(%B%F{%(#.red.blue)}%n'$prompt_symbol$'%m%b%F{%(#.blue.green)})-[%B%F{reset}%1~%b%F{%(#.blue.green)}]\n└─%B%(#.%F{red}#.%F{blue}$)%b%F{reset} '
#                 # Right-side prompt with exit codes and background processes
#                 #RPROMPT=$'%(?.. %? %F{red}%B⨯%b%F{reset})%(1j. %j %F{yellow}%B⚙%b%F{reset}.)'
#                 ;;
#             oneline)
#                 PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{%(#.red.blue)}%n@%m%b%F{reset}:%B%F{%(#.blue.green)}%1~%b%F{reset}%(#.#.$) '
#                 RPROMPT=
#                 ;;
#             backtrack)
#                 PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{red}%n@%m%b%F{reset}:%B%F{blue}%1~%b%F{reset}%(#.#.$) '
#                 RPROMPT=
#                 ;;
#         esac
#         unset prompt_symbol
#     }
# 
#     # The following block is surrounded by two delimiters.
#     # These delimiters must not be modified. Thanks.
#     # START KALI CONFIG VARIABLES
#     PROMPT_ALTERNATIVE=twoline
#     NEWLINE_BEFORE_PROMPT=yes
#     # STOP KALI CONFIG VARIABLES
# 
#     if [ "$color_prompt" = yes ]; then
#         # override default virtualenv indicator in prompt
#         VIRTUAL_ENV_DISABLE_PROMPT=1
# 
#         configure_prompt
# 
#         # enable syntax-highlighting
#         if [ -f /usr/$USER/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
#             . /usr/$USER/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
#             ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)
#             ZSH_HIGHLIGHT_STYLES[default]=none
#             ZSH_HIGHLIGHT_STYLES[unknown-token]=underline
#             ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=cyan,bold
#             ZSH_HIGHLIGHT_STYLES[suffix-alias]=fg=green,underline
#             ZSH_HIGHLIGHT_STYLES[global-alias]=fg=green,bold
#             ZSH_HIGHLIGHT_STYLES[precommand]=fg=green,underline
#             ZSH_HIGHLIGHT_STYLES[commandseparator]=fg=blue,bold
#             ZSH_HIGHLIGHT_STYLES[autodirectory]=fg=green,underline
#             ZSH_HIGHLIGHT_STYLES[path]=bold
#             ZSH_HIGHLIGHT_STYLES[path_pathseparator]=
#             ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]=
#             ZSH_HIGHLIGHT_STYLES[globbing]=fg=blue,bold
#             ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=blue,bold
#             ZSH_HIGHLIGHT_STYLES[command-substitution]=none
#             ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]=fg=magenta,bold
#             ZSH_HIGHLIGHT_STYLES[process-substitution]=none
#             ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]=fg=magenta,bold
#             ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=fg=green
#             ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=fg=green
#             ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
#             ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]=fg=blue,bold
#             ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=yellow
#             ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=yellow
#             ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]=fg=yellow
#             ZSH_HIGHLIGHT_STYLES[rc-quote]=fg=magenta
#             ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=magenta,bold
#             ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=magenta,bold
#             ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]=fg=magenta,bold
#             ZSH_HIGHLIGHT_STYLES[assign]=none
#             ZSH_HIGHLIGHT_STYLES[redirection]=fg=blue,bold
#             ZSH_HIGHLIGHT_STYLES[comment]=fg=black,bold
#             ZSH_HIGHLIGHT_STYLES[named-fd]=none
#             ZSH_HIGHLIGHT_STYLES[numeric-fd]=none
#             ZSH_HIGHLIGHT_STYLES[arg0]=fg=cyan
#             ZSH_HIGHLIGHT_STYLES[bracket-error]=fg=red,bold
#             ZSH_HIGHLIGHT_STYLES[bracket-level-1]=fg=blue,bold
#             ZSH_HIGHLIGHT_STYLES[bracket-level-2]=fg=green,bold
#             ZSH_HIGHLIGHT_STYLES[bracket-level-3]=fg=magenta,bold
#             ZSH_HIGHLIGHT_STYLES[bracket-level-4]=fg=yellow,bold
#             ZSH_HIGHLIGHT_STYLES[bracket-level-5]=fg=cyan,bold
#             ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]=standout
#         fi
#     else
#         PROMPT='${debian_chroot:+($debian_chroot)}%n@%m:%~%(#.#.$) '
#     fi
#     unset color_prompt force_color_prompt
# 
#     toggle_oneline_prompt(){
#         if [ "$PROMPT_ALTERNATIVE" = oneline ]; then
#             PROMPT_ALTERNATIVE=twoline
#         else
#             PROMPT_ALTERNATIVE=oneline
#         fi
#         configure_prompt
#         zle reset-prompt
#     }
#     zle -N toggle_oneline_prompt
#     bindkey ^P toggle_oneline_prompt
# 
#     # If this is an xterm set the title to user@host:dir
#     case "$TERM" in
#     xterm*|rxvt*|Eterm|aterm|kterm|gnome*|alacritty)
#         TERM_TITLE=$'\e]0;${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%n@%m: %~\a'
#         ;;
#     *)
#         ;;
#     esac
# 
#     precmd() {
#         # Print the previously configured title
#         print -Pnr -- "$TERM_TITLE"
# 
#         # Print a new line before the prompt, but only if it is not the first line
#         if [ "$NEWLINE_BEFORE_PROMPT" = yes ]; then
#             if [ -z "$_NEW_LINE_BEFORE_PROMPT" ]; then
#                 _NEW_LINE_BEFORE_PROMPT=1
#             else
#                 print ""
#             fi
#         fi
#     }
# 
#     # enable color support of ls, less and man, and also add handy aliases
#     if [ -x /usr/bin/dircolors ]; then
#         test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
#         export LS_COLORS="$LS_COLORS:ow=30;44:" # fix ls color for folders with 777 permissions
# 
#         alias ls='ls --color=auto'
#         #alias dir='dir --color=auto'
#         #alias vdir='vdir --color=auto'
# 
#         alias grep='grep --color=auto'
#         alias fgrep='fgrep --color=auto'
#         alias egrep='egrep --color=auto'
#         alias diff='diff --color=auto'
#         alias ip='ip --color=auto'
# 
#         export LESS_TERMCAP_mb=$'\E[1;31m'     # begin blink
#         export LESS_TERMCAP_md=$'\E[1;36m'     # begin bold
#         export LESS_TERMCAP_me=$'\E[0m'        # reset bold/blink
#         export LESS_TERMCAP_so=$'\E[01;33m'    # begin reverse video
#         export LESS_TERMCAP_se=$'\E[0m'        # reset reverse video
#         export LESS_TERMCAP_us=$'\E[1;32m'     # begin underline
#         export LESS_TERMCAP_ue=$'\E[0m'        # reset underline
# 
#         # Take advantage of $LS_COLORS for completion as well
#         zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
#         zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
#     fi
# 
#     # some more ls aliases
#     alias ll='ls -l'
#     alias la='ls -A'
#     alias l='ls -CF'
# 
#     # enable auto-suggestions based on the history
#     if [ -f /usr/$USER/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
#         . /usr/$USER/zsh-autosuggestions/zsh-autosuggestions.zsh
#         # change suggestion color
#         ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=10'
#     fi
# 
#     # enable command-not-found if installed
#     if [ -f /etc/zsh_command_not_found ]; then
#         . /etc/zsh_command_not_found
#     fi
# 
#     # >>> conda initialize >>>
#     # !! Contents within this block are managed by 'conda init' !!
#     __conda_setup="$('/home/$USER/anaconda3/bin/conda' '`shell`.zsh' 'hook' 2> /dev/null)"
#     if [ $? -eq 0 ]; then
#         eval "$__conda_setup"
#     else
#         if [ -f "/home/$USER/anaconda3/etc/profile.d/conda.sh" ]; then
#             . "/home/$USER/anaconda3/etc/profile.d/conda.sh"
#         else
#             export PATH="/home/$USER/anaconda3/bin:$PATH"
#         fi
#     fi
#     unset __conda_setup
#     # <<< conda initialize <<<
#     conda activate base
# 
#     plugins=(git sudo zsh-autosuggestions)
#     source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
#     ```
# 
#     **ATENÇÃO:** Perceber que, o `conda initialize` está inserido no código. Sendo assim, inicialmente deve ser instalado o `anaconda` e talvez o nome do usuário, neste caso `$USER` tenha que ser alterado.
# 

# ### 1.1 Configurar o `zsh` como seu `shell` padrão
# 
# 1. **Configurar o `zsh` como seu `shell` Padrão:** Para configurar o `zsh` como seu ``shell`` padrão, use (NÃO colocar o `sudo`!): `chsh -s $(which zsh)`
# 
#     - Você precisará fazer logout e login novamente para que a mudança tenha efeito.
# 
# 2. **Criar o Arquivo .`zshrc`:** Se, por algum motivo, o arquivo `.zshrc` não for criado automaticamente, você pode criá-lo manualmente: `sudo nano ~/.zshrc`
# 
#     - Adicione as configurações que deseja e salve o arquivo.
# 
# 3. **Aplicar as alterações:** Para que as mudanças tenham efeito, você precisa recarregar o arquivo de configuração. Isso pode ser feito com o comando: `source ~/.zshrc`
# 
#     Ou simplesmente feche e reabra o terminal.
# 
# Esses passos devem ajudar a configurar o `zsh` com o tema e os plugins desejados. Se tiver dificuldades com algum plugin específico, pode ser útil consultar a documentação do Oh My `zsh` ou procurar ajuda específica para aquele plugin.
# 

# #### 1.1.1 Ajustar as cores do `Terminal Emulator`
# 
# 1. No `Terminal Emulator`, na barra de ferramentas, clicar em: `Edit`
# 
# 2. Clique em: `Preferênces`
# 
# 3. Clique na aba `Appearence`
# 
#     3.1 Em `Background` altere a opção para `Transparent background`
# 
#     3.2 Em `Opacity` coloque em `0,85`
# 
# 4. Clique na aba `Colors`
# 
#     4.1 Em `Presets` selecione `Tango`
# 
# 5. Em `General`, em `Text color:` selecione a cor `Dourada` para que fique visível.
# 

# ### 1.2 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `zsh` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update -y
#     sudo apt autoremove -y
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install zsh -y
#     ```
# 

# ## 2. Habilitar o `autosuggestions` (auto-sugestões ou auto-completar) no `zsh`
# 
# O recurso que você está descrevendo é conhecido como `autosuggestions` (auto-sugestões ou auto-completar), que exibe comandos anteriores que você digitou que começam com o que você está digitando atualmente. No `zsh`, isso geralmente é realizado pelo plugin `zsh-autosuggestions`, você pode instalar o plugin manualmente.
# 
# Aqui estão as etapas para instalar o plugin `zsh-autosuggestions` sem usar o Oh My `zsh`:
# 
# 1. **Clone o Repositório do Plugin:** Abra um terminal e execute o seguinte comando para clonar o plugin para o diretório de plugins do `zsh`: `git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions`
# 
# 2. **Adicione o Plugin ao Seu Arquivo `.zshrc`:** Você precisará adicionar uma linha ao seu arquivo `.zshrc` para carregar o plugin. Abra o arquivo `.zshrc` com um editor de texto: `sudo nano ~/.zshrc`
# 
# 3. **E adicione a seguinte linha no final do arquivo:**
# 
#     ```
#     plugins=(git sudo zsh-autosuggestions)
#     source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
#     ``````
# 
# 4. **Configure as Cores das Sugestões (opcional):** Se você quiser personalizar a cor das sugestões para que sejam mais claras ou correspondam ao seu esquema de cores do terminal, adicione o seguinte ao seu `.zshrc`: `ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=10'`
# 
#     Ajuste o valor `'fg=10'` (compatível com o esquema de cores `Tango`) para a cor desejada conforme as configurações do seu terminal.
# 
# 5. **Recarregue o Seu Arquivo `.zshrc`:** Depois de salvar suas alterações, você pode recarregar o arquivo de configuração com: `source ~/.zshrc`
# 
# 6. **Verifique se Está Funcionando:** Após recarregar o arquivo `.zshrc`, comece a digitar um comando que você usou anteriormente. As sugestões devem aparecer automaticamente.
# 
# Após realizar esses passos, quando você começar a digitar um comando no terminal, o plugin `zsh-autosuggestions` mostrará sugestões com base nos seus comandos anteriores, com a sugestão exibida em uma cor mais clara. Você pode aceitar a sugestão pressionando a tecla de seta para a direita.
# 
# Espero que isso ajude a configurar as auto-sugestões no seu terminal `zsh`. Se você encontrar algum problema, certifique-se de que o caminho para o script `zsh-autosuggestions`.zsh está correto e que o plugin foi clonado para o local correto.
# 
# Se você estiver usando o `bash` e quiser um recurso similar, você precisaria de uma configuração diferente, já que o `zsh-autosuggestions` é específico para o `zsh`. No `bash`, o recurso mais próximo é o `history search`, que pode ser habilitado com algumas configurações no arquivo `.bashrc`.
# 

# ## 3. Alterar o símbolo que aparece entre o nome de usuário e o `host`
# 
# Para alterar o símbolo que aparece entre o seu nome de usuário e o nome do `host` no seu prompt do `zsh`, você precisará modificar a variável `PROMPT` (ou `PS1` em alguns casos) no seu arquivo `.zshrc`.
# 
# 1. **Abra o arquivo `.zshrc` no editor de texto:** `sudo nano ~/.zshrc`
# 
# 2. Localize a parte do arquivo onde a variável `PROMPT` é definida. Você mencionou que quer mudar o símbolo de `㉿` para `@`. Você deve procurar por uma linha que tenha algo similar a isto:
# 
#     ```
#     configure_prompt() {
#     prompt_symbol=@ # ESTA É A LINHA QUE DEVE SER ALTERADA
#     # Skull emoji for root terminal
#     #[ "$EUID" -eq 0 ] && prompt_symbol=💀
#     case "$PROMPT_ALTERNATIVE" in
#         twoline)
#             PROMPT=$'%F{%(#.blue.green)}┌──${debian_chroot:+($debian_chroot)─}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))─}(%B%F{%(#.red.blue)}%n'$prompt_symbol$'%m%b%F{%(#.blue.green)})-[%B%F{reset}%(6~.%-1~/…/%4~.%5~)%b%F{%(#.blue.green)}]\n└─%B%(#.%F{red}#.%F{blue}$)%b%F{reset} '
#             # Right-side prompt with exit codes and background processes
#             #RPROMPT=$'%(?.. %? %F{red}%B⨯%b%F{reset})%(1j. %j %F{yellow}%B⚙%b%F{reset}.)'
#             ;;
#         oneline)
#             PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{%(#.red.blue)}%n@%m%b%F{reset}:%B%F{%(#.blue.green)}%~%b%F{reset}%(#.#.$) '
#             RPROMPT=
#             ;;
#         backtrack)
#             PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{red}%n@%m%b%F{reset}:%B%F{blue}%~%b%F{reset}%(#.#.$) '
#             RPROMPT=
#             ;;
#     esac
#     unset prompt_symbol
#     }
#     ```
# 
# 3. **Altere o `㉿` para `@` assim:** `prompt_symbol=@`
# 
# 4. Salve o arquivo e saia do editor (em `nano`, você faz isso com `Ctrl+X`, confirma as mudanças com `Y` e depois pressiona `Enter`).
# 
# 5. Depois de salvar o arquivo, você pode aplicar as alterações imediatamente com: `source ~/.zshrc`
# 
#     Ou simplesmente fechar e reabrir o terminal.
# 

# ## 5. Mudar o seu `shell` de volta para o `bash` (ou outro `shell` de sua preferência) com o comando:
# 
# 1. Finalmente, mude o seu `shell` de volta para o `bash` (ou outro `shell` de sua preferência) com o comando: `sudo chsh -s /bin/bash`
# 
#     Você precisará fechar a sessão e logar novamente para que a alteração tenha efeito.
# 
# 2. **Iniciar o `bash` Manualmente:** Caso NÃO funcione, como solução temporária, você pode iniciar o `bash` manualmente em um terminal do `zsh`, simplesmente digitando bash. Isso não muda seu `shell` padrão, mas inicia uma sessão do `bash` naquele terminal específico.
# 

# ## 6. Alterar a opacidade/transparência do `Terminal Emulator`
# 
# A referência específica à transparência padrão do terminal no `Kali Linux` não é mencionada diretamente nas fontes. No entanto, uma prática comum é definir a transparência do painel do terminal para cerca de `5%`, para dar uma aparência estilizada, como mencionado em um guia de personalização do ambiente de desktop `xfce` no `Kali Linux​​`. Isso indica que a transparência padrão pode ser definida para um valor baixo ou até mesmo desativada por padrão, com a opção de ajuste conforme a preferência do usuário.
# 
# No entanto, se você deseja ajustar ou verificar a transparência do seu terminal no Kali Linux, você geralmente pode fazer isso através das preferências do próprio terminal. Por exemplo, no GNOME Terminal, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`.
# 
# 2. Clique com o botão direito dentro do terminal e selecione `“Preferences”` ou `“Profile Preferences”`.
# 
# 3. Na aba `“Appearance”`, você encontrará um controle deslizante para ajustar a opacidade/transparência do fundo do terminal.
# 
# É importante observar que essas configurações podem variar dependendo do emulador de terminal que você está usando. Além disso, a capacidade de ajustar a transparência pode depender de outros fatores do sistema, como os efeitos gráficos habilitados no seu ambiente de desktop.

# 7. Desinstalar o `shell` `zsh`
# 
# Para desinstalar o zsh e limpar as configurações no Ubuntu pelo terminal, você pode seguir estes passos:
# 
# 1. **Desinstalar o `zsh`:** `sudo apt remove --purge zsh`
# 
# 2. **Remover as configurações pessoais:** Apague o diretório de configuração do `zsh` no seu diretório `home`: `rm -rf ~/.zsh ~/.zshrc`
# 
# 3. **Mudar o `shell` padrão de volta para o `bash`: Para voltar para o `bash` como seu `shell` padrão, execute: `chsh -s /bin/bash`
# 
# Lembre-se de que você precisará fechar e reabrir o terminal ou reiniciar a sessão para que as alterações entrem em vigor. Isso removerá o zsh e suas configurações do seu sistema.
# 

# ## 7. Desinstalar o `zsh`
# 
# Para desinstalar completamente o `zsh` no `Linux Ubuntu`, você precisa seguir algumas etapas. Primeiro, é importante remover o pacote `zsh` em si e, em seguida, alterar o `shell` padrão para o usuário de volta ao `shell` anterior (geralmente `bash`), caso o `zsh` tenha sido configurado como o `shell` padrão. Aqui estão as etapas detalhadas:
# 
# 1. **Abra o terminal:** Você pode fazer isso pressionando no Ubuntu: `Ctrl + Alt + T`
# 
# 2. Verifique se o `zsh` é o `shell` atual: Antes de desinstalar o `zsh`, é uma boa ideia verificar se ele está configurado como o `shell` padrão para o seu usuário. Execute: `echo $SHELL`
# 
# 3. Se o resultado for algo como `/usr/bin/zsh` ou similar, significa que `zsh` é o seu `shell` atual.
# 
# 4. Troque o `shell` padrão para bash (ou outro `shell` de sua preferência): Se `zsh` é o seu `shell` atual, você precisa mudá-lo antes de desinstalar o `zsh`. Para mudar para `bash`, por exemplo, use: `chsh -s /bin/bash
# `
# 5. Você precisará sair e entrar novamente na sua sessão para que a alteração tenha efeito.
# 
# 6. **Desinstale o `zsh`:** Agora, para desinstalar o `zsh`, use o comando `apt` com privilégios de administrador: `sudo apt remove --purge zsh`
# 
# 7. Este comando remove o `zsh` e qualquer configuração personalizada que você possa ter feito.
# 
# 8. **Limpe os pacotes não mais necessários:** Após a desinstalação, é uma boa prática remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários: `sudo apt autoremove`
# 
# 9. **Opcional - Remova manualmente qualquer arquivo de configuração residuais:** Se você quiser garantir que todas as configurações personalizadas do zsh sejam removidas, pode precisar excluí-las manualmente. Arquivos de configuração do zsh geralmente estão localizados em seu diretório home, como .zshrc. Para removê-los, use: `rm ~/.zshrc`
# 
#     E qualquer outro arquivo de configuração do zsh que você possa ter criado ou modificado.
# 
# Lembre-se de que esses comandos podem variar ligeiramente dependendo da sua configuração específica e da versão do Ubuntu. Certifique-se de ter backups de quaisquer dados ou configurações importantes antes de proceder com a desinstalação.

# ## Referências
# 
# [1] OPENAI. ***Configurando terminal no ubuntu.*** Disponível em: <https://chat.openai.com/c/1ecf460a-8fee-4048-9a29-baae6a494efd> (texto adaptado). ChatGPT. Acessado em: 07/12/2023 09:07.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 29/11/2023 09:07.
# 
# [3] OPENAI. ***Comandos de manutenção do ubuntu.*** Disponível em: <https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830>. ChatGPT. Acessado em: 15/12/2023 08:25.
# 
