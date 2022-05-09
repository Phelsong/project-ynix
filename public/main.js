const { app, BrowserWindow } = require('electron')
const path = require('path')

//----------------------------------------------------------------
const createWindow = () => {
    const win = new BrowserWindow({
        width: 1200,
        height: 900,
        webPreferences: {
          preload: path.join(__dirname, '../preload.js')
        }
      })
      
      win.loadURL('http://localhost:3000/')
      // win.loadURL(`file:${path.join(__dirname, '../build/index.html')}`)
}

//----------------------------------------------------------------
app.whenReady().then(() => {
    createWindow()
})

//----------------------------------------------------------------
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
})

