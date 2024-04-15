py3file <sfile>:h:h/python3/wolbrw.py
python3 import vim

" 一覧作成用のバッファ名
let g:wolbrw_list_buffer = "WOLBRW_LIST"
let g:wolbrw_list_buffer_bible = "WOLBRW_CNT"
let g:wolbrw_list_buffer_right = "WOLBRW_CNT2"

" 履歴を保持するリスト
let g:wolbrw_history = []
let g:wolbrw_unhistory = []

" 履歴にアイテムを追加する関数
function! wolbrw#AddToHistory(item)
    " リストの長さが20を超えた場合、古いアイテムを削除
    if len(g:wolbrw_history) >= 20
        call remove(g:wolbrw_history, 0)
    endif
    " 新しいアイテムをリストの末尾に追加
    call add(g:wolbrw_history, a:item)
endfunction


" 履歴（元に戻す）にアイテムを追加する関数
function! wolbrw#AddToUnHistory(item)
    " リストの長さが20を超えた場合、古いアイテムを削除
    if len(g:wolbrw_unhistory) >= 20
        call remove(g:wolbrw_unhistory, 0)
    endif
    " 新しいアイテムをリストの末尾に追加
    call add(g:wolbrw_unhistory, a:item)
endfunction

" 履歴を表示する関数
function! wolbrw#ShowHistory()
    echo join(g:wolbrw_history, "\n")
endfunction

function! wolbrw#make_windows_History() abort
    let g:wolbrw_current_window_id = win_getid()
    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer, 'unlock')

    if len(g:wolbrw_history) > 1
      let last_item = g:wolbrw_history[-1]
      call wolbrw#make_windows(last_item)
      call wolbrw#AddToUnHistory(last_item)
      call remove(g:wolbrw_history, len(g:wolbrw_history) - 1)
    elseif len(g:wolbrw_history) == 1
      let last_item = g:wolbrw_history[-1]
      call wolbrw#make_windows(last_item)
      call wolbrw#AddToUnHistory(last_item)
    else
        echo "履歴は空です。"
        return
    endif
endfunction

function! wolbrw#make_windows_UnHistory() abort
    let g:wolbrw_current_window_id = win_getid()
    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer, 'unlock')

    if len(g:wolbrw_unhistory) > 1
      let last_item = g:wolbrw_unhistory[-1]
      call wolbrw#make_windows(last_item)
      call wolbrw#AddToHistory(last_item)
      call remove(g:wolbrw_unhistory, len(g:wolbrw_unhistory) - 1)
    elseif len(g:wolbrw_unhistory) == 1
      let last_item = g:wolbrw_unhistory[-1]
      call wolbrw#make_windows(last_item)
      call wolbrw#AddToUnHistory(last_item)
    else
        echo "もとに戻すは空です"
        return
    endif
endfunction

function! wolbrw#ParseFlags(arg_list, arg_mord) abort
  let text = []
  let scope = 'par'
  let order = 'occ'
  let flag = ''

  for arg in a:arg_list
    if arg == '-q'
      let flag = 'text'
    elseif arg == '-s'
      let flag = 'scope'
    elseif arg == '-o'
      let flag = 'order'
    elseif flag == 'text'
      call add(text, arg)
    elseif flag == 'scope'
      if arg =~ '^\(sen\|par\|doc\)$'
        let scope = arg
      endif
      let flag = ''
    elseif flag == 'order'
      if arg =~ '^\(occ\|newest\|oldest\)$'
        let order = arg
      endif
      let flag = ''
    elseif flag == ''
      call add(text, arg)
    endif
  endfor

  if a:arg_mord == 'search_simple'
    return {'text': join(text, '&'), 'scope': scope, 'order': order}
  elseif a:arg_mord == 'search_mean'
    let text = wolbrw#getSelectedText()
    return {'text': text, 'scope': scope, 'order': order}
  endif
endfunction

function! wolbrw#make_windows_from_command(...) abort
  let g:wolbrw_current_window_id = win_getid()
  let flags = wolbrw#ParseFlags(a:000, 'search_simple')
    echo flags

    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer, 'unlock')
    " 現在のウィンドウIDの取得
    python3 text = vim.eval("flags['text']")
    python3 scope = vim.eval("flags['scope']")
    python3 order = vim.eval("flags['order']")
    python3 vim.command(f'let s:result = {wolbrw_search(text=text,scope=scope,order=order)}')
    call wolbrw#make_windows(s:result)
    call wolbrw#AddToHistory(s:result)
