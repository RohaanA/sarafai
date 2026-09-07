$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech

$segs = @(
  @('n01', 'SarafAI. Credit scoring for the invisible economy.'),
  @('n02', 'Ahmed''s store earns well, but banks see no history, so no loan.'),
  @('n03', 'The score is explainable: six auditable cash flow factors.'),
  @('n04', 'A score becomes money: a collateral-free loan offer.'),
  @('n05', 'The data? Receipts, khata pages, and wallet histories.'),
  @('n06', 'Our OCR engine, Qwen V L on Alibaba Cloud, extracts every field from one photo.'),
  @('n07', 'The merchant verifies in one tap.'),
  @('n08', 'Every confirmed record joins one reconciled, fraud-checkable ledger.'),
  @('n09', 'Scan, verify, score, lend. One loop that banks the unbanked.'),
  @('n10', 'Try it yourself. Every scan updates the score in real time.'),
  @('n11', 'SarafAI. Credit for the invisible economy.')
)

foreach ($s in $segs) {
  $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
  $synth.Rate = 1
  try { $synth.SelectVoice('Microsoft Zira Desktop') } catch {}
  $synth.SetOutputToWaveFile((Join-Path $PSScriptRoot "audio\$($s[0]).wav"))
  $synth.Speak($s[1])
  $synth.Dispose()
}
Write-Output 'TTS done'
