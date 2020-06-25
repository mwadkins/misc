(setq user-full-name "Michele Adkins")
(setq user-mail-address "madkins@qti.qualcomm.com")

;; add my .emacs.d and ~/local/share to load-path
(setq home-emacs-dir (concat (getenv "HOME") "/.emacs.d/"))
;;(setq local-emacs-dir (concat (getenv "HOME") "/local/share/emacs/site-lisp/"))
(setq my-load-path home-emacs-dir)
(setq load-path (append my-load-path load-path))


(setq custom-file "~/.emacs.d/custom.el")
(load custom-file)

;; in a text editor, everything is (at least) text
(setq default-major-mode 'text-mode)

;; font-lock setting
(global-font-lock-mode t)
(show-paren-mode t)
(transient-mark-mode t)


;;(set-face-background 'default "#333333") ;; .Xdefaults
;;(set-face-foreground 'default "#cccccc") ;; .Xdefaults
;;(set-face-background 'cursor "#ffaa00") ;; .Xdefaults
;;(set-face-foreground 'cursor "#333333") ;; .Xdefaults

(setq x-pointer-foreground-color "#aaaaaa") ;; .Xdefaults

(set-face-background 'region "#33aaff")
(set-face-foreground 'region "#eeeeee")
(set-face-foreground 'font-lock-warning-face "#dd0000")

(set-face-foreground 'font-lock-preprocessor-face "#99cc33")
(set-face-foreground 'font-lock-constant-face "#dd00dd")
(set-face-foreground 'font-lock-comment-face "#888888")
(set-face-foreground 'font-lock-keyword-face "#dddd00")
(set-face-foreground 'font-lock-type-face "#ffaa00")
(set-face-foreground 'font-lock-function-name-face "#2277dd")
(set-face-foreground 'font-lock-string-face "#33aaff")
(set-face-foreground 'font-lock-variable-name-face "#00bb00")
;;(global-hl-line-mode t)
;;(set-face-background 'hl-line "#3a3a3a")
;;(set-face-foreground 'hl-line "#eeeeee")

(set-face-foreground 'highlight "#333333")
(set-face-background 'highlight "#dddd00")
(set-face-foreground 'isearch "#333333")
(set-face-background 'isearch "#bbbb22")
(set-face-background 'modeline "#aaaaaa")
(set-face-foreground 'modeline "#333333")
(set-face-foreground 'link "#4466ff")
(set-face-foreground 'link-visited "#aa33bb")
(set-face-foreground 'minibuffer-prompt "#bababa")
(set-face-foreground 'escape-glyph "#ccaa11")

;; tab = two spaces
(setq default-tab-width 2)
(setq-default tab-width 2)
(setq-default indent-tabs-mode nil)
(setq css-indent-offset 2)
(setq-default sh-basic-offset 2)
(setq-default sh-indentation 2)
(setq-default perl-indent-level 2)
(setq-default js-indent-level 2)

;; set the random number seed from current time and pid
(random t)


;; make f9 the goto-line number key
(global-set-key (kbd "<f9>") 'goto-line)    

;; enable mouse support
(unless window-system
  (require 'mouse)
  (xterm-mouse-mode t)
  (global-set-key [mouse-4] '(lambda ()
                              (interactive)
                              (scroll-down 1)))
  (global-set-key [mouse-5] '(lambda ()
                              (interactive)
                              (scroll-up 1)))
  (defun track-mouse (e))
  (setq mouse-sel-mode t)
)
