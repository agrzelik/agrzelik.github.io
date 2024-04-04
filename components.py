# -*- coding: utf-8 -*-

from airium import Airium

#base_url = "http://127.0.0.1:5500/" # debug
base_url = "https://agrzelik.github.io/" # production

def head(a, language, title, excerpt, permalink, img_url, icon_url, apple_icon_url):
        with a.head():
            # METADATA
            a("<!-- METADATA -->")
            a.title(_t=title)
            a.meta(charset="utf-8")
            a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
            a.meta(name="description", content=excerpt)
            a.meta(name="author", content="Aleksandra Grzelik")
            # OPEN GRAPH
            a("<!-- OPEN GRAPH -->")
            a.meta(property="og:title", content=title)
            a.meta(property="og:type", content="website")
            a.meta(property="og:url", content="https://agrzelik.github.io" + permalink)
            a.meta(property="og:description", content=excerpt)
            a.meta(property="og:image", content=base_url+img_url)
            a.meta(property="og:locale", content=language+"_"+language.upper())
            # RESOURCES
            a("<!-- RESOURCES -->")
            a.link(rel="stylesheet", href=base_url + "css/main.css")
            if(permalink != "/" and permalink != "/eng.html" and permalink != "/fr.html"):
                a.link(rel="stylesheet", href=base_url + "css/blog.css")
                a.link(rel="stylesheet", href=base_url +"css/projects.css")
            a.script(src="https://kit.fontawesome.com/d7fb58415a.js", crossorigin="anonymous")
            # ICONS
            a("<!-- ICONS -->")
            a.link(rel="icon", type="image/png", sizes="32x32", href=base_url+"favicon-32x32.png")
            a.link(rel="icon", type="image/png", sizes="16x16", href=base_url+"favicon-16x16.png")
            a.link(rel="apple-touch-icon",sizes="180x180", href=base_url+"apple-touch-icon.png")
            a.link(rel="manifest", href=base_url+"site.webmanifest")
            a.link(rel="mask-icon", href=base_url+"safari-pinned-tab.svg", color="#5bbad5")
            # CANNONICAL
            a("<!-- CANNONICAL -->")
            a.link(rel="cannonical", href="https://agrzelik.github.io" + permalink)

