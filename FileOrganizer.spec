# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Get Python DLL path and current directory
import os
python_dll = os.path.join(os.environ['pythonLocation'], 'python312.dll')
current_dir = os.path.dirname(os.path.abspath(SPECPATH))

a = Analysis(
    [os.path.join(current_dir, 'FileOrganizer.py')],  # Use absolute path
    pathex=[current_dir],  # Add current directory to path
    binaries=[(python_dll, '.')],  # Include Python DLL
    datas=[],
    hiddenimports=[
        'sys',
        'os',
        'shutil',
        'pathlib',
        'datetime',
        'time'
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
