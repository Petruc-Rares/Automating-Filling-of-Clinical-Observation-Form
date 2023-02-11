from os.path import join

import docx
from docxtpl import DocxTemplate
from docx.shared import Pt

from docx import Document

if __name__ == "__main__":
    doc = DocxTemplate('formulare_medicale_foaie_observatie_clinica_generala_w_fields.docx')

    name="Petruc"
    first_name="Rares"

    context = {
       'nume_observatie': name,
       'prenume_observatie': first_name,
       'CNP_0_observatie': 1,
       'CNP_1_observatie': 2,
       'CNP_2_observatie': 3,
       'CNP_3_observatie': 4,
       'CNP_4_observatie': 5,
       'CNP_5_observatie': 6,
       'CNP_6_observatie': 7,
       'CNP_7_observatie': 8,
       'CNP_8_observatie': 9,
       'CNP_9_observatie': 1,
       'CNP_10_observatie': 2,
       'CNP_11_observatie': 3,
       'CNP_12_observatie': 4,
       'CNP_13_observatie': 5
     }

    doc.render(context)
    doc.save("filled_formulare_medcale_foaie_observatie_clinica_generala.docx")

