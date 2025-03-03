# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Get Python DLL path and current directory
import os
python_dll = os.path.join(os.environ.get('pythonLocation', ''), 'python312.dll')
current_dir = os.path.dirname(os.path.abspath(SPECPATH))

a = Analysis(
    ['main.py'],  # Changed to main.py as it's the entry point
    pathex=[current_dir],
    binaries=[(python_dll, '.')] if os.path.exists(python_dll) else [],
    datas=[],
    hiddenimports=[
        'sys',
        'os',
        'shutil',
        'pathlib',
        'datetime',
        'time',
        'gui',
        'organizer',
        'theme'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FileOrganizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
