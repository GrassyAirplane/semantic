Semantic Language VS Code Extension
==================================

This extension provides syntax highlighting and basic editor behaviors for `.sem` and `.semantic` files.

Quick Test (Extension Development Host)
--------------------------------------
1. Open the `sem_file_format` folder in VS Code.
2. Press `F5` to launch an Extension Development Host window.
3. In the new window, open `example.sem` to see syntax highlighting.

Commands
```
# open the project in VS Code (run from PowerShell)
code .

# Press F5 in VS Code to start the Extension Development Host
```

What to verify
- Status bar shows `Semantic` as the language when `example.sem` is open.
- Keywords such as `@meta`, `@function`, and `purpose::` are highlighted.
- Strings, numbers, comments, and list items are highlighted.
- Folding works for blocks starting with `@...` and ending with `@end`.

Troubleshooting
---------------
- If highlighting doesn't appear:
  - Reload the Extension Development Host: use the Command Palette → `Developer: Reload Window`.
  - Manually set the language for the file: click the language in the lower-right status bar → `Configure File Association for '.sem'...` → choose `Semantic`.
  - Inspect token scopes: Command Palette → `Developer: Inspect Editor Tokens and Scopes` and click a token to see the grammar scope assigned.
  - Ensure `package.json` includes the `contributes.languages` and `contributes.grammars` sections.

Install Permanently
-------------------
Copy the `sem_file_format` folder to your VS Code extensions directory and restart VS Code:

Windows:
```
# replace <username> or use %USERPROFILE% in File Explorer
copy /Y /E sem_file_format "%USERPROFILE%\.vscode\extensions\semantic-language-1.0.0"
```

Package (.vsix) and Install
---------------------------
1. Install the vsce packager:
```
npm install -g vsce
```
2. From the `sem_file_format` folder run:
```
vsce package
# then install the produced .vsix with
code --install-extension semantic-language-1.0.0.vsix
```

If you want, I can:
- Update the `README.md` with screenshots and token-scope notes.
- Add tests or a small `test/` file to verify grammar tokens programmatically.
- Help package the `.vsix` here (requires `vsce` installed in your environment).
