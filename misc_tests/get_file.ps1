Add-Type -AssemblyName System.Windows.Forms
$OpenFileDialog = New-Object System.Windows.Forms.OpenFileDialog
$OpenFileDialog.ShowDialog() | Out-Null
$OpenFileDialog.FileName
