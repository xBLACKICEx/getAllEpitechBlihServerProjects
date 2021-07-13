#!/usr/bin/python3

import os
import re
import shutil
from pathlib import Path


def cloneProject(email: str, projectName: str):
    os.system('git clone git@git.epitech.eu:/' + email + '/' + projectName)


def getProjectList(epitechEmail):
    stream = os.popen('./Dependencies/blih -u ' + epitechEmail + ' repository list')
    return stream.read().splitlines()


def manageFolder(project):
    matchYears = re.search(r'(19|20)\d{2}$', project)
    matchFrench = re.search(r'^B', project)

    if matchYears:
        year = matchYears.group()
        Path("EpitechProjects/" + year).mkdir(parents=True, exist_ok=True)
        matchCatagorys = re.search(r'^[A-z].*?_', project)
        matchMath = re.search(r'^[0-9]{3}', project)

        if matchCatagorys:
            catagory = matchCatagorys.group().replace("_", "")
            Path("EpitechProjects/" + year + "/" + catagory).mkdir(parents = True, exist_ok = True)
            shutil.move(project, "EpitechProjects/" + year + "/" + catagory)
        elif matchMath:
            math = "MTH"
            Path("EpitechProjects/" + year + "/" + math).mkdir(parents = True, exist_ok = True)
            shutil.move(project, "EpitechProjects/" + year + "/" + math)
        else:
            Path("EpitechProjects/" + year + "/other").mkdir(parents = True, exist_ok = True)
            shutil.move(project, "EpitechProjects/" + year + "/other")
    elif matchFrench:
        french = "FR"
        Path("EpitechProjects/" + french).mkdir(parents = True, exist_ok = True)
        shutil.move(project, "EpitechProjects/" + "FR")
    else:
        Path("EpitechProjects/other").mkdir(parents = True, exist_ok = True)
        shutil.move(project, "EpitechProjects/other")


if __name__ == '__main__':
    epitechEmail = input("you epitech email: ")
    projectList = getProjectList(epitechEmail)

    Path("EpitechProjects").mkdir(parents=True, exist_ok=True)

    for project in projectList:
        cloneProject(epitechEmail, project)
        manageFolder(project)
