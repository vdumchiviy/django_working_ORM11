
class SlugConverter():
    regex = r"(\w*-*)+"

    def to_python(self, value):
        return value

    def to_url(self, value):
        pass
