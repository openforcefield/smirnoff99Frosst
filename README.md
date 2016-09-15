# smirff99Frosst

This provides the first general-purpose implementation of a Smirks Force Field (SMIRFF) as implemented by [SMARTY](https://github.com/open-forcefield-group/smarty) and its ForceField class (in smarty.forcefield) for parameterizing small molecules for OpenMM.

## What it is

The provided smirff99Frosst.xml (forcefield) is a starting point for a general-purpose small molecule force field in the SMIRFF format; it should cover all or almost all of drug-like chemical space, and illustrates some of the major functionality of the SMIRFF format as well as how it simplifies the specification of force field parameters in a compact and chemically sensible way.

HOWEVER, this is not expected to be (at present) an especially accurate small molecule force field. 
Its authors (see History, below) expect that while coverage will initially be good, additional refinements will be required (and possibly some expansion of the number of parameters) before it can rival current force fields such as GAFF or OPLS in accuracy. 
However, we are optimistic that it already rivals them in extensibility, and potentially with relatively minimal work can be extended to be a compelling present-day small molecule force field.

As with typical members of the AMBER force field family, smirf99Frosst is intended to be used with RESP or AM1-BCC charges which are not specified by the force field itself.

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
Specifically, the handling of improper torsions needs to be validated. 
Please see the smarty issue tracker for details.

## Versions


## Contributors

Contributors to the relevant ffxml file include:
- Christopher I. Bayly (OpenEye Software/UC Irvine)
- Caitlin C. Bannan (UC Irvine)
- David L. Mobley (UC Irvine)

Special thanks go to John D. Chodera (MSKCC) for his initial implementation of `smarty.forcefield`.
