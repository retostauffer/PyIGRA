

PyIGRA --keep --id ASM00094120 -o ASM00094120.txt
if [ $? -ne 0 ] ; then echo "DAMN IT"; exit 9; fi
PyIGRA --keep --id AGM00060390 -o AGM00060390.txt
if [ $? -ne 0 ] ; then echo "DAMN IT"; exit 9; fi
PyIGRA --keep --id ASM00094998 -o ASM00094998.txt
if [ $? -ne 0 ] ; then echo "DAMN IT"; exit 9; fi
PyIGRA --keep --id GMM00010393 -o GMM00010393.txt
if [ $? -ne 0 ] ; then echo "DAMN IT"; exit 9; fi
