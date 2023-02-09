class CulturePost:

    def __init__(self, text: str, additional_btn: str = None, url: str = None):
        self.text = text
        self.additional_btn = additional_btn
        self.url = url

    def toString(self):
        return f"CulturePost: {self.text}, {self.additional_btn}"
