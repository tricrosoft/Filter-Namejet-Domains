import time


class Filterer(object):

    def __init__(self, settings):
        self.domains_path = settings["domains_path"]
        self.keywords_path = settings["keywords_path"]
        self.filename = self.generate_filename()
        self.keywords = []

    def generate_filename(self):
        return str(time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime()) + " - Extracted Domains")

    def load(self, path):

        load_result = []

        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                load_result.append(line.strip())

        return load_result

    def create_file(self, data):

        file_path = "output/" + self.generate_filename() + ".txt"

        open(file_path, "w+", encoding="utf-8")

        with open(file_path, "a", encoding="utf-8") as file:
            for el in data:
                file.write(el + "\n")

        return True

    def run(self):

        keywords = self.load(self.keywords_path)
        domains = self.load(self.domains_path)

        run_result = []

        

        for domain in domains:
            for keyword in keywords:
                if (keyword in domain):
                    run_result.append(domain)

        # print(run_result)

        if(self.create_file(run_result)):
            print("Run Successful - Check output folder")
