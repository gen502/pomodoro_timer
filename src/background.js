'use strict'

import { app, protocol, BrowserWindow } from 'electron'
import { createProtocol } from 'vue-cli-plugin-electron-builder/lib'
import installExtension, { VUEJS3_DEVTOOLS } from 'electron-devtools-installer'
const isDevelopment = process.env.NODE_ENV !== 'production'
const { ipcMain } = require('electron');

// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([
  { scheme: 'app', privileges: { secure: true, standard: true } }
])

let isWindowMinimized = false; // ウィンドウが縮小されているかどうかのフラグ
let originalSize = { width: 800, height: 600 }; // ウィンドウの元のサイズ
let originalPosition = { x: 0, y: 0 }; // ウィンドウの元の位置
let isCursorOverMinimizeButtonLastState = false;

ipcMain.handle('set-ignore-mouse-events', (event, ignore) => {
  console.log("toggle-minimize called");
  const win = BrowserWindow.getFocusedWindow();
  if (win) {
    if (ignore) {
      console.log("Minimizing window");
      // ウィンドウの元のサイズと位置を保存
      originalSize = win.getSize();
      originalPosition = win.getPosition();

      // ウィンドウのサイズを変更
      win.setSize(500, 500); // 30%のサイズに変更

      // ウィンドウを右下に移動
      const { screen } = require('electron');
      const { width, height } = screen.getPrimaryDisplay().workAreaSize;
      win.setPosition(width - 490, height - 490);

      // ウィンドウを最前面に固定
      win.setAlwaysOnTop(true);

      // ウィンドウを透明にする
      win.setOpacity(0.3);

      // 最小化ボタンの領域を取得する関数
      function getMinimizeButtonBounds(win) {
        const winBounds = win.getBounds();
        const buttonSize = 40; // 最小化ボタンのサイズ
        const buttonMargin = 7; // 最小化ボタンのマージン
        return {
          x: winBounds.x + winBounds.width - buttonSize - buttonMargin * 2,
          y: winBounds.y + winBounds.height - buttonSize - buttonMargin * 2,
          width: buttonSize,
          height: buttonSize
        };
      }

      win.webContents.on('cursor-changed', (_, _type, _image, _scale, _size) => {
        const cursorPosition = screen.getCursorScreenPoint();
        const minimizeButtonBounds = getMinimizeButtonBounds(win);
        const isCursorOverMinimizeButton = cursorPosition.x >= minimizeButtonBounds.x &&
          cursorPosition.x <= minimizeButtonBounds.x + minimizeButtonBounds.width &&
          cursorPosition.y >= minimizeButtonBounds.y &&
          cursorPosition.y <= minimizeButtonBounds.y + minimizeButtonBounds.height;

        // カーソルの状態が変わったときだけ win.setIgnoreMouseEvents を呼び出す
        if (isCursorOverMinimizeButton !== isCursorOverMinimizeButtonLastState) {
          win.setIgnoreMouseEvents(!isCursorOverMinimizeButton, { forward: true });
          isCursorOverMinimizeButtonLastState = isCursorOverMinimizeButton;
        }
      });

      win.setIgnoreMouseEvents(true, { forward: true });
      isWindowMinimized = true;

    } else {
      console.log("Restoring window");
      // ウィンドウのサイズと位置を元に戻す
      win.setSize(originalSize[0], originalSize[1]);
      win.setPosition(originalPosition[0], originalPosition[1]);

      // 最前面固定を解除
      win.setAlwaysOnTop(false);

      // ウィンドウの透明度を元に戻す
      win.setOpacity(1.0);

      win.setIgnoreMouseEvents(false);
      isWindowMinimized = false;
    }
  }
});

async function createWindow() {
  // Create the browser window.
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true
    },
    frame: false,  // フレームをオフにする
  })


  if (process.env.WEBPACK_DEV_SERVER_URL) {
    // Load the url of the dev server if in development mode
    await win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)
    // if (!process.env.IS_TEST) win.webContents.openDevTools()
  } else {
    createProtocol('app')
    // Load the index.html when not in development
    win.loadURL('app://./index.html')
  }
}

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    // Install Vue Devtools
    try {
      await installExtension(VUEJS3_DEVTOOLS)
    } catch (e) {
      console.error('Vue Devtools failed to install:', e.toString())
    }
  }
  createWindow()
})

// Exit cleanly on request from parent process in development mode.
if (isDevelopment) {
  if (process.platform === 'win32') {
    process.on('message', (data) => {
      if (data === 'graceful-exit') {
        app.quit()
      }
    })
  } else {
    process.on('SIGTERM', () => {
      app.quit()
    })
  }
}
