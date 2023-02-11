<h2> IDEA </h2>

A friend of mine, resident doctor, complained to me about continuous need to fill a *clinical observation form*, which
also has **repetitive fields** in different pages (e.g.: "Numele" (Name) is requested on page 1, but also on page 9).

<h2> DONE STEPS </h2>

<ol>
<li> Got the clinical observation form from: <a href="http://www.spitalbt-sfgheorghe.ro/Legislatie/Foaia-de-observatie/formulare_medicale_foaie_observatie_clinica_generala.pdf">Link Clinical Form</a></li>
<li> Used <a href="https://www.zamzar.com/convert/docx-to-pdf/">ZAMZAR</a> for <b>conversion</b> from <b>pdf</b> to <b>docx</b></li>
<li> Added text boxes to the generated docx, containing placeholders, like <b>{{nume_observatie}}</b>, <b>{{CNP_0_observatie}}</b> which are used both in pages 1 and 9 of the document <b>formulare_medicale_foaie_observatie_clinica_generala_w_fields.docx</b></li>
<li> Developed a simple script (<b>fill_formulare_medicale.py</b>) that <i>replaces</i> these placeholders with the desired data</li>
</ol>

<h2> TODO STEPS </h2>
❌ Simple GUI asking user to input first & last name, and also the Personal Identification Number (CNP in romanian)

❌ Formatting of the input of the user and building the dictionary using the information provided, followed by launching the script of filling the form

❌ Add new repetitive fields

❌ Modify size of the font for the fields ([USEFUL](https://stackoverflow.com/questions/36888189/python-docx-paragraph-in-textbox))
