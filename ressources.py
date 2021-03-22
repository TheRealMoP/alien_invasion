class Ressources():
    """Loads and manages ressources"""
    
    def __init__(self):
        # Pathes
        self.PATH_HINT = "ressources/hints.txt"

        # Objects
        self.hints = self.load_lines(self.PATH_HINT)
        
    def load_lines(self, path):
        with open(path) as file:
            return file.readlines()

    def print_file_content(self):
        with open(self.PATH_HINT) as file:
            print(file.read())