endfunction

function! wolbrw#make_windows_mean_search(...) abort
  let g:wolbrw_current_window_id = win_getid()
  let flags = wolbrw#ParseFlags(a:000, 'search_mean')
    echo flags

    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer, 'unlock')
    " 現在のウィンドウIDの取得
    python3 text = vim.eval("flags['text']")
    python3 scope = vim.eval("flags['scope']")
    python3 order = vim.eval("flags['order']")
    python3 vim.command(f'let s:result = {wolbrw_mean_search(text=text,scope=scope,order=order)}')
    call wolbrw#make_windows(s:result)
    call wolbrw#AddToHistory(s:result)
endfunction

function! wolbrw#make_windows(result) abort
    let g:wolbrw_result_list = a:result[0]
    let g:wolbrw_result_dict = a:result[1]
    if g:wolbrw_result_dict == {}
      echo 'おそらくまだスタディノートが公開されていません'
      if bufexists(g:wolbrw_list_buffer)
        " バッファがウィンドウに表示されている場合は`win_gotoid`でウィンドウに移動します
        let winid = bufwinid(g:wolbrw_list_buffer)
        if winid isnot# -1
          call win_gotoid(winid)
          %delete _
        endif
      endif
      return
    endif

    " 'NEO4JLISTS' バッファが存在している場合
    if bufexists(g:wolbrw_list_buffer)
      " バッファがウィンドウに表示されている場合は`win_gotoid`でウィンドウに移動します
      let winid = bufwinid(g:wolbrw_list_buffer)
      if winid isnot# -1
        call win_gotoid(winid)
  
      " バッファがウィンドウに表示されていない場合は`sbuffer`で新しいウィンドウを作成してバッファを開きます
      else
        execute 'sbuffer' g:wolbrw_list_buffer
      endif
  
    else
      " バッファが存在していない場合は`new`で新しいバッファを作成します
      execute 'new' g:wolbrw_list_buffer_right
      execute 'vnew' g:wolbrw_list_buffer
      execute "normal \<C-W>l"
      "execute 'new' g:wolbrw_list_buffer_bible
      execute "normal \<C-W>h"
  
      " キーマッピングを定義します
      call wolbrw#set_keymap(g:wolbrw_list_buffer)
  
    endif
  
    " セッションファイルを表示する一時バッファのテキストをすべて削除して、取得したファイル一覧をバッファに挿入します
    %delete _
    " キーのみを抽出
    let g:wolbrw_result_keys = map(copy(g:wolbrw_result_list), 'v:val[0]')
    call setline(1, g:wolbrw_result_keys)
    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer, 'lock')
    call wolbrw#infowindow(g:wolbrw_result_dict[getline('.')])
endfunction




