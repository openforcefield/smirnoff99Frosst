# SMIRNOFF99Frosst

This provides the first general-purpose implementation of a SMIRKS Native Open Force Field (SMIRNOFF) created by the
[Open Force Field Initiative](https://openforcefield.org).
You can parameterize small molecules with SMIRNOFF using the
`ForceField` class in the [openforcefield toolkit](https://github.com/openforcefield/openforcefield)
for simulations with [OpenMM](http://openmm.org/).
Details about this new format are documented in our recent publication ([doi:10.1021/acs.jctc.8b00640](https://www.doi.org/10.1021/acs.jctc.8b00640) or [bioRxiv](https://doi.org/10.1101/286542)).
Usage examples can be found in the [openforcefield repository](https://github.com/openforcefield/openforcefield/tree/master/examples).

Latest release: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1186466.svg)](https://doi.org/10.5281/zenodo.1186466)

## Installation
```bash
conda install -c mobleylab smirnoff99frosst=1.0.7
```
(SMIRNOFF99frosst was formerly known as SMIRFF99frosst)

## What it is

The provided smirnoff99Frosst.xml (forcefield) is a starting point for a general-purpose small molecule force field in [the SMIRNOFF format](https://github.com/openforcefield/openforcefield/blob/master/The-SMIRNOFF-force-field-format.md); it should cover all or almost all of drug-like chemical space, and illustrates some of the major functionality of the SMIRNOFF format as well as how it simplifies the specification of force field parameters in a compact and chemically sensible way.

HOWEVER, this is not expected to be (at present) an especially accurate small molecule force field.
Its authors (see History, below) expect that while coverage will initially be good, additional refinements will be required (and possibly some expansion of the number of parameters) before it can rival current force fields such as GAFF or OPLS in accuracy.
However, we are optimistic that it already rivals them in extensibility, and potentially with relatively minimal work can be extended to be a compelling present-day small molecule force field.

As with typical members of the AMBER force field family, SMIRNOFF99Frosst is intended to be used with RESP or AM1-BCC charges which are not specified by the force field itself.

**Differences from parm99 and parm@frosst**:

SMIRNOFF99Frosst is neither parm99 nor parm@frosst exactly, for a number of reasons including that:

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

This forcefield, SMIRNOFF99Frosst, is a logical descendant of AMBER's parm99 forcefield as well as Merck-Frosst's [parm@frosst](http://www.ccl.net/cca/data/parm_at_Frosst/), but is generalized/simplified and put into the SMIRNOFF format.

SMIRNOFF99Frosst was created by Christopher I. Bayly (with help from Caitlin C. Bannan and David L. Mobley, UC Irvine) during his sabbatical at UCI during Summer 2016.
It was created by hand curation of the original parm99 and parm@frosst parameter and frcmod files (manually creating SMIRKS patterns, condensing parameters, etc.).
Usage of SMIRKS, along with application of Bayly's chemical intuition and extensive history with the AMBER force field family, allowed the number of parameter lines to be reduced from the multiple thousands of parm99+parm@frosst to the few hundred seen here.

## Tentative plan

We expect to continue to manually expand this to cover more chemical space and, when needed, to introduce additional parameters to improve accuracy.
Subsequent versions are expected to build on Bayly's hand created version with some enhancements by Caitlin Bannan by improving specific parameters, further differentiating some chemical functionality, etc.
However, derivatives are expected to retain this basic structure and the AMBER legacy/history; a full refitting of bonded parameters would result in a separate force field rather than a new version of this force field.

## Using SMIRNOFF99Frosst

In OpenMM, application of SMIRNOFF99Frosst to small molecules should be straightforward via `openforcefield` with examples available in the [openforcefield repository](https://github.com/openforcefield/openforcefield/tree/master/examples).
Additionally, with ParmEd, it should be possible to convert parameterized OpenMM systems into other formats such as AMBER, CHARMM, or GROMACS, making this forcefield available in a variety of packages.


## Versions
- Version 1.0/[Version 1.0.1](http://dx.doi.org/10.5281/zenodo.154235) (equivalent): Initial release after hand curation by C. I. Bayly and C. C. Bannan. DOI [10.5281/zenodo.154235](http://dx.doi.org/10.5281/zenodo.154235)
- [Version 1.0.2](http://doi.org/10.5281/zenodo.154555): Fixes an out-of-order generic (bond `[#6X2:1]-[#6:2]`) as per [Issue 4](https://github.com/openforcefield/smirnoff99Frosst/issues/4).
- [Version 1.0.3](http://dx.doi.org/10.5281/zenodo.161616): Bug fixes -- adding one omitted bond length, fixing four torsional smirks patterns, and adding one missing torsional term as detailed in [smarty issue 164](https://github.com/openforcefield/smarty/pull/164)
- [Version 1.0.4](http://doi.org/10.5281/zenodo.348165): Bug fixes --  #11: Fix the parm@Frosst-derived C-OS bond length so it does not also match (and thus override) C-OH, switching from SMIRKS of `[#6X3:1](=[#8X1])-[#8X2:2]` to `[#6X3:1](=[#8X1])-[#8X2H0:2]`, which avoids overriding `[#6X3:1]-[#8X2H1:2]`. And then add back in a generic which should have been present ([PR 15](https://github.com/openforcefield/smirnoff99Frosst/pull/15), fixing a bug introduced by [PR 11](https://github.com/openforcefield/smirnoff99Frosst/pull/11))
- [Version 1.0.5](http://doi.org/10.5281/zenodo.495249): Substantially improved coverage of chemical space via more general generics as well as a variety of new parameters introduced via generalization/estimation from other force fields such as GAFF/GAFF2. This release, this version covers an internal set of molecules from DrugBank filtered to remove metal atoms and to contain only compounds with less than 200 heavy atoms. Full documentation of changes is available [here](https://github.com/openforcefield/smarty/pull/232).
- [Version 1.0.6](https://doi.org/10.5281/zenodo.1093346): Added monovalent ion parameters (Joung/Cheatham) for TIP3P as default. Added angle parameters for cyclobutyl groups. Replaced `R` decorators with `x` to guarantee compatibility between OpenEye toolkits and RDKit SMIRKS parsing.
- [Version 1.0.7](https://dx.doi.org/10.5281/zenodo.1186466): Add hydroxyl hydrogen radii (as per SMIRNOFF initial paper); remove generics with pure wildcards (not even elemental types).
- [Version 1.0.8](http://doi.org/10.5281/zenodo.2565295): Fix human error in hydroxyl hydrogens; fix bond parameters between hydrogen and divalent carbons ([issue #81](https://github.com/openforcefield/smirnoff99Frosst/issues/81)); and fixed SMIRKS patterns for angle parameters around trivalent carbon in 5-membered rings ([issue #84](https://github.com/openforcefield/smirnoff99Frosst/issues/84)).

**Not yet in a version**:

## Contributors

Contributors to the relevant .offxml file include:
- Christopher I. Bayly (OpenEye Software/UC Irvine)
- Caitlin C. Bannan (UC Irvine)
- David L. Mobley (UC Irvine)

Special thanks go to John D. Chodera (MSKCC) for his initial implementation of `openforcefield` toolkits and the SMIRNOFF format.
