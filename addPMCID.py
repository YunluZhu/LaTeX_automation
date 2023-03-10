'''
input: *.bib file location
output: *_edit.bib at same location with "PMCID: PMCxxxxx" in "note"
process:
    1. read bibtex using bibtex.Parser
    2. get doi from doi field. If None, assign empty doi
    3. get pmcid via doi using metapub
    4. save string to note field:
        A. if pmcid is found, save pmcid
        B. if not, but doi is available, write doi if is intended to, and "PMCID: N/A"
        C. if none is available, write "PMCID: N/A"
NOTE 
See NIH instruction for details:
https://publicaccess.nih.gov/include-pmcid-citations.htm

'''

# %%
from pybtex.database.input import bibtex
# from metapub import convert
from tqdm import tqdm
from metapub import pubmedcentral


# %%
filename = input('Where is .bib file: ')
if_add_doi = input('Do you want to include DOI for references without PMCID? (y/n) ')
if if_add_doi in ['y', 'Y','yes']:
    if_add_doi = True
else:
    if_add_doi = False

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
        noDOI_entries.append(e)
        print(f"Error getting doi for {e}")
        
    try: 
        pmcid = pubmedcentral.get_pmcid_for_otherid(doi)
    except:
        pmcid = None
        
    # add note field
    newbib_parser = bibtex.Parser()
    newbib_parser.data.add_entry('note',entry)

    note_field = f"PMCID: N/A"
    
    if pmcid is None:
        noPMCID_entries.append(e)
        if if_add_doi:
            if doi:
                note_field = f"DOI: {doi}. PMCID: N/A"
    else:
        note_field = f"PMCID: {pmcid}"
        PMCID_entries.append(e)   
         
    entry.fields[u'note'] = f"{note_field}"

print(f"No DOI entries:\n    {noDOI_entries}\n")

print(f"Found PMCID for:\n    {PMCID_entries}\n")

if len(noPMCID_entries):
    print(f"Could not get PMCID for following entries:\n    {noPMCID_entries}")

# %%
bib_data.to_file(filename[:-4]+'_edit.bib', bib_format='bibtex')


# %%
