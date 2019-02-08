from modules.filterer import Filterer

# Init Main Settings
settings = {
    "domains_path": "input/domains.txt",
    "keywords_path": "input/keywords.txt",
}

filterer_instance = Filterer(settings)

filterer_instance.run()


