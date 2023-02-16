# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
#todo Executable not working
a = Analysis(['geweather.py'],
             pathex=['C:\\Users\\p.delhomme\\PycharmProjects`\\Geweather'],
             binaries=[],
             datas=[('icons', 'icons')],
             hiddenimports=['PyQt5.QtCore', 'PyQt5.QtGui', 'requests'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='WeatherApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )