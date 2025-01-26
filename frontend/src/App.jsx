import { useState } from 'react'
import './App.css'

const App = () => {
  const [url, setUrl] = useState('')
  const [status, setStatus] = useState('')
  const [isDownloading, setIsDownloading] = useState(false)
  const [audioOnly, setAudioOnly] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!url.trim()) return
    
    setIsDownloading(true)
    setStatus('Starting download...')
    
    try {
      const response = await fetch('http://localhost:5000/download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, audioOnly })
      })
      
      const data = await response.json()
      
      if (response.ok && data.status === 'success') {
        setStatus('✅ Download completed! Check your downloads folder.')
        setUrl('')
      } else {
        setStatus(`❌ ${data.error || 'Download failed. Please try again.'}`)
      }
    } catch (error) {
      setStatus('❌ Error connecting to server. Is the Python server running?')
      console.error('Server connection error:', error)
    }
    setIsDownloading(false)
  }

  const openDownloadsFolder = () => {
    fetch('http://localhost:5000/open-downloads')
  }

  return (
    <div className="app">
      <h1>❄️ Cooldown YT</h1>
      <div className="container">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Paste YouTube URL here..."
            required
          />
          <div className="checkbox-container">
            <label>
              <input
                type="checkbox"
                checked={audioOnly}
                onChange={(e) => setAudioOnly(e.target.checked)}
              />
              Audio only (MP3)
            </label>
          </div>
          <button type="submit" disabled={isDownloading}>
            {isDownloading ? '⏳ Downloading...' : '⬇️ Download'}
          </button>
        </form>
        {status && <p className="status">{status}</p>}
        <p className="downloads-link" onClick={openDownloadsFolder}>
          📂 Open downloads folder
        </p>
      </div>
    </div>
  )
}

export default App