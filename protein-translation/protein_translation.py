def proteins(strand):
    string = strand
    RNA_list = []
    
    # Spliting the string +++++++++++++++++++++++++++++++++++
    n = 3   # every 2 characters
    split_string = [string[i:i+n] for i in range(0, len(string), n)]
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    Methionine = ['AUG']
    Phenylalanine = ['UUU', 'UUC']
    Leucine = ['UUA', 'UUG']
    Serine = ['UCU', 'UCC', 'UCA', 'UCG']
    Tyrosine = ['UAU', 'UAC']
    Cysteine = ['UGU', 'UGC']
    Tryptophan = ['UGG']
    STOP = ['UAA', 'UAG', 'UGA']
    
    out_list =[]

    # Starting of comparations
    for item in split_string:
        if item in Methionine:
            out_list.append('Methionine')
        if item in Phenylalanine:
            out_list.append('Phenylalanine')
        if item in Leucine:
            out_list.append('Leucine')
        if item in Serine:
            out_list.append('Serine')
        if item in Tyrosine:
            out_list.append('Tyrosine')
        if item in Cysteine:
            out_list.append('Cysteine')
        if item in Tryptophan:
            out_list.append('Tryptophan')
        if item in STOP:
            break
    return out_list

print(proteins.Phenylalanine)