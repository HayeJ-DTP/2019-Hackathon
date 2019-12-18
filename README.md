# 2019-Hackathon
GitHub repository for the 2019 Bioinformatics assessment

This project was "Developing a tool to identify and remove population variants out of NGS read alignments" through the use of a python script


Usage: Pileup2variant.py INPUT.pileup OUTPUTname %variantCutoff SAMdepth.csv

 

It was ran using a bash script:

#Generate variant files and depth plot
	
if [ -z "$PerformVA" ]; then
	
       echo "Skip variant analysis"
	
       echo "Variant analysis skipped" >> "$NEW_BAM_PATH"/"$refname"_BAM_stats_and_Options.txt
	
else
	
       echo "Will perform Variant analysis"
	
       echo "Performed variant analysis. -v option given as "$PerformVA"% variant threshold" >> "$NEW_BAM_PATH"/"$refname"_BAM_stats_and_Options.txt
	
       echo "Performed variant analysis using "$BAM"" >> "$NEW_BAM_PATH"/"$refname"_BAM_stats_and_Options.txt
	
       mkdir "$refname"_variant_analysis
	
       cd "$refname"_variant_analysis
	
       samtools mpileup -d 0 -Q 0 -AEf "$REF" "$BAM" > "$refname"_REFBAM.pileup
	
       #Issue with mpileup depth limit; -d 0 removes the limit but then the depth plot looks weird, needs investigating.
	
       samtools depth -d 0 -a "$BAM" > SAMdepth_"$refname".csv
	
       Pileup2variant.py "$refname"_REFBAM.pileup "$refname" "$PerformVA" SAMdepth_"$refname".csv

 
