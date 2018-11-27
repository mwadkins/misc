# Hello emacs, this is -*- sh -*-
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

export HOSTNAME=`hostname`

export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

if [ -f ~/.bashrc.work ]
then
    # WORK
    . ~/.bashrc.work
    PS1='\h:$(__git_ps1 " (%s)")>' 
	
else
    # HOME
    alias emacs='open -a /Applications/Emacs.app $1'

    # note: keyboard mapping for esc-p auto completion goes in .inputrc
    #"\ep": history-search-backward
    #"\en": history-search-forward
 
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

# helper functions
if [ "${BASH_DEBUG}" == "true" ] ; then  echo "load func files" 1>&2; fi
for file in ~/func/*.func
do
  . $file
  if [ "${BASH_DEBUG}" == "true" ] ; then  echo "load ${file}" 1>&2; fi
done

# set file mode creation mask (group write=1)
umask 2

# me first
export PATH=${HOME}/bin:${PATH}

if [ "$HOSTNAME" == "madkins-ubuntu" ]; then
   alias emacs='/usr/bin/emacs'
fi


### BEGIN GIT2CC ###
if [ -f /prj/qct/coredev/hexagon/sitelinks/arch/scripts/git2cc_user.new/bashrc ] ; then
  source /prj/qct/coredev/hexagon/sitelinks/arch/scripts/git2cc_user.new/bashrc
fi
### END GIT2CC ###
