import adsk.core
import adsk.fusion
import traceback

import time

from .Fusion360Utilities.Fusion360Utilities import AppObjects
from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase


SLEEP_TIME = 1


def all_off(bodies: adsk.fusion.BRepBodies):
    for body in bodies:
        body.isLightBulbOn = False


class HiderCommand(Fusion360CommandBase):

    def on_execute(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs, args, input_values):

        # Get a reference to all relevant application objects in a dictionary
        ao = AppObjects()

        bodies = ao.root_comp.bRepBodies

        all_off(bodies)

        for body in bodies:
            all_off(bodies)
            body.isLightBulbOn = True

            time.sleep(SLEEP_TIME)

            adsk.doEvents()