function! wolbrw#set_keymap(bufname) abort
    let current_window_id = win_getid()
    let targetwindow_id = bufwinid(a:bufname)
    if targetwindow_id != -1
      call win_gotoid(targetwindow_id)
        " 1. セッション一覧のバッファで`q`を押下するとバッファを破棄
        " 2. `Enter`でセッションをロード
        " の2つのキーマッピングを定義します。
        "
        " <C-u>と<CR>はそれぞれコマンドラインでCTRL-uとEnterを押下した時の動作になります
        " <buffer>は現在のバッファにのみキーマップを設定します
        " <silent>はキーマップで実行されるコマンドがコマンドラインに表示されないようにします
        " <Plug>という特殊な文字を使用するとキーを割り当てないマップを用意できます
        " ユーザはこのマップを使用して自分の好きなキーマップを設定できます
        "
        " \ は改行するときに必要です
        nnoremap <silent> <buffer>
          \ <Plug>(session-move-j)
          \ :<C-u> call wolbrw#move(1) <CR>
        nnoremap <silent> <buffer>
          \ <Plug>(session-move-k)
          \ :<C-u> call wolbrw#move(-1) <CR>
        nnoremap <silent> <buffer>
          \ <Plug>(session-close)
          \ :<C-u> call wolbrw#clearHighlight() <CR>
          \ :<C-u> execute 'bwipeout!' g:wolbrw_list_buffer_right <CR>
          \ :<C-u> execute 'bwipeout!' g:wolbrw_list_buffer <CR>
        nnoremap <silent> <buffer>
          \ <Plug>(session-open)
          \ :<C-u> call wolbrw#echo_line_data(getline('.')) <CR>
          "\ :<C-u> call wolbrw#echo_line_data(g:wolbrw_result_dict[getline('.')]) <CR>
          \ :<C-u> call wolbrw#clearHighlight() <CR>
        nnoremap <silent> <buffer>
          \ <Plug>(session-select)
          \ :<C-u> call wolbrw#selectLine()<CR>
        nnoremap <silent> <buffer>
          \ <Plug>(neo4j-history-back)
          \ :<C-u> call wolbrw#make_windows_History() <CR>
        nnoremap <silent> <buffer>
          \ <Plug>(neo4j-history-next)
          \ :<C-u> call wolbrw#make_windows_UnHistory() <CR>
    
        " <Plug>マップをキーにマッピングします
        " `q` は最終的に :<C-u>bwipeout!<CR>
        " `Enter` は最終的に :<C-u>call session#load_session()<CR>
        " が実行されます
        nmap <buffer> j <Plug>(session-move-j)
        nmap <buffer> k <Plug>(session-move-k)
        nmap <buffer> q <Plug>(session-close)
        nmap <buffer> <CR> <Plug>(session-open)
        nmap <buffer> z <Plug>(session-select)
        nmap <buffer> u <Plug>(neo4j-history-back)
        nmap <buffer> <C-r> <Plug>(neo4j-history-next)

      call win_gotoid(current_window_id)
    endif
endfunction


function! wolbrw#move(num) abort
  let pos = getcurpos()
  let newpos = [pos[1] + a:num,pos[2],pos[3],pos[4]]
  call cursor(newpos)
  "echo(g:wolbrw_result_dict[trim(getline('.'))])
  call wolbrw#infowindow(g:wolbrw_result_dict[trim(getline('.'))])
  python3 line = vim.eval('getline(".")')

endfunction

function! wolbrw#infowindow(info) abort
    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer_right, 'unlock')
    call wolbrw#delete_window(g:wolbrw_list_buffer_right)
    call InsertNewLine(g:wolbrw_list_buffer_right, 1, a:info)
    call wolbrw#lock_unlock_window(g:wolbrw_list_buffer_right, 'lock')
endfunction


function! wolbrw#lock_unlock_window(bufname, lock_flag) abort
    let current_window_id = win_getid()
    let targetwindow_id = bufwinid(a:bufname)
    if targetwindow_id != -1
      call win_gotoid(targetwindow_id)

      " バッファの種類を指定します
      " ユーザが書き込むことはないバッファなので`nofile`に設定します
      " 詳細は`:h buftype`を参照してください
      setlocal buftype=nofile
        if a:lock_flag == 'lock'
          setlocal nomodifiable
        elseif a:lock_flag == 'unlock'
          setlocal modifiable
        endif
      call win_gotoid(current_window_id)
    endif
endfunction


