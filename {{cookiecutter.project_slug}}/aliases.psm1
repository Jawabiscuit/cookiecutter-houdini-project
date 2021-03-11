<#
aliases.psm1
#>

Function Invoke-Houdini {

    [CmdletBinding()] 
    [Alias('hou')]

    Param(
        [string] $File,
        [string] $Option2,
        [int] $Option3)

    $houdiniCmd = @("houdini", "-background", "-s", "Solaris")
    if ($File -ne "") {
        $houdiniCmd += @($File)
    }

    If ($MyInvocation.InvocationName -eq 'hou') {
        Write-Host "Launching houdini!" -ForegroundColor Yellow
        cmd /c "$houdiniCmd"
    }
    Else {
        Write-Host "Launching houdini..." -ForegroundColor Green
        cmd /c "$houdiniCmd"
    }
}

Function Invoke-Emacs {

    [CmdletBinding()] 
    [Alias('em')]

    Param(
        [string] $File,
        [string] $Option2,
        [int] $Option3)

    $emacsCmd = @("emacs")
    if ($File -ne "") {
        $emacsCmd += @($File)
    }

    If ($MyInvocation.InvocationName -eq 'em') {
        Write-Host "Launching Emacs!" -ForegroundColor Yellow
        # cmd /c "$emacsCmd"
        Start-Process -NoNewWindow "$emacsCmd"
    }
    Else {
        Write-Host "Launching Emacs..." -ForegroundColor Green
        Start-Process -NoNewWindow "$emacsCmd"
    }
}
