# maintboot

maintboot runs commands outside of the current OS,
with exclusive access to the system and hardware.

This can be useful to run maintenance tasks,
like repartitioning, in a controlled environment.

Maintboot builds an appliance on the fly from a list
of packages (using supermin).
It then loads the appliance with kexec, bypassing
the bios, and runs the maintenance script in that
new context.

# Usage

Write an initscript

    maintboot --pkgs pkg1 pkg2 --initscript init

Most things are left to the initscript, like parsing
the kernel commandline (may need some kind of encoding)
and choosing to either reboot or shutdown after maintenance.

