import sys,os,re
import requests, urllib
from bs4 import BeautifulSoup
import biblesitation

DOMEIN = 'https://wol.jw.org'

def make_disp_result(text='', scope='', order=''):
    # r: 並び順
    #   occ    出例の多い順
    #   newest 新しい順
    #   oldest 古い順
    
    # p: 範囲
    #   sen  同じ文の中
    #   par  同じ段落の中
    #   doc  同じ記事の中
    
    org_dict = {}
    result_url_dict = {}
    prog_del_return = re.compile(r'[\n\r\u200e]')

    search_word_utf8 = text
    search_word = urllib.parse.quote(search_word_utf8, encoding='utf-8')
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    urlpath = f"{DOMEIN}/ja/wol/s/r7/lp-j?q={search_word}&p={scope}&r={order}&st=e&fc%5B%5D=gloss&fc%5B%5D=it&fc%5B%5D=dx&fc%5B%5D=w&fc%5B%5D=g&fc%5B%5D=bk&fc%5B%5D=yb&fc%5B%5D=mwb&fc%5B%5D=km&fc%5B%5D=brch&fc%5B%5D=bklt&fc%5B%5D=trct&fc%5B%5D=kn&fc%5B%5D=web&fc%5B%5D=pgm&fc%5B%5D=manual"
    res=requests.get(urlpath, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    search_results = soup.select('ul.results.resultContentDocument')
    for search_result in search_results:
        try:
            result_source = search_result.select('li.ref')[0].get_text()
            result_source = prog_del_return.sub('',result_source)
        except:
            continue

        result_caption = search_result.select('li.caption')[0].get_text()
        result_caption = prog_del_return.sub('',result_caption)
        result_caption = result_caption.strip()

        result_url     = search_result.select('li.caption')[0].select('a')[0].attrs['href']
        result_url     = DOMEIN + result_url

        result_content = search_result.select('article')[0].get_text()
        result_content = prog_del_return.sub('',result_content)

        org_dict[f'{result_caption}'] = f'{result_source}\n{result_content}\n{result_url}'
        result_url_dict[f'{result_caption}'] = f'{result_url}'

    inner_list = [[key, value] for key, value in org_dict.items()]
    return [inner_list, org_dict, result_url_dict]


def wolbrw_search(
                    text,
                    scope='par',
                    order='occ'):

    # text: 文字列 (q に投入するもの)
    # この関数では、 スペース(U+0020)が '&' で連結されたものが渡される(wolbrw#ParseFlags の mode が 'search_simple')

    result = make_disp_result(text=text, scope=scope, order=order)
    return result


def wolbrw_mean_search(
                    text,
                    scope='par',
                    order='occ'):
    
    # text: 文字列 (q に投入するもの)
    # この関数では、 単純な文字列が渡される(wolbrw#ParseFlags の mode が 'search_mean')

    bible_citation_list = biblesitation.citation_text(text)
    search_bi_text = "(という意味|という語)&"
    cnt = 0
    for bi_text in bible_citation_list:
        if cnt == 0:
            search_bi_text += f'({bi_text}'
        else:
            search_bi_text += f'|{bi_text}'
        cnt += 1
    search_bi_text += ')'
    print(search_bi_text)

    result = make_disp_result(text=search_bi_text, scope=scope, order=order)
    return result
