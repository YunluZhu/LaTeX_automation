# LaTeX Toolbox

This repo contains scripts for solving LaTeX bibliography formating problems.

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

