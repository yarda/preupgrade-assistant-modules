#!/bin/bash

. /usr/share/preupgrade/common.sh

#END GENERATED SECTION
ARCH="$(arch)"

# grub is not supported on s390x machines
[ "$ARCH" == "s390x" ] && exit_not_applicable

DIR=grubby_workaround
FILE=postupgrade.sh
mkdir -p $POSTUPGRADE_DIR/$DIR
cp  $FILE $POSTUPGRADE_DIR/$DIR/$FILE
chmod a+x $POSTUPGRADE_DIR/$DIR/$FILE
exit_fixed
