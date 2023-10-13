# SPARCPublic
SPARC is a compact high-field tokamak (R_0 = 1.85 m, B_0 = 12.2 T) being constructed by Commonwealth Fusion System (CFS). This repository contains a collection of files that can be used as inputs in the physics codes commonly used in the Plasma Physics community. More details on SPARC can be found in a special series of 7 papers published in the Journal of Plasma Physics in 2020 on the SPARC Physics Basis:

Status of the SPARC Physics Basis (Status of the SPARC Physics Basis )
- Creely, A., Greenwald, M., Ballinger, S., Brunner, D., Canik, J., Doody, J., . . . Zhu, J. (2020). Overview of the SPARC tokamak. Journal of Plasma Physics, 86(5), 865860502. doi:10.1017/S0022377820001257
- Rodriguez-Fernandez, P., Howard, N., Greenwald, M., Creely, A., Hughes, J., Wright, J., . . . Sciortino, F. (2020). Predictions of core plasma performance for the SPARC tokamak. Journal of Plasma Physics, 86(5), 865860503. doi:10.1017/S0022377820001075
- Hughes, J., Howard, N., Rodriguez-Fernandez, P., Creely, A., Kuang, A.Q., Snyder, P., . . . Greenwald, M. (2020). Projections of H-mode access and edge pedestal in the SPARC tokamak. Journal of Plasma Physics, 86(5), 865860504. doi:10.1017/S0022377820001300
- Kuang, A.Q., Ballinger, S., Brunner, D., Canik, J., Creely, A., Gray, T., . . . Wukitch, S. (2020). Divertor heat flux challenge and mitigation in SPARC. Journal of Plasma Physics, 86(5), 865860505. doi:10.1017/S0022377820001117
- Lin, Y., Wright, J., & Wukitch, S. (2020). Physics basis for the ICRF system of the SPARC tokamak. Journal of Plasma Physics, 86(5), 865860506. doi:10.1017/S0022377820001269
- Sweeney, R., Creely, A., Doody, J., Fülöp, T., Garnier, D., Granetz, R., . . . Zhu, J. (2020). MHD stability and disruptions in the SPARC tokamak. Journal of Plasma Physics, 86(5), 865860507. doi:10.1017/S0022377820001129
- Scott, S., Kramer, G., Tolman, E., Snicker, A., Varje, J., Särkimäki, K., . . . Rodriguez-Fernandez, P. (2020). Fast-ion physics in SPARC. Journal of Plasma Physics, 86(5), 865860508. doi:10.1017/S0022377820001087

## Content
This repository is designed to make publicly available a set of SPARC baseline parameters for the purpose of scientific exploration. It is important to clarify that the information within is meant to be a snapshot in time of the SPARC design and representative of plasmas that may be produced in the machine. For this first release, most of the information within is based on the figures and tables published in the Journal of Plasma Physics papers. The repository includes the following:

### Primary Reference Discharge

- POPCON generated 0D scenario parameters (1)

- Magnetic equilibrium formatted as geqdsk-files and generated using the FREEGS code [FREEGS code](https://github.com/freegs-plasma/freegs) with a simplified first wall contour:
  - Double null discharge equilibrium (2)
  - Lower single null discharge equilibrium (3)
  - Double null discharge equilibrium with high resolution (7)


- CHEASE modified core plasma equilibrium (4)

- Core plasma profiles formatted as a simplified version of an input.gacode file and generated using:
  - TRANSP (5)
  - CGYRO (6) - data published in Rodriguez-Fernandez, P., et al. “Nonlinear gyrokinetic predictions of SPARC burning plasma profiles enabled by surrogate modeling.“ Nucl. Fusion 62 076036 (2022).


- Coil positions / currents for the FreeGS DN Equilibrium (8)


### X-point target

- POPCON generated 0D scenario parameters
- Magnetic equilibrium formatted as geqdsk-files and generated using the [FREEGS code](https://github.com/freegs-plasma/freegs) with a simplified first wall contour:
  - Double null discharge equilibrium
  - single null discharge equilibrium


### EQlibrary
 - This folder contains ~100 magnetic equilibrium reconstructions in GEQDSK format.  
 - Also contains a .png for each GEQDSK
 - GEQDSKs have been corrected to match SPARC helicity

## Version

Note though that over the last two years, the design has progressed and the range of scenarios expanded. Subsequent version controlled updates will be released with the associated data provenance.

0.1.0 13th October 2022
- Initial file list released consistent with figures and data used in the Journal of Plasma Physics 2020 publications.

## License
```
Copyright 2020 CFS

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
## Acknowledgement Statement

Use of this data in publication and presentation should be acknowledged as:

"The information, data, or work presented herein builds on the SPARC primary reference discharge and X-point target discharge data provided by Commonwealth Fusion Systems."

## Contact Information

For all enquiries please email akuang@cfs.energy or alex@cfs.energy