function! wolbrw#echo_line_data(msg) abort

  if g:wolbrw#highlighted_lines == {}
    python3 line = vim.eval('getline(".")')

    call win_gotoid(wolbrw#GetOtherWindowId())

    call append(line('.')-1, a:msg)
    call InsertNewLine_for_paste(bufnr(), line('.')-1, g:wolbrw_result_dict[a:msg])

    "call append(line('.')+1, '')
    let pos = getcurpos()
    let newpos = [pos[1]+1 ,pos[2],pos[3],pos[4]]
    "call cursor(newpos)
    call win_gotoid(bufwinid(g:wolbrw_list_buffer))
    normal 0
  else
    "call win_gotoid(g:current_window_id)
    call win_gotoid(wolbrw#GetOtherWindowId())

    for key in keys(g:wolbrw#highlighted_lines)
      let s:key_bi = g:wolbrw#highlighted_lines[key]
      python3 line = vim.eval('s:key_bi')

      call append(line('.')-1, g:wolbrw#highlighted_lines[key])
      "call append(line('.')-1, g:wolbrw_result_dict[g:wolbrw#highlighted_lines[key]])
      call InsertNewLine_for_paste(bufnr(), line('.')-1, g:wolbrw_result_dict[g:wolbrw#highlighted_lines[key]])
      "call append(line('.')-1, g:wolbrw_result_dict[key])
      let pos = getcurpos()
      let newpos = [pos[1]+1 ,pos[2],pos[3],pos[4]]
      "call cursor(newpos)
    endfor
    call win_gotoid(bufwinid(g:wolbrw_list_buffer))
    normal 0
  endif
endfunction


" グローバル変数の初期化
let g:wolbrw#highlighted_lines = {}
" 行をハイライトする関数
function! wolbrw#selectLine() abort
    " 現在の行番号を取得
    let lnum = line('.')

    " 行がすでにハイライトされているかチェック
    if get(g:wolbrw#highlighted_lines, lnum, '-1') == -1
        " ハイライトされていない場合、行をハイライトし、リストに追加
        call matchadd('Statement', '\%' . lnum . 'l')
        let g:wolbrw#highlighted_lines[lnum] = getline('.')
    else
        " ハイライトされている場合、ハイライトを解除し、リストから削除
        echo('ハイライトされている')
        call remove(g:wolbrw#highlighted_lines, lnum)
        call matchdelete(wolbrw#findMatchByLinenum(lnum))
    endif
endfunction

function! wolbrw#findMatchByLinenum(linenum) abort
    let matches = getmatches()
    for match in matches
        if match['pattern'] == '\%'.a:linenum.'l'
            return match['id']
        endif
    endfor
    return {}  " マッチが見つからなかった場合、空の辞書を返す
endfunction

function! wolbrw#clearHighlight() abort
  call clearmatches()
  let g:wolbrw#highlighted_lines = {}
endfunction

function! wolbrw#getSelectedText()
    let selected_text = @"
    return selected_text
endfunction

function! InsertNewLine(buffer,num, text)
    " 改行で分割して配列にする
    let lines = split(a:text, '\\n')

    " 現在の行に配列の内容を挿入
    call setbufline(a:buffer, a:num, lines)
    "call setbufline(a:buffer, a:num+len(lines), 'test')

endfunction

function! InsertNewLine_for_paste(buffer,num, text)
    let current_window_id = win_getid()
    call win_gotoid(a:buffer)
    " 改行で分割して配列にする
    let lines = split(a:text, '\\n')

    " 現在の行に配列の内容を挿入
    let cnt = 0
    for line in lines
      call append(a:num+cnt, line)
      let cnt += 1
    "call setbufline(a:buffer, a:num+len(lines), 'test')
    endfor
    call win_gotoid(current_window_id)
endfunction

function! wolbrw#delete_window(bufname) abort
    let current_window_id = win_getid()
    let targetwindow_id = bufwinid(a:bufname)
    if targetwindow_id != -1
      call win_gotoid(targetwindow_id)
      %delete _
      call win_gotoid(current_window_id)
    endif
endfunction

function! s:create_winid2bufnr_dict() abort " {{{
  let winid2bufnr_dict = {}
  for bnr in filter(range(1, bufnr('$')), 'v:val')
    for wid in win_findbuf(bnr)
      let winid2bufnr_dict[wid] = bnr
    endfor
  endfor
  return winid2bufnr_dict
endfunction " }}}

function! wolbrw#GetOtherWindowId()
  " 現在のタブページ番号を取得
  let current_tnr = tabpagenr()
  " ウィンドウIDからバッファ番号への逆引き辞書を作成
  let winid2bufnr_dict = s:create_winid2bufnr_dict()
  " 現在のタブページ内のすべてのウィンドウをループ
  for wininfo in map(range(1, tabpagewinnr(current_tnr, '$')), '{"wid": win_getid(v:val, current_tnr)}')
    " ウィンドウIDに対応するバッファ番号を取得
    let bufnr = get(winid2bufnr_dict, wininfo.wid, -1)
    " バッファ名を取得
    let bufname = bufnr == -1 ? '' : bufname(bufnr)
    " 条件に合致する場合、ウィンドウIDを返す
    if bufname != g:wolbrw_list_buffer && bufname != g:wolbrw_list_buffer_right
      return wininfo.wid
    endif
  endfor
  " 該当するウィンドウがない場合は-1を返す
  return -1
endfunction