def navbar(a,language, pl_permalink, eng_permalink, fr_permalink):
    with a.div(id="preloader"):
        with a.div(id="preloader-polygon"):
            a.div(id="preloader-polygon-side-1")
            a.div(id="preloader-polygon-side-2")
            a.div(id="preloader-polygon-side-3")
            a.div(id="preloader-polygon-side-4")
            a.div(id="preloader-polygon-side-5")
            a.div(id="preloader-polygon-side-6")    

    if(language == "en"):
        landing_url = "/eng.html"
        about_url = base_url + "eng.html#about-me"
        about_caption = "About me"
        projects_url = base_url + "eng/projects.html"
        projects_caption = "My Projects"
        blog_url = base_url + "eng/blog.html"
        blog_caption = "Blog"
        contact_url = base_url + "eng.html#contact"
        contact_caption = "Contact me"
        subtitle = "Data science"
        current_lang = "English"
        current_lang_img = base_url + "imgs/icons/eng.png"
        other_lang_1 = "Polski"
        other_lang_1_img = base_url + "imgs/icons/pl.png"
        other_lang_1_url = base_url + pl_permalink
        other_lang_2 = "Fran&ccedil;ais"
        other_lang_2_img = base_url + "imgs/icons/fr.png"
        other_lang_2_url = base_url + fr_permalink
    elif(language == "fr"):
        landing_url = "/fr.html"
        about_url = base_url + "fr.html#about-me"
        about_caption = "Sur moi"
        projects_url = base_url + "fr/projects.html"
        projects_caption = "Mes projets"
        blog_url = base_url + "fr/blog.html"
        blog_caption = "Blog"
        contact_url = base_url + "fr.html#contact"
        contact_caption = "Contactez-moi"
        subtitle = "L'Analyse des Donnes"
        current_lang = "Fran&ccedil;ais"
        current_lang_img = base_url + "imgs/icons/fr.png"
        other_lang_1 = "Polski"
        other_lang_1_img = base_url + "imgs/icons/pl.png"
        other_lang_1_url = base_url + pl_permalink
        other_lang_2 = "English"
        other_lang_2_img = base_url + "imgs/icons/eng.png"
        other_lang_2_url = base_url + eng_permalink
    else:
        landing_url = "/"
        about_url = base_url[:-1] + "#about-me"
        about_caption = "O mnie"
        projects_url = base_url + "projects.html"
        projects_caption = "Moje projekty"
        blog_url = base_url + "blog.html"
        blog_caption = "Blog"
        contact_url = base_url[:-1] + "#contact"
        contact_caption = "Kontakt"
        subtitle = "Analiza danych"

        current_lang = "Polski"
        current_lang_img = base_url + "imgs/icons/pl.png"
        other_lang_1 = "English"
        other_lang_1_img = base_url + "imgs/icons/eng.png"
        other_lang_1_url = base_url + eng_permalink
        other_lang_2 = "Fran&ccedil;ais"
        other_lang_2_img = base_url + "imgs/icons/fr.png"
        other_lang_2_url = base_url + fr_permalink


    with a.div(id="sideMenu"):
        with a.a(href=about_url, onclick="document.querySelector('.about-me').scrollIntoView();closeMenu()"): a(about_caption)
        with a.a( href=projects_url): a(projects_caption)
        with a.a(href=blog_url): a(blog_caption)
        with a.a(href=contact_url, onclick="document.querySelector('.contact').scrollIntoView();closeMenu()"):  a(contact_caption)
    # NAVBAR
    with a.nav(id="navbar"):
                with a.div(klass="navbar-logo", onclick=f"location.href='{landing_url}'"):
                    with a.h1(): a("Aleksandra Grzelik")
                    with a.p(): a(subtitle)
                with a.div(id="navbar-logowrap"):
                    with a.a(href=about_url, onclick="document.querySelector('.about-me').scrollIntoView()"): a(about_caption)
                    with a.a(href=projects_url): a(projects_caption)
                    with a.a(href=blog_url): a(blog_caption)
                    with a.a(href=contact_url, onclick="document.querySelector('.contact').scrollIntoView()"): a(contact_caption)
                    # LANGUAGE SELECTOR
                    with a.div(klass="lang-icon", onclick="language()"):
                        with a.p(id="lang-icon-name"): a(current_lang)
                        a.img(src=current_lang_img)
                        with a.p(id="lang-arrow"): a("&#9660;")
                    with a.div(klass="mobileMenu", onclick="mobileMenu()"):
                        a.span()
                        a.span()
                        a.span()
                    with a.div(klass="lang"):
                        with a.div(onclick=f"window.open('{other_lang_1_url}', target='_self')"): 
                            with a.p(): a(other_lang_1)
                            a.img(src=other_lang_1_img)
                        with a.div(onclick=f"window.open('{other_lang_2_url}', target='_self')"): 
                            with a.p(): a(other_lang_2)
                            a.img(src=other_lang_2_img)
    return

def footer(a, language):
    with a.footer():
        a.p(id="year")
        if(language == "en"):
                with a.p(): 
                    a("Design by:")
                    with a.a(href="https://matig152.github.io/"):
                        a("Mateusz Grzelik &#128279;")
        elif(language == "fr"):
                with a.p(): 
                    a("Le projet:")
                    with a.a(href="https://matig152.github.io/"):
                        a("Mateusz Grzelik &#128279;")
        else:
                with a.p(): 
                    a("Zaprojektowa&lstrok;:")
                    with a.a(href="https://matig152.github.io/"):
                        a("Mateusz Grzelik &#128279;")
    a.script(src=base_url+"js/main.js")
    
        