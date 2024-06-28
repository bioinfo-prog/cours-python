SOURCE_ACTIVATE=. ../venv/bin/activate

tk: 20_tkinter.md ../template.latex
	$(SOURCE_ACTIVATE) && \
	pandoc -o tk_tmp.tex  \
		-S --toc \
		-M links-as-notes \
		--filter pandoc-fignos \
		--template="../template.latex" \
		20_tkinter.md
	bash ../make-boxes.sh
	pdflatex tk_tmp.tex tk_tmp.pdf

tkclean:
	rm -rf tk_tmp.*

fct: 09_fonctions.md ../template.latex
	$(SOURCE_ACTIVATE) && \
	pandoc -o fct_tmp.tex  \
		-S --toc \
		-M links-as-notes \
		--filter pandoc-fignos \
		--template="../template.latex" \
		09_fonctions.md
	bash ../make-boxes.sh
	pdflatex fct_tmp.tex fct_tmp.pdf

fctclean:
	rm -rf fct_tmp.*

pep: 15_bonnes_pratiques.md ../template.latex
	$(SOURCE_ACTIVATE) && \
	pandoc -o pep_tmp.tex  \
		-S --toc \
		-M links-as-notes \
		--filter pandoc-fignos \
		--template="../template.latex" \
		15_bonnes_pratiques.md
	bash ../make-boxes.sh
	pdflatex pep_tmp.tex pep_tmp.pdf

pepclean:
	rm -rf pep_tmp.*

annexinst: annexe_install_python.md ../template.latex
	$(SOURCE_ACTIVATE) && \
	pandoc -o annexinst_tmp.tex  \
		-S --toc \
		-M links-as-notes \
		--filter pandoc-fignos \
		--template="../template.latex" \
		annexe_install_python.md
	bash ../make-boxes.sh
	pdflatex annexinst_tmp.tex annexinst_tmp.pdf

annexinstclean:
	rm -rf annexinst_tmp.*

class: 19_avoir_la_classe_avec_les_objets.md ../template.latex
	$(SOURCE_ACTIVATE) && \
	pandoc -o class_tmp.tex  \
		-S --toc \
		-M links-as-notes \
		--filter pandoc-fignos \
		--template="../template.latex" \
		19_avoir_la_classe_avec_les_objets.md
	bash ../make-boxes.sh
	pdflatex class_tmp.tex class_tmp.pdf

classclean:
	rm -rf class_tmp.*

projpap: 22_mini_projets_pas_a_pas.md ../template.latex
	$(SOURCE_ACTIVATE) && \
	pandoc -o projpap.tex  \
		-S --toc \
		-M links-as-notes \
		--filter pandoc-fignos \
		--template="../template.latex" \
		22_mini_projets_pas_a_pas.md
	pdflatex projpap.tex projpap.pdf

projpap_clean:
	rm -rf tk_tmp.*
