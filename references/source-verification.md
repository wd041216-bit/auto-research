# Source Verification

## Purpose

Prevent fabricated references and stale metadata.

## Required Inputs

- Candidate citation metadata
- Source URL, DOI, arXiv ID, DBLP entry, publisher page, or supplied PDF

## Required Outputs

- Verified or uncertain metadata in the literature matrix and BibTeX

## Procedure

1. Verify title, authors, year, venue, DOI, arXiv ID, and URL from primary or trusted index sources.
2. Prefer publisher, conference, journal, arXiv, DBLP, Semantic Scholar, and author project pages over untraceable summaries.
3. When current metadata may have changed, browse or verify before writing.
4. Mark uncertain fields as `uncertain`, not guessed.
5. For arXiv preprints, check whether an accepted venue exists before central citation use.
6. Never fabricate citations, venues, DOIs, author lists, years, or titles.

## Process Constraints

- Prefer primary sources for central claims; secondary indexes may help locate but not replace missing primary metadata when precision matters.
- Record uncertainty in `metadata_status`, `venue_verified`, or notes.
- If current venue or version status may have changed, verify before making final claims.
- Supplied PDFs or local files still require enough metadata to cite or must remain provisional.
- Failed verification is a result: record it and downgrade citation use.

## Blocking Gates

- Unverified central references cannot be `must-cite`.
- Fabricated metadata blocks all final writing using that source.
- Missing source URL, DOI, arXiv ID, or supplied file blocks source verification.

## Common Failure Modes

- Relying on memory for a paper's accepted venue.
- Assuming arXiv version equals final publication.
- Creating plausible BibTeX without source metadata.
