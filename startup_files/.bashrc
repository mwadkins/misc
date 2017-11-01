# Hello emacs, this is -*- sh -*-
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

if [ -f ~/.bashrc.work ]
then
    # WORK
    . ~/.bashrc.work
else
    # HOME
    alias emacs='open -a /Applications/Emacs.app $1'

    # note: keyboard mapping for esc-p auto completion is in .inputrc
    
    # custom prompt
    PS1="[\d \t \u@\h:\w ] $ "
fi


# don't put duplicate lines in the history. See bash(1) for more options
export HISTCONTROL=ignoredups
export HISTSIZE=4095

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

#git grep, then blame on those files... if a file is passed to ggb, files are not shows in git blame.
ggb() { if [ ! -n "$2" ]; then
      	   showfile="-f";
	else
	   showfile="";
	fi;
	git grep -n "$@" | while IFS=: read i j k; do
	    git --no-pager blame $showfile -L $j,$j $i;
	done;
      }

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=always'
    alias fgrep='fgrep --color=always'
    alias egrep='egrep --color=always'
fi

# more aliases
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi

# set file mode creation mask (group write=1)
umask 2

# me first
export PATH=${HOME}/bin:${PATH}


