[Setup]
AppName=File Organizer
AppVersion=1.0
DefaultDirName={pf}\FileOrganizer
DefaultGroupName=File Organizer
OutputDir=.
OutputBaseFilename=FileOrganizerInstaller
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\FileOrganizer.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\File Organizer"; Filename: "{app}\FileOrganizer.exe"
Name: "{group}\Uninstall File Organizer"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\FileOrganizer.exe"; Description: "{cm:LaunchProgram,File Organizer}"; Flags: nowait postinstall skipifsilent
