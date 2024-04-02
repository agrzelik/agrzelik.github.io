# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
from airium import Airium
import json
import components

with codecs.open('posts.json', 'r', 'utf-8') as file:
    posts = json.load(file)
with codecs.open('projects.json', 'r', 'utf8') as file:
    projects = json.load(file)

def generate_landing_page():
    # VARIABLES
    site_title_pl = "Aleksandra Grzelik - Portfolio"
    site_description_pl = "Aleksandra Grzelik - Portfolio"
    site_title_eng = "Aleksandra Grzelik - Portfolio"
    site_description_eng = "Aleksandra Grzelik - Portfolio"
    site_title_fr = "Aleksandra Grzelik - Portfolio"
    site_description_fr = "Aleksandra Grzelik - Portfolio"
    # HTML META DATA
    icon_url = "/favicon.ico"
    apple_icon_url = "/apple-touch-icon.png"
    # IMGS URLS
    main_bg_url = "imgs/mainbg.jpg"
    about_me_img = "imgs/about.jpg"
    interests_img = "imgs/interests.jpg"
    internship_icon = "https://static-00.iconduck.com/assets.00/google-ads-icon-2048x1837-4vbvpswm.png"


    # POLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        components.head(a, "pl", site_title_pl, site_description_pl, "/", "imgs/mainbg.jpg", icon_url, apple_icon_url)
        with a.body(onload="preloader()", onscroll="navbar()"):
            components.navbar(a, "pl", "/", "/eng.html", "/fr.html")
            # MAINFRAME
            with a.div(klass="mainbg"):
                a.img(src=main_bg_url)

            with a.div(klass="mainframe"):
                with a.div(klass="mainframe-content"):
                    a.h1(_t="Witaj w moim portfolio")
                    a.p(_t="Zapraszam do zapoznania si&#281; z moimi projektami")
            # ABOUT ME
            with a.div(klass="about-me"):
                with a.div(klass="bio"):
                    with a.div(klass="bio-photo"):
                        a.img(src=about_me_img)
                    with a.div(klass="bio-content"):
                        a.h1(_t="O mnie")
                        a.p(_t="Nazywam się Aleksandra Grzelik. Pasjonuje mnie modelowanie matematyczne i statystyczne, szczególnie zjawisk z zakresu psychologii, ekologii czy socjologii. W lipcu 2022 ukończyłam studia licencjackie na kierunku Ekonometria i Analityka Danych na Uniwersytecie Łódzkim, moja praca dyplomowa podejmowała statystyczną analizę poziomu szczęścia studentów. Praca była inspirowana alternatywnym (wobec PKB) podejściem do pomiaru dobrobytu społeczeństwa, miarami opartymi na czynnikach takich jak dbałość o środowisko czy praworządność. W oparciu o badania, m.in. World Happiness Report, przygotowane zostały miara poziomu szczęścia i model, który po odpowiedniej walidacji, pozwolił wyłonić najważniejsze zmienne decydujące o poziomie szczęścia wśród studentów. W październiku 2022 rozpoczęłam studia magisterskie na kierunku Analiza Danych (UŁ). W czasie studiów zdobyłam kompetencje związane z matematyką oraz sztuczną inteligencją, uczestniczyłam w wielu ciekawych projektach, więcej o nich w zakładce 'Moje projekty'.")
                with a.div(klass="exp"):
                    with a.div(klass="exp-educ"):
                        a.h2(_t="Edukacja")
                        with a.ul(klass="exp-tiles"):
                            with a.li():
                                a.img(src="imgs/icons/ul-mi.png")
                                with a.span():
                                    a.h3(_t="Analiza danych")
                                    a.small(_t="Wydział Matematyki i Informatyki")
                                    a.small(_t="Uniwersytet Łódzki")
                                    a.small(_t="studia licencjackie")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2022 - obecnie")
                            with a.li():
                                a.img(src="imgs/icons/ul-eksoc.jpg")
                                with a.span():
                                    a.h3(_t="Ekonometria i analityka danych")
                                    a.small(_t="Wydział Ekonomiczno-Socjologiczny")
                                    a.small(_t="Uniwersytet Łódzki")
                                    a.small(_t="studia licencjackie")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2019-2022")
                            with a.li():
                                a.img(src="imgs/icons/ul-fil.png")
                                with a.span():
                                    a.h3(_t="Filologia romańska")
                                    a.small(_t="Wydział Filologiczny")
                                    a.small(_t="Uniwersytet Łódzki")
                                    a.small(_t="studia licencjackie")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2019-2022")
                    with a.div(klass="exp-comp"):
                        a.h2(_t="Kompetencje")
                        with a.ul(klass="comps"):
                            a.li(_t="zaplecze teoretyczne z zakresu statystyki, matematyki, finansów")
                            a.li(_t="programowanie: moim ulubionym językiem jest Python")
                            a.li(_t="tworzenie modeli uczenia maszynowego, sieci neuronowe")
                            a.li(_t="znajomość technik weryfikacji modeli i testów statystycznych")
                            a.li(_t="umiejętność przyswojenia i redakcji tekstów naukowych")
                            a.li(_t="myślenie analityczne, z miejscem na kreatywność")
                    with a.div(klass="exp-job"):
                        a.h2(_t="Doświadczenie")
                        with a.ul(klass="exp-tiles"):
                            with a.li():
                                a.img(src="imgs/icons/acc.png")
                                with a.span():
                                    a.h3(_t="Application Developement Associate ")
                                    a.small(_t="Accenture Polska")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> wrzesień 2022 - obecnie")
                            with a.li():
                                a.img(src=internship_icon)
                                with a.span():
                                    a.h3(_t="Praktyki zawodowe")
                                    a.small(_t="przygotowanie projektu teoretycznego dotyczącego optymalizacji reklam w Google Ads")
                                    a.small(_t="Evillage.pl")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2021 lipiec - sierpień")
                    with a.div(klass="exp-jezyki"):
                        a.h2(_t="Języki")
                        with a.ul(klass="langs"):
                            with a.li():
                                a.img(src="imgs/icons/pl.png")
                                a.p(_t="Polski - język ojczysty")
                            with a.li():
                                a.img(src="imgs/icons/eng.png")
                                a.p(_t="Angielski - poziom C1")
                            with a.li():
                                a.img(src="imgs/icons/fr.png")
                                a.p(_t="Francuski - poziom B2")
                with a.div(klass="bio"):
                    with a.div(klass="bio-content", id="interests"):
                        a.h1(_t="Zainteresowania")
                        a.p(_t="Lubię sport, jeżdżę na rolkach, ćwiczę step aerobik, czasami wybieram ćwiczenia siłowe. Lubię spacerować, najczęściej z moimi pieskami Riną i Ruby, to dla mnie okazja do aktywnego wypoczynku i kontaktu z naturą, który jest dla mnie ważny. Pasjonuje mnie czytanie, chociaż ciągle brakuje mi na nie czasu. Najchętniej sięgam po literaturę piękną, reportaże, pozycje popularnonaukowe i romanse. Prowadzę subiektywny ranking przeczytanych pozycji, w 2023 roku moimi faworytami były “Fizyka Smutku” (Georgi Gospodinow) oraz “Madame” (Antoni Libera). W bieżącym roku uczestniczę w wyzwaniu czytelniczym - 40 książek, a moje postępy śledzę na <a href='https://www.goodreads.com/user/show/163587605-ola'>goodreads</a>.  ")
                    with a.div(klass="bio-photo"):
                        a.img(src=interests_img)
                with a.section(klass="projectBlog"):
                    with a.article():
                        a.h1(_t="Projekty")
                        with a.a(klass="project", href="projects/"+projects[-1]['permalink']+'.html'):
                            a.img(src=projects[-1]['img'])
                            with a.div():
                                a.h3(_t=projects[-1]['pl']['title'])
                                a.small(_t=projects[-1]['date'])
                                a.p(_t=projects[-1]['pl']['excerpt'])
                    with a.article():
                        a.h1(_t="Blog")
                        with a.a(klass="project", href="blog/"+posts[-1]['permalink']+'.html'):
                            a.img(src=posts[-1]['imgUrl'])
                            with a.div():
                                a.h3(_t=posts[-1]['pl']['title'])
                                a.small(_t=posts[-1]['date'])
                                a.p(_t=posts[-1]['pl']['excerpt'])
                with a.div(klass="contact"):
                    a.h1(_t="Kontakt")
                    with a.div(klass="contact-wrap"):
                        with a.div(klass="contact-wrap-left"):
                            # with a.div(klass="contact-info"):
                            #     with a.p():
                            #         a.i(klass="fa-regular fa-envelope")
                            #         a("&nbsp;ola.grzelik.bno@gmail.com")
                            with a.div(klass="contact-links"):
                                with a.a(href="https://www.linkedin.com/in/aleksandra-grzelik-070291210?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app&fbclid=IwAR36g7HqOMaWRaIIc6dOUlOCUwKUVuVgH_zEZzSmF-seF1W-PBMWviSxEC0", target="_blank"):
                                    a.img(src="imgs/icons/linkedin.png")
                                    a.p(_t="LinkedIn")
                        with a.form():
                            a.h1(style="text-align:center", _t="Wyślij mi wiadomość")
                            a.label(_for="imie", _t="Twoje imię:")
                            a.input(type="text", id="imie", name="imie")
                            a.label(_for="email", _t="Twój email:")
                            a.input(type="email", id="email", name="email")
                            a.label(_for="tresc", _t="Wiadomość:")
                            a.textarea(id="tresc")
                            a.input(id="submit", onclick="sendMail()", value="Wyślij &gt;")

            # FOOTER
            components.footer(a, "pl")
    f = codecs.open("index.html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    # ENGLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        components.head(a, "en", site_title_eng, site_description_eng, "/", "imgs/mainbg.jpg", icon_url, apple_icon_url)
        with a.body(onload="preloader()", onscroll="navbar()"):
            components.navbar(a, "en", "/", "/eng.html", "/fr.html")
            # MAINFRAME
            with a.div(klass="mainbg"):
                a.img(src=main_bg_url)

            with a.div(klass="mainframe"):
                with a.div(klass="mainframe-content"):
                    a.h1(_t="Welcome to my portfolio")
                    a.p(_t="Scroll to check out my projects and blog")
            # ABOUT ME
            with a.div(klass="about-me"):
                with a.div(klass="bio"):
                    with a.div(klass="bio-photo"):
                        a.img(src=about_me_img)
                    with a.div(klass="bio-content"):
                        a.h1(_t="About me")
                        a.p(_t="My name is Aleksandra Grzelik. I am interested in mathematical and statistical modeling, particularly for phenomena in the field of psychology, ecology or sociology. I graduated from the University of Lodz in July 2022 with a BA in Econometrics and Data Analytics, my thesis dealt with statistical analysis of students' happiness level. The thesis was inspired by an alternative (to GDP) approach to measuring the well-being of a society: the measures based on factors such as environmental care or lawfulness. On the basis of research, including the World Happiness Report, a happiness measure and a model were prepared. After appropriate validation, the model was used to identify the most important variables determining the level of happiness among students. In October 2022, I started MA in Data Analysis (University of Łódź). During studies, I gained competences in mathematics and artificial intelligence and participated in many interesting projects. Read more about them in 'My projects' tab.")
                with a.div(klass="exp"):
                    with a.div(klass="exp-educ"):
                        a.h2(_t="Education")
                        with a.ul(klass="exp-tiles"):
                            with a.li():
                                a.img(src="imgs/icons/ul-mi.png")
                                with a.span():
                                    a.h3(_t="Data analysis")
                                    a.small(_t="Faculty of Mathematics and Computer Science")
                                    a.small(_t="University of Lodz")
                                    a.small(_t="master's degree")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2022 - obecnie")
                            with a.li():
                                a.img(src="imgs/icons/ul-eksoc.jpg")
                                with a.span():
                                    a.h3(_t="Econometrics and data analysis")
                                    a.small(_t="Faculty of Economics and Sociology")
                                    a.small(_t="University of Lodz")
                                    a.small(_t="bachelor's degree")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2019-2022")
                            with a.li():
                                a.img(src="imgs/icons/ul-fil.png")
                                with a.span():
                                    a.h3(_t="Roman philology")
                                    a.small(_t="Faculty of Philology")
                                    a.small(_t="University of Lodz")
                                    a.small(_t="bachelor's degree")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2019-2022")
                    with a.div(klass="exp-comp"):
                        a.h2(_t="Competences")
                        with a.ul(klass="comps"):
                            a.li(_t="theoretical background in statistics, mathematics, finance")
                            a.li(_t="programming: my favourite language is Python")
                            a.li(_t="development of machine learning models, neural networks")
                            a.li(_t="knowledge of techniques for verifying models and statistical tests")
                            a.li(_t="ability to comprehend and prepare scientific texts")
                            a.li(_t="analytical thinking, but also creativity")
                    with a.div(klass="exp-job"):
                        a.h2(_t="Experience")
                        with a.ul(klass="exp-tiles"):
                            with a.li():
                                a.img(src="imgs/icons/acc.png")
                                with a.span():
                                    a.h3(_t="Application Developement Associate ")
                                    a.small(_t="Accenture Polska")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> september 2022 - present")
                            with a.li():
                                a.img(src=internship_icon)
                                with a.span():
                                    a.h3(_t="Internship")
                                    a.small(_t="Participating in Google Ads optimization project")
                                    a.small(_t="Evillage.pl")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2021 july - august")
                    with a.div(klass="exp-jezyki"):
                        a.h2(_t="Languages")
                        with a.ul(klass="langs"):
                            with a.li():
                                a.img(src="imgs/icons/pl.png")
                                a.p(_t="Polish - native language")
                            with a.li():
                                a.img(src="imgs/icons/eng.png")
                                a.p(_t="English - C1 level")
                            with a.li():
                                a.img(src="imgs/icons/fr.png")
                                a.p(_t="French - B2 level")
                with a.div(klass="bio"):
                    with a.div(klass="bio-content", id="interests"):
                        a.h1(_t="Interests")
                        a.p(_t="I enjoy sports, I rollerblade, practice step aerobics, sometimes I opt for strength training. I like to walk, usually with my dogs Rina and Ruby, it's an opportunity to relax actively and get in touch with nature, which is important to me. I am keen on reading, although I constantly lack time for it. My favourite genres are fiction, reportage, popular science and romance. I conduct a subjective ranking of the books I have read; in 2023, my favourites were The Physics of Sorrow (Georgi Gospodinov) and Madame (Antoni Libera). This year I am taking part in a reading challenge - 40 books - and I track my progress on <a href='https://www.goodreads.com/user/show/163587605-ola'>goodreads</a>.  ")
                    with a.div(klass="bio-photo"):
                        a.img(src=interests_img)
                with a.section(klass="projectBlog"):
                    with a.article():
                        a.h1(_t="Projects")
                        with a.a(klass="project", href="eng/projects/"+projects[-1]['permalink']+'.html'):
                            a.img(src=projects[-1]['img'])
                            with a.div():
                                a.h3(_t=projects[-1]['eng']['title'])
                                a.small(_t=projects[-1]['date'])
                                a.p(_t=projects[-1]['eng']['excerpt'])
                    with a.article():
                        a.h1(_t="Blog")
                        with a.a(klass="project", href="eng/blog/"+posts[-1]['permalink']+'.html'):
                            a.img(src=posts[-1]['imgUrl'])
                            with a.div():
                                a.h3(_t=posts[-1]['eng']['title'])
                                a.small(_t=posts[-1]['date'])
                                a.p(_t=posts[-1]['eng']['excerpt'])
                with a.div(klass="contact"):
                    a.h1(_t="Contact")
                    with a.div(klass="contact-wrap"):
                        with a.div(klass="contact-wrap-left"):
                            # with a.div(klass="contact-info"):
                            #     with a.p():
                            #         a.i(klass="fa-regular fa-envelope")
                            #         a("&nbsp;ola.grzelik.bno@gmail.com")
                            with a.div(klass="contact-links"):
                                with a.a(href="https://www.linkedin.com/in/aleksandra-grzelik-070291210?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app&fbclid=IwAR36g7HqOMaWRaIIc6dOUlOCUwKUVuVgH_zEZzSmF-seF1W-PBMWviSxEC0", target="_blank"):
                                    a.img(src="imgs/icons/linkedin.png")
                                    a.p(_t="LinkedIn")
                        with a.form():
                            a.h1(style="text-align:center", _t="Send me a message")
                            a.label(_for="imie", _t="Your name:")
                            a.input(type="text", id="imie", name="imie")
                            a.label(_for="email", _t="Your email:")
                            a.input(type="email", id="email", name="email")
                            a.label(_for="tresc", _t="Message:")
                            a.textarea(id="tresc")
                            a.input(id="submit", onclick="sendMail()", value="Send &gt;")

            # FOOTER
            components.footer(a, "en")
    f = codecs.open("eng.html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    # FRENCH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="fr"):
        components.head(a, "fr", site_title_fr, site_description_fr, "/", "imgs/mainbg.jpg", icon_url, apple_icon_url)
        with a.body(onload="preloader()", onscroll="navbar()"):
            components.navbar(a, "fr", "/", "/eng.html", "/fr.html")
            # MAINFRAME
            with a.div(klass="mainbg"):
                a.img(src=main_bg_url)

            with a.div(klass="mainframe"):
                with a.div(klass="mainframe-content"):
                    a.h1(_t="Bienvenue dans mon portefeuille")
                    a.p(_t="Je vous invite cordialement &agrave; consulter mes projets")
            # ABOUT ME
            with a.div(klass="about-me"):
                with a.div(klass="bio"):
                    with a.div(klass="bio-photo"):
                        a.img(src=about_me_img)
                    with a.div(klass="bio-content"):
                        a.h1(_t="Sur moi")
                        a.p(_t="Je m'appelle Aleksandra Grzelik. Je m'intéresse à la modélisation mathématique et statistique, en particulier pour les phénomènes dans le domaine de la psychologie, de l'écologie ou de la sociologie. J'ai terminé mes études à l'université de Lodz en juillet 2022 avec une licence en Économétrie et Analyse de Donnée, ma thèse portait sur l'analyse statistique du niveau de bonheur des étudiants. La thèse a été inspirée par une approche alternative (au produit intérieur brut) pour mesurer le bien-être d'une société : les mesures basées sur des facteurs tels que la protection de l'environnement ou la légalité. Sur la base de recherches, telles que le World Happiness Report, une mesure du bonheur et un modèle ont été préparés. Après une validation appropriée, le modèle a été utilisé pour identifier les variables les plus importantes qui déterminent le niveau de bonheur des étudiants. En octobre 2022, j'ai commencé une maîtrise en analyse de données (Université de Łódź). Pendant mes études, j'ai acquis des compétences en mathématiques et en intelligence artificielle et j'ai participé à de nombreux projets intéressants. Pour en savoir plus, consultez l'onglet 'Mes projets'.")
                with a.div(klass="exp"):
                    with a.div(klass="exp-educ"):
                        a.h2(_t="Education")
                        with a.ul(klass="exp-tiles"):
                            with a.li():
                                a.img(src="imgs/icons/ul-mi.png")
                                with a.span():
                                    a.h3(_t="l'Analyse des donnes")
                                    a.small(_t="Facult&eacute; de Mathematique et Informatique")
                                    a.small(_t="Universit&eacute; de Lodz")
                                    a.small(_t="ma&icirc;trise")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2022 - obecnie")
                            with a.li():
                                a.img(src="imgs/icons/ul-eksoc.jpg")
                                with a.span():
                                    a.h3(_t="Econometrie et l'Analyse des donnes")
                                    a.small(_t="Facult&eacute; de Economie et Sociologie")
                                    a.small(_t="Universit&eacute; de Lodz")
                                    a.small(_t="licence")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2019-2022")
                            with a.li():
                                a.img(src="imgs/icons/ul-fil.png")
                                with a.span():
                                    a.h3(_t="Philologie Romaine")
                                    a.small(_t="Facult&eacute; de Philologie")
                                    a.small(_t="Universit&eacute; de Lodz")
                                    a.small(_t="licence")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2019-2022")
                    with a.div(klass="exp-comp"):
                        a.h2(_t="Competences")
                        with a.ul(klass="comps"):
                            a.li(_t="formation théorique en statistique, mathématique, finance")
                            a.li(_t="programmation : mon langage préféré est Python")
                            a.li(_t="développement de modèles d'apprentissage automatique, de réseaux neuronaux")
                            a.li(_t="connaissance des techniques de vérification des modèles et des tests statistiques")
                            a.li(_t="capacité à interpréter et à rédiger des textes scientifiques")
                            a.li(_t="pensée analytique, mais aussi créativité")
                    with a.div(klass="exp-job"):
                        a.h2(_t="Exp&eacute;rience")
                        with a.ul(klass="exp-tiles"):
                            with a.li():
                                a.img(src="imgs/icons/acc.png")
                                with a.span():
                                    a.h3(_t="Application Developement Associate ")
                                    a.small(_t="Accenture Polska")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> septembre 2022 - pr&eacute;sent")
                            with a.li():
                                a.img(src=internship_icon)
                                with a.span():
                                    a.h3(_t="Stage")
                                    a.small(_t="La Pr&eacute;paration du Projet th&eacute;oretique optimisation des Google Ads")
                                    a.small(_t="Evillage.pl")
                                    a.p(_t="<i class=\"fa-regular fa-calendar\"></i> 2021 julliet - ao&ucirc;t")
                    with a.div(klass="exp-jezyki"):
                        a.h2(_t="Langues")
                        with a.ul(klass="langs"):
                            with a.li():
                                a.img(src="imgs/icons/pl.png")
                                a.p(_t="Polonais - la langue maternelle")
                            with a.li():
                                a.img(src="imgs/icons/eng.png")
                                a.p(_t="Anglais - niveau C1")
                            with a.li():
                                a.img(src="imgs/icons/fr.png")
                                a.p(_t="Fran&ccedil;ais - niveau B2")
                with a.div(klass="bio"):
                    with a.div(klass="bio-content", id="interests"):
                        a.h1(_t="Interests")
                        a.p(_t="J'aime le sport, je fais du roller, je pratique le step aerobics et parfois je choisis la gym. J'aime me promener, le plus souvent avec mes chiennes Rina et Ruby, c'est l'occasion de me détendre activement et de prendre contact avec la nature, ce qui est important pour moi. Je suis passionnée de lecture, bien que le temps manque toujours pour lire. Mes genres préférés sont la fiction, le reportage, la science populaire et le roman d'amour. Je mène un classement subjectif des livres que j'ai lus, en 2023, mes préférés étaient La physique de la mélancolie ( Guéorgui Gospodinov ) et Madame ( Antoni Libera ). Cette année, je participe à un défi de lecture - 40 livres - et je trace mes progrès sur <a href='https://www.goodreads.com/user/show/163587605-ola'>goodreads</a>.  ")
                    with a.div(klass="bio-photo"):
                        a.img(src=interests_img)
                with a.section(klass="projectBlog"):
                    with a.article():
                        a.h1(_t="Projets")
                        with a.a(klass="project", href="fr/projects/"+projects[-1]['permalink']+'.html'):
                            a.img(src=projects[-1]['img'])
                            with a.div():
                                a.h3(_t=projects[-1]['fr']['title'])
                                a.small(_t=projects[-1]['date'])
                                a.p(_t=projects[-1]['fr']['excerpt'])
                    with a.article():
                        a.h1(_t="Blog")
                        with a.a(klass="project", href="fr/blog/"+posts[-1]['permalink']+'.html'):
                            a.img(src=posts[-1]['imgUrl'])
                            with a.div():
                                a.h3(_t=posts[-1]['fr']['title'])
                                a.small(_t=posts[-1]['date'])
                                a.p(_t=posts[-1]['fr']['excerpt'])
                with a.div(klass="contact"):
                    a.h1(_t="Contactez-moi")
                    with a.div(klass="contact-wrap"):
                        with a.div(klass="contact-wrap-left"):
                            # with a.div(klass="contact-info"):
                            #     with a.p():
                            #         a.i(klass="fa-regular fa-envelope")
                            #         a("&nbsp;ola.grzelik.bno@gmail.com")
                            with a.div(klass="contact-links"):
                                with a.a(href="https://www.linkedin.com/in/aleksandra-grzelik-070291210?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app&fbclid=IwAR36g7HqOMaWRaIIc6dOUlOCUwKUVuVgH_zEZzSmF-seF1W-PBMWviSxEC0", target="_blank"):
                                    a.img(src="imgs/icons/linkedin.png")
                                    a.p(_t="LinkedIn")
                        with a.form():
                            a.h1(style="text-align:center", _t="Envoyez-moi un message")
                            a.label(_for="imie", _t="Votre nome:")
                            a.input(type="text", id="imie", name="imie")
                            a.label(_for="email", _t="Votre adresse email:")
                            a.input(type="email", id="email", name="email")
                            a.label(_for="tresc", _t="Message:")
                            a.textarea(id="tresc")
                            a.input(id="submit", onclick="sendMail()", value="Envoyer &gt;")

            # FOOTER
            components.footer(a, "fr")
    f = codecs.open("fr.html", "w", "utf-8")
    f.write(str(a))
    f.close()


def populate_landing_pages():
    generate_landing_page()
    print("Succesfully generated the landing pages.")