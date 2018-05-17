let s:save_cpo = &cpo
set cpo&vim

py3file <sfile>:h:h/src/p.py
python3 import vim
function! dataURIschemebase64#input(path)
  python3 dataURIschemebase64_input(vim.eval('a:path'))
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
