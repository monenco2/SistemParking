from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Panorama Laboral en Programación de Software - Colombia", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, body)
        self.ln()

    def add_word_puzzle(self, puzzle):
        self.set_font("Courier", "", 9)
        for line in puzzle:
            self.cell(0, 5, line, ln=True)
        self.ln()

    def add_list(self, items):
        self.set_font("Arial", "", 10)
        for item in items:
            self.cell(0, 5, f"- {item}", ln=True)
        self.ln()

pdf = PDF()
pdf.add_page()

intro_text = (
    "En Colombia, la técnica en programación de software es una de las más demandadas por el mercado laboral. "
    "Las oportunidades incluyen el trabajo remoto, el desarrollo de software para empresas extranjeras, y el "
    "emprendimiento digital. Sin embargo, también existen retos como el dominio del inglés, la actualización "
    "constante en tecnologías y la informalidad laboral. El país está impulsando el crecimiento del sector tecnológico "
    "con iniciativas como Misión TIC. Las habilidades blandas, el conocimiento de frameworks y la creación de un "
    "portafolio son claves para el éxito laboral."
)
pdf.chapter_title("Texto Base")
pdf.chapter_body(intro_text)

pdf.chapter_title("Sopa de Letras – 'Panorama Laboral Tech'")
sopa_words = [
    "PROGRAMACIÓN", "TECNOLOGÍA", "INGLÉS", "ACTUALIZACIÓN", "FREELANCE",
    "EMPRENDIMIENTO", "MISIONTIC", "FRAMEWORK", "PORTAFOLIO", "EMPLEO",
    "TRABAJO", "RETOS", "OPORTUNIDADES", "HABILIDADES", "INFORMALIDAD"
]
pdf.chapter_body("Busca las siguientes palabras:")
pdf.add_list(sopa_words)

sopa_puzzle = [
    "P R O G R A M A C I Ó N",
    "O B M E R C A D O R E T",
    "R T I C N O I C A Z A L",
    "T M A C T U A L I Z A C",
    "A I N G L É S T R O F M",
    "F F R A M E W O R K N I",
    "O I N F O R M A L I D A",
    "L D E S A R R O L L O M",
    "I T A R A B A J O F C E",
    "O I E M P R E N D I M I",
    "P O R T A F O L I O T D",
    "E O P O R T U N I D A D",
    "M M I S I O N T I C O X"
]
pdf.add_word_puzzle(sopa_puzzle)

pdf.chapter_title("Crucigrama – 'Retos y Oportunidades en Programación'")
crucigrama_definiciones = [
    "Horizontales:",
    "1. Sector en crecimiento que impulsa la demanda de programadores.",
    "3. Actividad que consiste en crear proyectos propios, como apps o startups.",
    "5. Herramienta digital donde muestras tus proyectos y habilidades.",
    "6. Plataforma nacional que impulsa el aprendizaje de programación en Colombia.",
    "8. Es necesario dominar este idioma para acceder a mejores oportunidades.",
    "",
    "Verticales:",
    "2. Práctica laboral común pero sin contrato formal.",
    "4. Forma de trabajo independiente, común entre programadores.",
    "7. Habilidad clave además del conocimiento técnico.",
    "9. Necesario para mantenerse vigente en un mercado cambiante."
]
pdf.add_list(crucigrama_definiciones)
pdf.chapter_body("Palabras clave: TECNOLOGÍA, INFORMALIDAD, EMPRENDIMIENTO, FREELANCE, PORTAFOLIO, "
                 "MISIONTIC, HABILIDADES, INGLÉS, ACTUALIZACIÓN.")

pd
