# -*- coding: utf-8 -*-

import json
from airium import Airium
import generateposts
import generateprojects
import generatelandingpages
import shutil
import os
from datetime import datetime
import cleardir

# CREATE BACKUP OF JSON FILES
date_time = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
backup_directory = f'backup/{date_time}'
os.makedirs(backup_directory)
shutil.copy('projects.json', f'{backup_directory}/projects.json')
shutil.copy('posts.json', f'{backup_directory}/posts.json')
print("Succesfully created backup of json files.")

# CLEAR DIRECTORIES
directories_to_clear = ["blog/", "projects/", "eng/blog/", "eng/projects", "fr/blog", "fr/projects"]
for dir in directories_to_clear:
    cleardir.clear_directory(dir)
print("Directories cleared successfully!")

# GENERATE LANDING PAGES
generatelandingpages.populate_landing_pages()
# GENERATE POSTS
generateposts.populate_posts() 
# GENERATE PROJECTS
generateprojects.populate_projects()