from urllib import request
import tomllib as toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_content: dict = toml.loads(content)
        name = toml_content.get("tool").get("poetry").get("name")
        desc = toml_content.get("tool").get("poetry").get("description")
        dep = toml_content.get("tool").get("poetry").get("dependencies")
        dep_dev = toml_content.get("tool").get("poetry").get("group").get("dev").get("dependencies")
        
        license = toml_content.get("tool").get("poetry").get("license")
        authors = toml_content.get("tool").get("poetry").get("authors")
        
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dep, dep_dev, license, authors)
