# -*- mode: python -*-

block_cipher = None


a = Analysis(['desktop_appTK.py'],
             pathex=['C:\\Users\\kdrag\\Documents\\Python_recap\\Python_project5(tkinter_desktopapp)'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='desktop_appTK',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
