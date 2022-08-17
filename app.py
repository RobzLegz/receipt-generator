from fpdf import FPDF

invoiceData = {
    "nr": "1",
    "date": "04.05.2022",
    "name": "Roberts",
    "surname": "Legzdins",
}

class PDF(FPDF):
    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('courier', 'I', 8)
        # Page number
        self.cell(0, 10, f'Apmaksats ar karti', align='C')

# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

#Add Page
pdf.add_page()

# specify font
pdf.set_font('helvetica', '', 20)
pdf.cell(40, 20, "Ceks")
pdf.set_font('helvetica', '', 25)
pdf.cell(240, 20, "Seru vainagi", align="C")

pdf.set_font('helvetica', '', 16)
pdf.cell(40, 40, "Pasutijuma Nr.")
# pdf.cell(40, 40, invoiceData['nr'])

pdf.cell(40, 60, "Datums")
pdf.cell(40, 60, invoiceData['date'])


pdf.output('output.pdf')