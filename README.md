# LaTeX Toolbox

This repo contains scripts for getting bibTeX from dois and solving LaTeX bibliography formating problems.
- addPMCID: adds PMCID to bibTeX files
- doi2bib: a Mac Service (Quick Action) for getting bibTeX citation from selected text 

## Prerequisite

- Python3.10
- pybtex
- metapub
- tqdm

## Usage

### Add PMCID 

Script: `addPMCID.py` 
Behave in following ways:
1. load .bib file, fetch PMCID using field `doi` 
2. get pmcid via `doi` using `metapub` package
3. write PMCID to the `note` field in the format of: `PMCID: PMCxxxx`
4. save as a new .bib BibTeX file
5. print results

Notes:
1. for entries that have `doi` but no `PMCID`, write `DOI: xxxx/xx. PMCID: Not available`
2. for entries that have neither, write `PMCID: Not available`

### get bibTeX

1. Download and unzip: `doi2bib-service.workflow`
2. Move the file to ~/Library/Services
3. Adjust security settings to grant your browser accessibility access. To do this, open Preferences > Privacy & Security > Accessibility, turn on your web browser. 
4. Open web browser, right click on a doi address. Click Services > doi2bib-service
5. Keyboard shortcut can be setup under Preferences > Keyboard > Keyboard Shortcuts...
