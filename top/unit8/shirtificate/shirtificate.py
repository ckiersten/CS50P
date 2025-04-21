from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        super().add_page()
        super().set_auto_page_break(False)
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def make_header(self):
        super().set_y(30)
        super().set_text_color(0, 0, 0)
        super().set_font("Helvetica", size=50)
        super().cell(None, None, "CS50 Shirtificate", align="C", center=True)

    def make_visuals(self):
        super().image("shirtificate.png", "C", 80, 180, 200, keep_aspect_ratio=True)
        super().set_y(150)
        super().set_text_color(255, 255, 255)
        super().set_font("Helvetica", size=20)
        super().cell(None, None, self.name+" took CS50", align="C", center=True)


    def make_pdf(self):
        self.make_header()
        self.make_visuals()


def main():
    name = input("Name: ")
    shirt = PDF(name)
    shirt.make_pdf()
    shirt.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

