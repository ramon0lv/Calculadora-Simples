# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calculadora.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='calculadora',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='C:\\Users\\l2ram\\AppData\\Local\\Temp\\4b41c95e-8c11-4d4b-9279-e4e8eb44a743',
    icon=['C:\\Users\\l2ram\\OneDrive\\Área de Trabalho\\Calculadora\\calculadora_icon.png'],
)
