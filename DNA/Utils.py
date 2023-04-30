import random
import collections
from DNAconstants import nucleotides, RNA_Codons, DNA_Codons

class BioSeq:
    """DNA sequnece class. Defalt value: ATCG, DNA, No label"""

    def __init__(self, seq="ATCG", seq_type="DNA", label='No Label'):
        """Sequence initialization and validation."""
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided string does not seem to be a correct {self.seq_type} sequence"



    def __validate(self):
        """Check the sequence to make sure it is a valid DNA string"""
        return set(nucleotides[self.seq_type]).issuperset(self.seq)

    def generate_random_DNA(self, length=10, seq_type="DNA"):
        """Generate a random DNA sequence, provided the length"""
        seq = ''.join([random.choice(nucleotides[seq_type])
                       for x in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")


    def nuc_freq(self):
        return dict(collections.Counter(self.seq))

    def transcription(self):
        """replaces the T by U"""
        if self.seq_type== "DNA":
            return self.seq.replace("T","U")
        return"The provided sequence is not a DNA sequence"

    def DNA_complement(self):
        #could use mapping
        map = str.maketrans('ATCG','TAGC')
        return self.seq.translate(map)
        

    def reverse_complement(self):
        if self.seq_type== "DNA":
            map = str.maketrans('ATCG','TAGC')
        else:
            map = str.maketrans('AUCG','UAGC')    
        return self.seq.translate(map)[::-1]
    
    def calculate_gc (self):
        return (self.seq.count("G")+ self.seq.count("C")) * 100/len(self.seq) 

    def translate (self, start_pos = 0):
        if self.seq_type== "DNA":
            return[DNA_Codons [self.seq[pos : pos +3]] for pos in range(start_pos , len(self.seq)-2 , 3)]
        else:
            return[RNA_Codons [self.seq [pos : pos +3]] for pos in range(start_pos , len(self.seq)-2 , 3)]

        

    def gen_rf(self):
        rf = []
        rf.append(self.translate_DNA(self.translate_DNA(0))) 
        rf.append(self.translate_DNA(self.translate_DNA(1))) 
        rf.append(self.translate_DNA(self.translate_DNA(2))) 
        temp_seq= BioSeq(self.DNA_reverse_complement, self.seq_type)
        rf.append(temp_seq.translate_DNA(0)) 
        rf.append(temp_seq.translate_DNA(1)) 
        rf.append(temp_seq.translate_DNA(2))
        del temp_seq
        return rf 

    def rf_to_protein(self, aa_seq):
        current_prot = []
        proteins = []
        for aa in aa_seq:
            if aa == "_":
                # STOP accumulating amino acids if _ - STOP was found
                if current_prot:
                    for p in current_prot:
                        proteins.append(p)
                    current_prot = []
            else:
                # START accumulating amino acids if M - START was found
                if aa == "M":
                    current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i] += aa
        return proteins

    def orfs_poly_peptides(self, start_pos = 0, end_pos = 0, ordered = True):
        """Compute all possible proteins for all open reading frames"""
        """Protine Search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
        """API can be used to pull protein info"""
        if end_pos > start_pos:
            temp_seq= BioSeq(self.seq[start_pos : end_pos], self.seq_type)
            rfs = temp_seq.gen_rf()
        else:
            rfs = self.gen_rf()

        res = []
        for rf in rfs:
            prots = self.rf_to_protein(rf)
            for p in prots:
                res.append(p)

        if ordered:
            return sorted(res , key=len , reverse=True)
        return res


