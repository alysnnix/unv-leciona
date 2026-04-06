SHARED     := $(CURDIR)/shared
TEXINPUTS  := $(SHARED)//:

# Documentos disponíveis
DOCS := company-authorization-term partial-report

# ── Build ────────────────────────────────────────────────────────────────────

## Compila um documento: make build DOC=company-authorization-term
build:
	@test -n "$(DOC)" || { echo "Uso: make build DOC=<nome>"; exit 1; }
	@mkdir -p $(DOC)/build
	cd $(DOC) && TEXINPUTS="$(TEXINPUTS)" pdflatex -synctex=1 -interaction=nonstopmode \
		-output-directory=build main.tex
	cd $(DOC) && TEXINPUTS="$(TEXINPUTS)" pdflatex -synctex=1 -interaction=nonstopmode \
		-output-directory=build main.tex
	@echo "PDF: $(DOC)/build/main.pdf"

## Compila todos os documentos
all:
	@for doc in $(DOCS); do \
		echo "── Compilando $$doc ──"; \
		$(MAKE) build DOC=$$doc; \
	done

## Compila e copia o PDF final para entregues/ com nome legível
entrega:
	@test -n "$(DOC)" || { echo "Uso: make entrega DOC=<nome>"; exit 1; }
	@test -n "$(NUM)" || { echo "Uso: make entrega DOC=<nome> NUM=004"; exit 1; }
	@test -n "$(TITULO)" || { echo "Uso: make entrega DOC=<nome> NUM=004 TITULO='Termo de Autorizacao'"; exit 1; }
	$(MAKE) build DOC=$(DOC)
	@mkdir -p entregues
	cp $(DOC)/build/main.pdf "entregues/$(NUM) - $(TITULO).pdf"
	@echo "Entrega: entregues/$(NUM) - $(TITULO).pdf"

## Limpa artefatos de build
clean:
	find . -path '*/build/*' ! -name '.gitkeep' -type f -delete

.PHONY: build all entrega clean
