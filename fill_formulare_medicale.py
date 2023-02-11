from os.path import join

import docx
from docxtpl import DocxTemplate
from docx.shared import Pt

from docx import Document

FILLED_DOCUMENT = "filled_formulare_medcale_foaie_observatie_clinica_generala.docx"
PARAMETERIZED_DOCUMENT = 'formulare_medicale_foaie_observatie_clinica_generala_w_fields.docx'
SIZE_CNP = 13

def write_new_document(context):
    doc = DocxTemplate(PARAMETERIZED_DOCUMENT)
    doc.render(context)
    doc.save(FILLED_DOCUMENT)

def create_context(first_name, last_name, personal_id_no):
    context= {'nume_observatie': last_name, 'prenume_observatie': first_name}

    for digit_no in range(SIZE_CNP):
        field = 'CNP_' + str(digit_no) + '_observatie'
        context[field] = personal_id_no[digit_no]

    return context

def fill_document(first_name, last_name, personal_id_no):
    context = create_context(first_name, last_name, personal_id_no)
    write_new_document(context)

# if __name__ == "__main__":
#     name="Petruc"
#     first_name="Rares"
#
#     context = {
#        'nume_observatie': name,
#        'prenume_observatie': first_name,
#        'CNP_0_observatie': 1,
#        'CNP_1_observatie': 2,
#        'CNP_2_observatie': 3,
#        'CNP_3_observatie': 4,
#        'CNP_4_observatie': 5,
#        'CNP_5_observatie': 6,
#        'CNP_6_observatie': 7,
#        'CNP_7_observatie': 8,
#        'CNP_8_observatie': 9,
#        'CNP_9_observatie': 1,
#        'CNP_10_observatie': 2,
#        'CNP_11_observatie': 3,
#        'CNP_12_observatie': 4,
#        'CNP_13_observatie': 5
#      }
