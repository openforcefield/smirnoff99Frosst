# smirff99Frosst

This provides the first general-purpose implementation of a Smirks Force Field (SMIRFF) as implemented by [SMARTY](https://github.com/open-forcefield-group/smarty) and its ForceField class (in smarty.forcefield) for parameterizing small molecules for OpenMM.

Latest release: [![DOI](https://zenodo.org/badge/68331217.svg)](https://zenodo.org/badge/latestdoi/68331217)

## What it is

The provided smirff99Frosst.xml (forcefield) is a starting point for a general-purpose small molecule force field in [the SMIRFF format](https://github.com/open-forcefield-group/smarty/blob/master/The-SMIRFF-force-field-format.md); it should cover all or almost all of drug-like chemical space, and illustrates some of the major functionality of the SMIRFF format as well as how it simplifies the specification of force field parameters in a compact and chemically sensible way.

HOWEVER, this is not expected to be (at present) an especially accurate small molecule force field. 
Its authors (see History, below) expect that while coverage will initially be good, additional refinements will be required (and possibly some expansion of the number of parameters) before it can rival current force fields such as GAFF or OPLS in accuracy. 
However, we are optimistic that it already rivals them in extensibility, and potentially with relatively minimal work can be extended to be a compelling present-day small molecule force field.

As with typical members of the AMBER force field family, smirf99Frosst is intended to be used with RESP or AM1-BCC charges which are not specified by the force field itself.

**Differences from parm99 and parm@frosst**:

smirff99Frosst is neither parm99 nor parm@frosst exactly, for a number of reasons including that:

- It covers, or should cover with only slight modification, all reasonable organic chemistry, which neither of the above did
- It is much simpler (because of parameter consolidation by SMIRKS, because of removing questionably differentiated parameters, and because its goal is to be a "good starting point" than a finished product)
- It introduces a number of approximations/consolidations for conciseness/clarity
- It fixes a number of mistakes/omissions, etc.

The second and third bullet points are particularly important. 
When many parameters (such as torsional barrier heights, or equlibrium angles) for similar chemical functionality differed only slightly in the existing force fields, these were often deliberately consolidated to have a single value. 

The last bullet point is also noteworthy. 
Because of limitations of atom typing, many torsions were missing in parm99/parm@frosst, resulting in generics being erroneously applied when a more specialized torsion could have served.
The use of SMIRKS typically means that this is not the case, so many mistakes are eliminated.

## History

This forcefield, smirff99Frosst, is a logical descendant of AMBER's parm99 forcefield as well as Merck-Frosst's [parm@frosst](http://www.ccl.net/cca/data/parm_at_Frosst/), but is generalized/simplified and put into the SMIRFF format. 

smirff99Frosst was created by Christopher I. Bayly (with help from Caitlin C. Bannan and David L. Mobley, UC Irvine) during his sabbatical at UCI during Summer 2016.
It was created by hand curation of the original parm99 and parm@frosst parameter and frcmod files (manually creating SMIRKS patterns, condensing parameters, etc.). 
Usage of SMIRKS, along with application of Bayly's chemical intuition and extensive history with the AMBER force field family, allowed the number of parameter lines to be reduced from the multiple thousands of parm99+parm@frosst to the few hundred seen here. 

## Tentative plan

We expect to continue to manually expand this to cover more chemical space and, when needed, to introduce additional parameters to improve accuracy. 
Subsequent versions are expected to build on Bayly's hand created version with some enhancements by Caitlin Bannan by improving specific parameters, further differentiating some chemical functionality, etc. 
However, derivatives are expected to retain this basic structure and the AMBER legacy/history; a full refitting of bonded parameters would result in a separate force field rather than a new version of this force field.

## Using smirff99Frosst

In OpenMM, application of smirff99Frosst to small molecules should be straightforward via `smarty.forcefield`. 
Additionally, with ParmEd, it should be possible to convert parameterized OpenMM systems into other formats such as AMBER, CHARMM, or GROMACS, making this forcefield available in a variety of packages.

**However**, some development/testing remains to be done on `smarty.forcefield` before this should be applied widely. 
Please see the smarty issue tracker for details.

## Versions
- Version 1.0/[Version 1.0.1](http://dx.doi.org/10.5281/zenodo.154235) (equivalent): Initial release after hand curation by C. I. Bayly and C. C. Bannan. DOI [10.5281/zenodo.154235](http://dx.doi.org/10.5281/zenodo.154235)
- [Version 1.0.2](http://doi.org/10.5281/zenodo.154555): Fixes an out-of-order generic (bond `[#6X2:1]-[#6:2]`) as per [Issue 4](https://github.com/open-forcefield-group/smirff99Frosst/issues/4).
- Version 1.0.3: Bug fixes -- adding one omitted bond length, fixing four torsional smirks patterns, and adding one missing torsional term as detailed in [smarty issue 164](https://github.com/open-forcefield-group/smarty/pull/164)

## Contributors

Contributors to the relevant ffxml file include:
- Christopher I. Bayly (OpenEye Software/UC Irvine)
- Caitlin C. Bannan (UC Irvine)
- David L. Mobley (UC Irvine)

Special thanks go to John D. Chodera (MSKCC) for his initial implementation of `smarty.forcefield`.
