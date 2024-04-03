# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs

import components
import json
from airium import Airium


with codecs.open('posts.json', 'r', 'utf-8') as file:
    posts = json.load(file)

def generate_post(post):
    # HTML META DATA
    icon_url = "/favicon.ico"
    apple_icon_url = "/apple-touch-icon.png"
    # FILE NAME
    filename = post['permalink'] + ".html"
    # PERMALINKS
    pl_permalink = f'/blog/{filename}'
    eng_permalink = f'/eng/blog/{filename}'
    fr_permalink = f'/fr/blog/{filename}'
    # DATE
    date = post['date']
    # IMG URL
    img_url = post['imgUrl']
    # POLISH VERSION
    pl_title = post['pl']['title']
    pl_excerpt = post['pl']['excerpt']
    pl_content = post['pl']['content']
    pl_img_desc = post['pl']['imgDesc']
    # ENGLISH VERSION
    eng_title = post['eng']['title']
    eng_excerpt = post['eng']['excerpt']
    eng_content = post['eng']['content']
    eng_img_desc = post['eng']['imgDesc']
    # FRENCH VERSION
    fr_title = post['fr']['title']
    fr_excerpt = post['fr']['excerpt']
    fr_content = post['fr']['content']
    fr_img_desc = post['fr']['imgDesc']
    # SOURCES
    sources = []
    for src in post['sources']:
        sources.append(src)

    # POLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        # HEAD
        components.head(a, "pl", pl_title, pl_excerpt, pl_permalink, img_url, icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            # NAVBAR
            components.navbar(a, "pl", pl_permalink, eng_permalink, fr_permalink)
            
            # CONTENT
            with a.div(klass="contentWrapper"):
                with a.article(klass="post"):
                    with a.header():
                        with a.h1(): a(pl_title)
                        with a.h4(klass="date"): a(date)
                        with a.div(klass="links"):
                            with a.div(klass="link", onclick="document.getElementById('share').style.display='block'"):
                                with a.div(klass="linkIcon"):
                                    a.img(src="../imgs/icons/share.png")
                                with a.p(): a("Udost&#281;pnij")
                            with a.div(klass="link", onclick="document.getElementById('cite').style.display='block'"):
                                with a.div(klass="linkIcon"):
                                    a.img(src="../imgs/icons/cite.png")
                                with a.p(): a("Cytuj")
                    with a.main():
                        if (img_url != ""):
                            with a.figure(klass="postPhoto"):
                                a.img(src="/../"+img_url)
                                with a.figcaption(): a(pl_img_desc)
                        with a.section(klass="postContent"): a(pl_content)

                        if(len(sources) > 0):
                            with a.section(class_="sources"):  # ŻRÓDŁA
                                with a.h3(): a("&#377;r&oacute;d&lstrok;a:")
                                with a.ul():
                                    for src in sources:
                                        with a.li(): 
                                            a(src['name'])
                                            with a.a(href=src['link']): a("<i class='fa-solid fa-arrow-up-right-from-square link_icon'></i>")
            # SHARE POPUP
            with a.div(id="share"):
                a.div(klass="mask", onclick="document.getElementById('share').style.display='none'")
                with a.div(klass="box"):
                    with a.div(klass="close", onclick="document.getElementById('share').style.display='none'"):
                        a.img(src="../imgs/icons/close.png")
                    with a.h3(): a("URL:")
                    with a.p(): a("https://agrzelik.github.io" + pl_permalink)
            # CITE POPUP
            with a.div(id="cite"):
                a.div(klass="mask", onclick="document.getElementById('cite').style.display='none'")
                with a.div(klass="box"):
                    with a.div(klass="close", onclick="document.getElementById('cite').style.display='none'"):
                        a.img(src="../imgs/icons/close.png")
                    with a.h3(): a("Link:")
                    with a.p():
                        a("Grzelik A. ")
                        with a.span(): a(f'({date[-4:]}), ')
                        with a.i(): a(pl_title)
                        a(", URL: ")
                        a("https://agrzelik.github.io" + pl_permalink)
                    with a.h3(): a("BibTeX:")
                    with a.p():
                        a("@misc{" + filename[:-5] + ",")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; title={" + pl_title + "},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; url={"+ 'https://agrzelik.github.io' + pl_permalink +"},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; author={Grzelik, Aleksandra},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; year={" + date[-4:] + "},")
                        a.br()
                        a("}")
            # FOOTER
            components.footer(a, "pl")

    f = codecs.open("blog/"+filename, "w", 'utf-8')
    f.write(str(a))
    f.close()

    # ENGLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        # HEAD
        components.head(a, "en", eng_title, eng_excerpt, eng_permalink, img_url, icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            # NAVBAR
            components.navbar(a, "en", pl_permalink, eng_permalink, fr_permalink)
            
            # CONTENT
            with a.div(klass="contentWrapper"):
                with a.article(klass="post"):
                    with a.header():
                        with a.h1(): a(eng_title)
                        with a.h4(klass="date"): a(date)
                        with a.div(klass="links"):
                            with a.div(klass="link", onclick="document.getElementById('share').style.display='block'"):
                                with a.div(klass="linkIcon"):
                                    a.img(src="../../imgs/icons/share.png")
                                with a.p(): a("Share")
                            with a.div(klass="link", onclick="document.getElementById('cite').style.display='block'"):
                                with a.div(klass="linkIcon"):
                                    a.img(src="../../imgs/icons/cite.png")
                                with a.p(): a("Cite")
                    with a.main():
                        if (img_url != ""):
                            with a.figure(klass="postPhoto"):
                                a.img(src="/../"+img_url)
                                with a.figcaption(): a(eng_img_desc)
                        with a.section(klass="postContent"): a(eng_content)

                        if(len(sources) > 0):
                            with a.section(class_="sources"):  # ŻRÓDŁA
                                with a.h3(): a("Sources:")
                                with a.ul():
                                    for src in sources:
                                        with a.li(): 
                                            a(src['name'])
                                            with a.a(href=src['link']): a("<i class='fa-solid fa-arrow-up-right-from-square link_icon'></i>")
            # SHARE POPUP
            with a.div(id="share"):
                a.div(klass="mask", onclick="document.getElementById('share').style.display='none'")
                with a.div(klass="box"):
                    with a.div(klass="close", onclick="document.getElementById('share').style.display='none'"):
                        a.img(src="../../imgs/icons/close.png")
                    with a.h3(): a("URL:")
                    with a.p(): a("https://agrzelik.github.io" + eng_permalink)
            # CITE POPUP
            with a.div(id="cite"):
                a.div(klass="mask", onclick="document.getElementById('cite').style.display='none'")
                with a.div(klass="box"):
                    with a.div(klass="close", onclick="document.getElementById('cite').style.display='none'"):
                        a.img(src="../../imgs/icons/close.png")
                    with a.h3(): a("Link:")
                    with a.p():
                        a("Grzelik A. ")
                        with a.span(): a(f'({date[-4:]}), ')
                        with a.i(): a(eng_title)
                        a(", URL: ")
                        a("https://agrzelik.github.io" + eng_permalink)
                    with a.h3(): a("BibTeX:")
                    with a.p():
                        a("@misc{" + filename[:-5] + ",")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; title={" + eng_title + "},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; url={"+ 'https://agrzelik.github.io' + eng_permalink +"},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; author={Grzelik, Aleksandra},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; year={" + date[-4:] + "},")
                        a.br()
                        a("}")
            # FOOTER
            components.footer(a, "en")

    f = codecs.open("eng/blog/"+filename, "w", 'utf-8')
    f.write(str(a))
    f.close()


    # FRENCH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="fr"):
        # HEAD
        components.head(a, "fr", fr_title, fr_excerpt, fr_permalink, img_url, icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            # NAVBAR
            components.navbar(a, "fr", pl_permalink, eng_permalink, fr_permalink)
            
            # CONTENT
            with a.div(klass="contentWrapper"):
                with a.article(klass="post"):
                    with a.header():
                        with a.h1(): a(fr_title)
                        with a.h4(klass="date"): a(date)
                        with a.div(klass="links"):
                            with a.div(klass="link", onclick="document.getElementById('share').style.display='block'"):
                                with a.div(klass="linkIcon"):
                                    a.img(src="../../imgs/icons/share.png")
                                with a.p(): a("Propagater")
                            with a.div(klass="link", onclick="document.getElementById('cite').style.display='block'"):
                                with a.div(klass="linkIcon"):
                                    a.img(src="../../imgs/icons/cite.png")
                                with a.p(): a("Citation")
                    with a.main():
                        if (img_url != ""):
                            with a.figure(klass="postPhoto"):
                                a.img(src="/../"+img_url)
                                with a.figcaption(): a(fr_img_desc)
                        with a.section(klass="postContent"): a(fr_content)

                        if(len(sources) > 0):
                            with a.section(class_="sources"):  # ŻRÓDŁA
                                with a.h3(): a("Sources:")
                                with a.ul():
                                    for src in sources:
                                        with a.li(): 
                                            a(src['name'])
                                            with a.a(href=src['link']): a("<i class='fa-solid fa-arrow-up-right-from-square link_icon'></i>")
            # SHARE POPUP
            with a.div(id="share"):
                a.div(klass="mask", onclick="document.getElementById('share').style.display='none'")
                with a.div(klass="box"):
                    with a.div(klass="close", onclick="document.getElementById('share').style.display='none'"):
                        a.img(src="../../imgs/icons/close.png")
                    with a.h3(): a("URL:")
                    with a.p(): a("https://agrzelik.github.io" + fr_permalink)
            # CITE POPUP
            with a.div(id="cite"):
                a.div(klass="mask", onclick="document.getElementById('cite').style.display='none'")
                with a.div(klass="box"):
                    with a.div(klass="close", onclick="document.getElementById('cite').style.display='none'"):
                        a.img(src="../../imgs/icons/close.png")
                    with a.h3(): a("Link:")
                    with a.p():
                        a("Grzelik A. ")
                        with a.span(): a(f'({date[-4:]}), ')
                        with a.i(): a(fr_title)
                        a(", URL: ")
                        a("https://agrzelik.github.io" + fr_permalink)
                    with a.h3(): a("BibTeX:")
                    with a.p():
                        a("@misc{" + filename[:-5] + ",")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; title={" + fr_title + "},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; url={"+ 'https://agrzelik.github.io' + fr_permalink +"},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; author={Grzelik, Aleksandra},")
                        a.br()
                        a('&nbsp;&nbsp;&nbsp;')
                        a("&nbsp; year={" + date[-4:] + "},")
                        a.br()
                        a("}")
            # FOOTER
            components.footer(a, "fr")

    f = codecs.open("fr/blog/"+filename, "w", 'utf-8')
    f.write(str(a))
    f.close()

def generate_blog_page():
    # VARIABLES
    site_title_pl = "Blog - Aleksandra Grzelik"
    site_description_pl = "Aleksandra Grzelik - blog naukowy. Ekonometria, Analiza danych, Statystyka matematyczna. Modelowanie matametyczne, machine learing."
    site_title_eng = "Blog - Aleksandra Grzelik"
    site_description_eng = "Aleksandra Grzelik - scientific blog. Econometrics, Data Science, Mathematical Statistics. Matematical modelling, machine learing."
    site_title_fr = "Blog - Aleksandra Grzelik"
    site_description_fr = "Blog - Aleksandra Grzelik"
    # HTML META DATA
    icon_url = "/favicon.ico"
    apple_icon_url = "/apple-touch-icon.png"

    # POLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        components.head(a, "pl", site_title_pl, site_description_pl, "/blog.html", "/mainbg.jpeg", icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "pl", "/blog.html", "/eng/blog.html", "fr/blog.html")
            # CONTENT
            with a.div(klass="contentWrapper"):
                with a.div(klass="posts"):
                    a.h1(_t="Blog")
                    for post in posts:
                        with a.a(klass="postPreview", href="blog/"+post['permalink']+".html"):
                            if(post['imgUrl'] != ""):
                                a.img(src=post['imgUrl'])
                            with a.div(klass="desc"):
                                a.h3(_t=post['pl']['title'])
                                a.small(_t=post['date'])
                                a.p(_t=post['pl']['excerpt'])
            # FOOTER
            components.footer(a, "pl")
    f = codecs.open("blog.html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    # ENGLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        components.head(a, "en", site_title_eng, site_description_eng, "/eng/blog.html", "/mainbg.jpeg", icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "en", "/blog.html", "/eng/blog.html", "fr/blog.html")
            # CONTENT
            with a.div(klass="contentWrapper"):
                with a.div(klass="posts"):
                    a.h1(_t="Blog")
                    for post in posts:
                        with a.a(klass="postPreview", href="blog/"+post['permalink']+".html"):
                            if(post['imgUrl'] != ""):
                                a.img(src="../"+post['imgUrl'])
                            with a.div(klass="desc"):
                                a.h3(_t=post['eng']['title'])
                                a.small(_t=post['date'])
                                a.p(_t=post['eng']['excerpt'])
            # FOOTER
            components.footer(a, "en")
    f = codecs.open("eng/blog.html", "w", 'utf-8')
    f.write(str(a))
    f.close()
   
    # FRENCH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="fr"):
        components.head(a, "fr", site_title_fr, site_description_fr, "/fr/blog.html", "/mainbg.jpeg", icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "fr", "/blog.html", "/eng/blog.html", "fr/blog.html")
            # CONTENT
            with a.div(klass="contentWrapper"):
                with a.div(klass="posts"):
                    a.h1(_t="Blog")
                    for post in posts:
                        with a.a(klass="postPreview", href="blog/"+post['permalink']+".html"):
                            if(post['imgUrl'] != ""):
                                a.img(src="../"+post['imgUrl'])
                            with a.div(klass="desc"):
                                a.h3(_t=post['fr']['title'])
                                a.small(_t=post['date'])
                                a.p(_t=post['fr']['excerpt'])
            # FOOTER
            components.footer(a, "fr")
    f = codecs.open("fr/blog.html", "w", 'utf-8')
    f.write(str(a))
    f.close()


# CALL FUNCTIONS
def populate_posts():
    for post in posts:
        generate_post(post)
    generate_blog_page()
    print(f"Succesfully generated {len(posts)} posts.")
