#!/usr/bin/env python3
#Usage: Pileup2variant.py [INPUT.pileup] [NameOfOuput] [Variant % cut off] [SAMdepth.csv]

# Name: Pileup2variant.py
# Created by: Holly Everest - holly.everest@hertford.ox.ac.uk; Jack Hayes - jack.hayes@st-hughs.ox.ac.uk
# Special thanks to Dr Dorey-Robinson
# Date: 16 Dec 2019

"""
---------------------------------------------------------------------------------------------------------

#### G E N E R A L   D E S C R I P T I O N ####:

#A tool to read, identify, and remove population variants from NGS read alignments from a chosen input file. The tool allows for the input of sequences from any .fasta file, enabling the user to easily, and quickly, download and analyse sequence data from sites such as NCBI.

"""
"""
---------------------------------------------------------------------------------------------------------
"""
import sys

print("Hello world!")
#test line to ensure the program has launched properly, also assures the user of this

bases = {'A': ['A'], 'C': ['C'], 'B': ['C', 'G', 'T'], 'D': ['A', 'G', 'T'], 'G': ['G'], 'H': ['A','C', 'T'], 'K': ['G', 'T'], 'M': ['A', 'C'], 'N': ['G', 'A', 'T', 'C'], 'S': ['C', 'G'], 'R': ['A', 'G'], 'T': ['T'], 'W': ['A', 'T'], 'V': ['A', 'C', 'G'], 'Y': ['C', 'T']}
#dictionary of "acceptable" bases, will alert the user if the input file contains erroneous data that is not from this list

input_file = sys.argv[1]
output_file = sys.argv[2]
min_percent = float(sys.argv[3])
Total_Depth = sys.argv[4]
lines = open(input_file).readlines()
#using sys.argv to recieve and process the different sets of information from the file
#Usage: Pileup2variant.py INPUT.pileup OUTPUTname %variantCutoff SAMdepth.csv

variant_lines = []
depth_lines = []
Coverage_file = []
variant_depth = []

