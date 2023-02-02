'''
input: *.bib file location
output: *_edit.bib at same location with "PMCID: PMCxxxxx" in "note"
process:
    1. read bibtex using bibtex.Parser
    2. get doi from doi field. If None, assign empty doi
    3. get pmcid via doi using metapub
    4. save string to note field:
        A. if pmcid is found, save pmcid
        B. if not, but doi is available, write doi, and "PMCID: Not available"
        C. if none is available, write "PMCID: Not available"
'''

# %%
from pybtex.database.input import bibtex
from pybtex.database.input.bibtex import Parser
# from metapub import convert
from tqdm import tqdm
from metapub import pubmedcentral


# %%
# filename = input('Where is .bib file: ')
filename = "/Users/yunluzhu/Documents/Lab2/Writings/K99/_with EmyLou/10 day deadline/k99.bib"
# %%
parser = bibtex.Parser()
bib_data = parser.parse_file(filename)
# %%
# key_list = [e for e in bib_data.entries]
noPMCID_entries = []
PMCID_entries = []
noDOI_entries = []

for e in tqdm(bib_data.entries):
    entry = bib_data.entries[e]
    try:
        doi = entry.fields[u'doi']
    except:
        doi = ''
        print(f"Error getting doi for {e}")
        
    try: 
        pmcid = pubmedcentral.get_pmcid_for_otherid(doi)
        PMCID_entries.append(e)
    except:
        pmcid = None
        
    # add note field
    newbib_parser = Parser()
    newbib_parser.data.add_entry('note',entry)

    note_field = f"PMCID: {pmcid}"
    
    if pmcid is None:
        if doi:
            note_field = f"DOI: {doi}. PMCID: Not available"
        else:
            noDOI_entries.append(e)
            note_field = f"PMCID: Not available"
        noPMCID_entries.append(e)
        
    entry.fields[u'note'] = f"{note_field}"

print(f"No DOI entries:\n    {noDOI_entries}\n")

print(f"Found PMCID for:\n    {PMCID_entries}\n")

if len(noPMCID_entries):
    print(f"Could not get PMCID for following entries:\n    {noPMCID_entries}")

# %%
bib_data.to_file(filename[:-4]+'_edit.bib', bib_format='bibtex')


# %%
