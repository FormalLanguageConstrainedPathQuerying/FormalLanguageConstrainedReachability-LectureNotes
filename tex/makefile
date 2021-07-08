main=FormalLanguageConstrainedReachabilityLectureNotes

all: 
	pdflatex $(main).tex
	bibtex $(main).aux
	pdflatex $(main).tex

clean:
	rm -f $(main).pdf *.log *.aux *.bbl *.blg *.out *.toc *~
