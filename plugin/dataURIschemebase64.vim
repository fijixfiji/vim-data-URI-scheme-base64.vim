if exists("g:loaded_dataURIschemebase64")
  finish
endif
let g:loaded_dataURIschemebase64 = 1

let s:save_cpo = &cpo
set cpo&vim

command! -nargs=1 InputeDataURISchemeBase64 call dataURIschemebase64#input(<f-args>)

let &cpo = s:save_cpo
unlet s:save_cpo
