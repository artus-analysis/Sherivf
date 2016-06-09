#!/bin/bash


. @SHERIVFDIR@/scripts/ini_sherivf.sh


# run xfitter
echo -e "\nFit:"
xfitter
xfitter-draw --3panels --ratio-to-theory --bands --relative-errors hera/
mv hera/plots.pdf .

cd hera/
echo -e "\n\nErrorType:"
grep ErrorType hf_pdf/hf_pdf.info -n
sed -i 's/replicas/hessian/g' hf_pdf/hf_pdf.info

# evaluate PDFs
for q in 1.9 10.0 91.2; do
	for squared in "" "--q2"; do
		pdf_2_root.py -p hf_pdf -q ${q} ${squared}
	done
done
mv *.root fittedresults.txt Results.txt minuit.out.txt ..
cd ..

exit 0
