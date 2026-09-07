const { chromium } = require('playwright-core');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    recordVideo: { dir: 'video', size: { width: 1920, height: 1080 } }
  });
  const page = await context.newPage();

  const t0 = Date.now();
  const el = () => ((Date.now() - t0) / 1000).toFixed(2);
  await page.goto('https://rohaana.github.io/sarafai/', { waitUntil: 'networkidle', timeout: 60000 });
  console.log('T LOAD', el());
  await sleep(1500);

  await page.waitForSelector('#tourTip', { state: 'visible', timeout: 15000 });
  console.log('T WELCOME', el());
  await sleep(4200);
  await page.click('#tourStart');

  for (let step = 1; step <= 8; step++) {
    await page.waitForSelector(`#tourTip:has-text("STEP ${step} OF 8")`, { state: 'visible', timeout: 15000 });
    console.log('T STEP' + step, el());
    if (step === 5) {
      await page.waitForFunction(() => {
        const b = document.getElementById('confirmBtn');
        return b && !b.disabled;
      }, { timeout: 20000 });
      console.log('T OCR_DONE', el());
      await sleep(2500);
    }
    await sleep(step === 1 || step === 8 ? 6500 : 5500);
    await page.click('#tourNext');
  }

  console.log('T FINISH', el());
  await sleep(4500);

  await page.click('.receipt-thumb:nth-child(2)');
  console.log('T BONUS_CLICK', el());
  await page.waitForFunction(() => {
    const b = document.getElementById('confirmBtn');
    return b && !b.disabled;
  }, { timeout: 20000 });
  console.log('T BONUS_OCR_DONE', el());
  await sleep(2500);
  await page.click('#confirmBtn');
  console.log('T BONUS_CONFIRMED', el());
  await sleep(4200);

  await context.close(); // flushes video to disk
  await browser.close();
  console.log('DONE');
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
