"""Example script demonstrating use of the Device Description."""

import argparse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon
from omas import ODS

if __name__ == "__main__":
    #
    # We set up a simple command line interface to allow a user to specify the
    # file to load from and whether to interactively open a plot or save it to
    # a file.
    parser = argparse.ArgumentParser(prog="Device Description Plotter")
    parser.add_argument(
        "-f",
        "--file",
        help="The device description json file.",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file to save to",
        default="",
    )
    args = parser.parse_args()

    # The first step is to load the json file and turn it into an `OMAS.ODS`
    # object which represents the class through which all interactions with the
    # data are performed.

    # The consistency_check=True argument will make omas validate the loaded
    # data against the IMAS schema
    ods = ODS(consistency_check=True).load(args.file)

    # Create a figure to plot the geometry description we will be retrieving
    # from the ODS object.
    fig, ax = plt.subplots(figsize=(8, 9))

    # Note: The below example is specific to the shared device description.
    # This is not a general plotting routine that would work for all possible
    # geometry descriptions that adhere to the IMAS data schema.
    #
    # Thus you will often see that wee access fields directly like below where
    # we directly access the Vacuum Vessel description and we know that it is
    # in "block format"

    # A more general routine would need to iterate over each wall description
    # checking the "wall.description_2d.[:].type" value to determine the type
    # of wall description and then choose an appropriate plotting routing

    # See for example "wall.description_2d[:].vessel.type", for possible
    # formats of vessel description. In our case we know it's:
    assert ods["wall.description_2d.0.vessel.type.index"] == 1
    assert ods["wall.description_2d.0.vessel.type.description"] == "Block description of the vessel"

    # The string based access above shows one of the reasons why using omas is a good idea.
    # and this is a good moment to link to an omas example:
    # https://gafusion.github.io/omas/auto_examples/showcase_paths.html#sphx-glr-auto-examples-showcase-paths-py
    # Which explains this feature in more detail.
    #
    # In short, usually a python dictionary access would require multiple levels of [].
    # ODS still supports this:
    assert ods["wall"]["description_2d"][0]["vessel"]["type"]["index"] == 1
    # But it is clearly more cumbersome. If you were to simply use the `json`
    # library to open the file, every access would have to be done like above.
    # There is other neat features like array access, which are showcased in
    # the linked omas example.

    # Retrieve the inner and outer wall description
    vv_iw = ods["wall.description_2d.0.vessel.unit.0.element"]
    vv_ow = ods["wall.description_2d.0.vessel.unit.1.element"]

    ## Iterate over each block and add a polygon patch to the figure
    for i, elem in enumerate([*vv_iw.values(), *vv_ow.values()]):
        # R and Z coordinates are arrays of values
        r = elem["outline.r"]
        z = elem["outline.z"]
        ax.add_patch(
            Polygon(
                np.array((r, z)).T,
                lw=0.5,
                fill=False,
                # Only label the first element so the legend does not have
                # repeated elements
                label="Vacuum Vessel" if i == 0 else None,
            ),
        )

    # Plot the VSC Coil Covers. We know that there are 2 coil covers so we
    # simply access them directly
    ax.add_patch(
        Polygon(
            np.array(
                (
                    ods["pf_passive.loop.0.element.0.geometry.outline.r"],
                    ods["pf_passive.loop.0.element.0.geometry.outline.z"],
                )
            ).T,
            linestyle="--",
            lw=0.5,
            fill=False,
            label="Coil Cover",
        )
    )
    ax.add_patch(
        Polygon(
            np.array(
                (
                    ods["pf_passive.loop.1.element.0.geometry.outline.r"],
                    ods["pf_passive.loop.1.element.0.geometry.outline.z"],
                )
            ).T,
            linestyle="--",
            lw=0.5,
            fill=False,
        )
    )

    # Plot the limiter contour
    ax.add_patch(
        Polygon(
            np.array(
                (
                    ods["wall.description_2d.0.limiter.unit.0.outline.r"],
                    ods["wall.description_2d.0.limiter.unit.0.outline.z"],
                )
            ).T,
            lw=1,
            fill=False,
            ec="y",
            linestyle="-.",
            label="Limiter",
        )
    )

    # All axis symmetric coils are stored in the `pf_active` hierarchy.
    # Iterate over all coils and plot its turns.
    for ci, ods_coil in enumerate(ods["pf_active.coil"].values()):
        # In the IMAS data schema each coil is made up from "elements" which
        # represent a conductor of a certain geometry.
        # Again, here we know that what is stored all have geometry type
        # "annulus", but a more general routine would have to check whether it
        # is outline, rectangle, oblique, arcs of circle, annulus, or thick
        # line.

        # The below shows how one can do an array access. For example `rw` will
        # have the `annulus.r` coordinate for all stored elements since it has
        # the string `element.:.`, while `element.0.` would access only the
        # first element.
        rw = ods_coil["element.:.geometry.annulus.r"]
        zw = ods_coil["element.:.geometry.annulus.z"]
        ro = ods_coil["element.:..geometry.annulus.radius_outer"]
        ri = ods_coil["element.:..geometry.annulus.radius_inner"]

        # We know that this is true for our data, but let's check to ensure
        # that not plotting ri is correct.
        assert np.all(ri == 0), "Expect all inner radius to be zero in in this geometry."

        for i in range(len(ro)):
            ax.add_patch(
                Circle(
                    (rw[i], zw[i]),
                    ro[i],
                    color="orange",
                    lw=0,
                    alpha=0.5,
                    # Only label the first element of the first coil so
                    # the legend does not have repeated elements
                    label="Coil Turns" if ci + i == 0 else None,
                )
            )

    # Just some last touches to the plot before we are done.
    ax.set_xlabel("R / m")
    ax.set_ylabel("Z / m")
    ax.autoscale_view()
    ax.set_aspect(1)
    ax.legend(loc="upper right")

    if args.output:
        plt.savefig(args.output, bbox_inches="tight", dpi=100)
    else:
        plt.show()
