# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import components
import json
from airium import Airium

with codecs.open('projects.json', 'r', 'utf-8') as file:
    projects = json.load(file)

def generate_project(project):
    # HTML META DATA
    icon_url = "/favicon.ico"
    apple_icon_url = "/apple-touch-icon.png"
    # DATE
    date = project['date']
    # FILENAME
    filename = project['permalink']
    # PERMALINKS
    pl_permalink = f'/projects/{filename}.html'
    eng_permalink = f'/eng/projects/{filename}.html'
    fr_permalink = f'/fr/projects/{filename}.html'
    # IMG URL
    img_url = project['img']
    # TITLES
    pl_title = project['pl']['title']
    eng_title = project['eng']['title']
    fr_title = project['fr']['title']
    # EXCERPTS
    pl_excerpt = project['pl']['excerpt']
    eng_excerpt = project['eng']['excerpt']
    fr_excerpt = project['fr']['excerpt']
    # CONTENT 
    pl_content = project['pl']['content']
    eng_content = project['eng']['content']
    fr_content = project['fr']['content']
    # LINKS
    links = []
    for link in project['links']:
        links.append(link)

    # POLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        components.head(a, "pl", pl_title, pl_excerpt, pl_permalink, img_url, icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "pl", pl_permalink, eng_permalink, fr_permalink)
            # CONTENT
            with a.div(klass="contentWrapper  projectWrapper"):
                with a.article(klass="singleProject"):
                    with a.header():
                        with a.div(klass="metaData"):
                            a.h1(_t=pl_title)
                            a.h4(_t=date)
                            if(len(links) > 0):
                                for link in links:
                                    with a.a(_t=link['name_pl'], href=link['url'], target="_blank"):
                                        a.i(klass="fa-solid fa-arrow-up-right-from-square")
                        if (img_url != ""):
                            with a.figure(klass="mainPhoto"):
                                a.img(src="../"+img_url)
                    with a.section(klass="content"): a(pl_content)
            # FOOTER
            components.footer(a, "pl")
    f = codecs.open("projects/"+filename+".html", "w", 'utf-8')
    f.write(str(a))
    f.close()

     # ENGLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="e"):
        components.head(a, "en", eng_title, eng_excerpt, eng_permalink, img_url, icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "en", pl_permalink, eng_permalink, fr_permalink)
            # CONTENT
            with a.div(klass="contentWrapper  projectWrapper"):
                with a.article(klass="singleProject"):
                    with a.header():
                        with a.div(klass="metaData"):
                            a.h1(_t=eng_title)
                            a.h4(_t=date)
                            if(len(links) > 0):
                                for link in links:
                                    with a.a(_t=link['name_eng'], href=link['url'], target="_blank"):
                                        a.i(klass="fa-solid fa-arrow-up-right-from-square")
                        if (img_url != ""):
                            with a.figure(klass="mainPhoto"):
                                a.img(src="../../"+img_url)
                    with a.section(klass="content"): a(eng_content)
            # FOOTER
            components.footer(a, "en")
    f = codecs.open("eng/projects/"+filename+".html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    # FRENCH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="fr"):
        components.head(a, "fr", fr_title, fr_excerpt, fr_permalink, img_url, icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "fr", pl_permalink, eng_permalink, fr_permalink)
            # CONTENT
            with a.div(klass="contentWrapper projectWrapper"):
                with a.article(klass="singleProject"):
                    with a.header():
                        with a.div(klass="metaData"):
                            a.h1(_t=fr_title)
                            a.h4(_t=date)
                            if(len(links) > 0):
                                for link in links:
                                    with a.a(_t=link['name_fr'], href=link['url'], target="_blank"):
                                        a.i(klass="fa-solid fa-arrow-up-right-from-square")
                        if (img_url != ""):
                            with a.figure(klass="mainPhoto"):
                                a.img(src="../../"+img_url)
                    with a.section(klass="content"): a(fr_content)
            # FOOTER
            components.footer(a, "fr")
    f = codecs.open("fr/projects/"+filename+".html", "w", 'utf-8')
    f.write(str(a))
    f.close()


def generate_project_page():
    # VARIABLES
    site_title_pl = "Projekty - Aleksandra Grzelik"
    site_description_pl = "Aleksandra Grzelik - projekty naukowe, akademickie, granty."
    site_title_eng = "Projects - Aleksandra Grzelik"
    site_description_eng = "Aleksandra Grzelik - scientific and academic projects, grants."
    site_title_fr = "Projets - Aleksandra Grzelik"
    site_description_fr = "Projekty - Aleksandra Grzelik"
    # HTML META DATA
    icon_url = "/favicon.ico"
    apple_icon_url = "/apple-touch-icon.png"

    # POLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        components.head(a, "pl", site_title_pl, site_description_pl, "/projects.html", "", icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "pl", "/projects.html", "/eng/projects.html", "/fr/projects.html")
            # CONTENT
            with a.div(klass="contentWrapper projectWrapper"):
                a.h1(_t="Projekty")
                with a.section(klass="projects"):
                    for project in projects:
                        with a.a(klass="projectPreview", href="/projects/"+project['permalink']+".html"):
                            if (project['img'] != ""):
                                a.img(src=project['img'])
                            with a.div(klass="desc"):
                                a.h3(_t=project['pl']['title'])
                                a.small(_t=project['date'])
                                a.p(_t=project['pl']['excerpt'])
            # FOOTER
            components.footer(a, "pl")
    f = codecs.open("projects.html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    # ENGLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        components.head(a, "en", site_title_eng, site_description_eng, "/eng/projects.html", "", icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "en", "/projects.html", "/eng/projects.html", "/fr/projects.html")
            # CONTENT
            with a.div(klass="contentWrapper  projectWrapper"):
                a.h1(_t="Projects")
                with a.section(klass="projects"):
                    for project in projects:
                        with a.a(klass="projectPreview", href="/eng/projects/"+project['permalink']+".html"):
                            if (project['img'] != ""):
                                a.img(src="../"+project['img'])
                            with a.div(klass="desc"):
                                a.h3(_t=project['eng']['title'])
                                a.small(_t=project['date'])
                                a.p(_t=project['eng']['excerpt'])
            # FOOTER
            components.footer(a, "en")
    f = codecs.open("eng/projects.html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    # ENGLISH HTML    
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="fr"):
        components.head(a, "fr", site_title_fr, site_description_fr, "/fr/projects.html", "", icon_url, apple_icon_url)
        with a.body(onload="preloader()"):
            components.navbar(a, "fr", "/projects.html", "/eng/projects.html", "/fr/projects.html")
            # CONTENT
            with a.div(klass="contentWrapper projectWrapper"):
                a.h1(_t="Projets:")
                with a.section(klass="projects"):
                    for project in projects:
                        with a.a(klass="projectPreview", href="/fr/projects/"+project['permalink']+".html"):
                            if (project['img'] != ""):
                                a.img(src="../"+project['img'])
                            with a.div(klass="desc"):
                                a.h3(_t=project['fr']['title'])
                                a.small(_t=project['date'])
                                a.p(_t=project['fr']['excerpt'])
            # FOOTER
            components.footer(a, "fr")
    f = codecs.open("fr/projects.html", "w", 'utf-8')
    f.write(str(a))
    f.close()

    return


def populate_projects():
    for project in projects:
        generate_project(project)
    generate_project_page()
    print(f"Succesfully generated {len(projects)} projects.")