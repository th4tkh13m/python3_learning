As some of you have noticed, the .pyc files for the robot visualisation only go up to Python 3.7

Likewise the precompiled .pyc files for Part B of the problem set.

EDIT to add the fuller instructions which I have now recovered from the last edition of this course.

The additions are 38 and 39, for Python 3.8 and 3.9 respectively. If you load them into the same directory as the rest of the ps2 verifiers, and then edit the lines at the top of the ps2.py file as follows:-

1) Click on the three dots after import to expand the import commands

2) Edit one of the lines to read

from ps2_verify_movement37 import testRobotMovement (for Python 3.7)

from ps2_verify_movement38 import testRobotMovement (for Python 3.8)

from ps2_verify_movement39 import testRobotMovement (for Python 3.9)

and uncomment it (remove the hash #)

3) Make sure all the versions except the one relating to your python version are commented out with a #

then the test and plot functionality should be restored.
The following link is a link for downloading the needed file for different python version:
https://github.com/Richard-B-UK/MITx-6.00.2x-version-files-for-Python-3.5---3.9