# Variant analysis using th empileup file
for line in lines [0:]:
                f = line.split()
                ref_matchF = f[4].count(".")
                ref_matchR = f[4].count(",")
                #print(ref_matchF)
                #print(ref_matchR)
                ref_match = [float(ref_matchF)] + [float(ref_matchR)]
                total_matches = sum(ref_match)
                Depth = f[3]
                ref_base = f[2]
                locus = f[1]
                Subject = f[0]
                #print(f[2])

                if ref_base == "A" or ref_base == "a":
                                A_total = (str(total_matches))                   
                                C_baseF = f[4].count("C")
                                C_baseR = f[4].count("c")
                                C_float = [float(C_baseF)] + [float(C_baseR)]
                                C_sum = sum(C_float)
                                C_total = (str(C_sum))                             
                                G_baseF = f[4].count("G")
                                G_baseR = f[4].count("g")
                                G_float = [float(G_baseF)] + [float(G_baseR)]
                                G_sum = sum(G_float)
                                G_total = (str(G_sum))                            
                                T_baseF = f[4].count("T")
                                T_baseR = f[4].count("t")
                                T_float = [float(T_baseF)] + [float(T_baseR)]
                                T_sum = sum(T_float)
                                T_total = (str(T_sum))                              
                                                             
                elif ref_base == "G" or ref_base == "g":
                                G_total = (str(total_matches))                              
                                A_baseF = f[4].count("A")
                                A_baseR = f[4].count("a")
                                A_float = [float(A_baseF)] + [float(A_baseR)]
                                A_sum = sum(A_float)
                                A_total = (str(A_sum))                              
                                C_baseF = f[4].count("C")
                                C_baseR = f[4].count("c")
                                C_float = [float(C_baseF)] + [float(C_baseR)]
                                C_sum = sum(C_float)
                                C_total = (str(C_sum))                              
                                T_baseF = f[4].count("T")
                                T_baseR = f[4].count("t")
                                T_float = [float(T_baseF)] + [float(T_baseR)]
                                T_sum = sum(T_float)
                                T_total = (str(T_sum))

                                                                                                               

                elif ref_base == "C" or ref_base == "c":
                                C_total = (str(total_matches))                              
                                A_baseF = f[4].count("A")
                                A_baseR = f[4].count("a")
                                A_float = [float(A_baseF)] + [float(A_baseR)]
                                A_sum = sum(A_float)
                                A_total = (str(A_sum))                              
                                G_baseF = f[4].count("G")
                                G_baseR = f[4].count("g")
                                G_float = [float(G_baseF)] + [float(G_baseR)]
                                G_sum = sum(G_float)
                                G_total = (str(G_sum))                              
                                T_baseF = f[4].count("T")
                                T_baseR = f[4].count("t")
                                T_float = [float(T_baseF)] + [float(T_baseR)]
                                T_sum = sum(T_float)
                                T_total = (str(T_sum))
                             
                elif ref_base == "T" or ref_base == "t":
                                T_total = (str(total_matches))                              
                                C_baseF = f[4].count("C")
                                C_baseR = f[4].count("c")
                                C_float = [float(C_baseF)] + [float(C_baseR)]
                                C_sum = sum(C_float)
                                C_total = (str(C_sum))                             
                                G_baseF = f[4].count("G")
                                G_baseR = f[4].count("g")
                                G_float = [float(G_baseF)] + [float(G_baseR)]
                                G_sum = sum(G_float)
                                G_total = (str(G_sum))                              
                                A_baseF = f[4].count("A")
                                A_baseR = f[4].count("a")
                                A_float = [float(A_baseF)] + [float(A_baseR)]
                                A_sum = sum(A_float)
                                A_total = (str(A_sum))                

                else:
                                total_matches = "0"                                                     
                                C_baseF = f[4].count("C")
                                C_baseR = f[4].count("c")
                                C_float = [float(C_baseF)] + [float(C_baseR)]
                                C_sum = sum(C_float)
                                C_total = (str(C_sum))                              
                                G_baseF = f[4].count("G")
                                G_baseR = f[4].count("g")
                                G_float = [float(G_baseF)] + [float(G_baseR)]
                                G_sum = sum(G_float)
                                G_total = (str(G_sum))                              
                                A_baseF = f[4].count("A")
                                A_baseR = f[4].count("a")
                                A_float = [float(A_baseF)] + [float(A_baseR)]
                                A_sum = sum(A_float)
                                A_total = (str(A_sum))              
                                T_baseF = f[4].count("T")
                                T_baseR = f[4].count("t")
                                T_float = [float(T_baseF)] + [float(T_baseR)]
                                T_sum = sum(T_float)
                                T_total = (str(T_sum))                            
              
                Ins_count = f[4].count("+")
                Ins = (str(Ins_count))
                Del_count = f[4].count("-")
                Del = (str(Del_count))
                              
                new_line = Subject + "\t" + locus + "\t" + ref_base + "\t" + Depth + "\t" + A_total + "\t" + G_total + "\t" + C_total + "\t" + T_total + "\t" + Ins + "\t" + Del
                depth_lines.append(new_line)
                print(new_line)
              
                coverage = locus + "\t" + Depth
                Coverage_file.append(coverage)
               
                Depth_float = float(Depth)
                Ref_matches = float(total_matches)
                pc_not_matching_ref = 100 - (100*Ref_matches/Depth_float)
                if pc_not_matching_ref >= min_percent:
                                variant_lines.append(new_line)
                                variant_depth.append(coverage)
                                #print(coverage)
                                #print(Depth_float)
                                #print(new_line)                          
#print(variant_lines)

new_header = "Subject\tlocus\tref_base\tdepth\tA\tG\tC\tT\tInsertions\tDeletions"
#print(new_header)

with open(output_file + "_total_coverage.txt", "w") as fh:
                fh.write(new_header + "\n")
                fh.write("\n".join(depth_lines))
              
with open("Coverage_file.txt", "w") as fh:
                fh.write("\n".join(Coverage_file))

with open(output_file + "_variant_coverage.txt", "w") as fh:
                fh.write(new_header + "\n")
                fh.write("\n".join(variant_lines))

with open("Variant_Depth.txt", "w") as fh:
                fh.write("\n".join(variant_depth))
              
# Zero depth positions using the samtools depth function
Zerolines = open(Total_Depth).readlines()
ZeroDepth_cov = []

for line in Zerolines [0:]:
                f = line.split()
                PositionZero = f[1]
                DepthZero = f[2]
 
                ZeroCoverage = PositionZero + "\t" + DepthZero                     
                ZeroDepth_float = float(DepthZero)
                if ZeroDepth_float == 0:
                                ZeroDepth_cov.append(ZeroCoverage)
