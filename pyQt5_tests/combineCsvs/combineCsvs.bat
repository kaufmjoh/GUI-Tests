echo off
set cSourceFile=%1
set executableDest=%2
set inputFile1=%3
set inputFile2=%4
set destinationFile=%5

gcc %cSourceFile% -o %executableDest%

%executableDest% %inputFile1% %inputFile2% %destinationFile%

rm %executableDest%