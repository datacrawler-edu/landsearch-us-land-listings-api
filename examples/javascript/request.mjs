import { readFile } from 'node:fs/promises';
import { setTimeout as wait } from 'node:timers/promises';

const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error('Set APIFY_API_TOKEN.');
const input = JSON.parse(await readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8'));

async function api(path, method = 'GET', body) {
  const response = await fetch('https://api.apify.com/v2' + path, {
    method,
    headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
    signal: AbortSignal.timeout(30000),
  });
  if (!response.ok) throw new Error('Apify returned HTTP ' + response.status);
  return response.json();
}

const { data: started } = await api('/acts/datascraperes~landsearch-us-land-scraper/runs?timeout=120&maxTotalChargeUsd=0.01', 'POST', input);
console.error('Run ID:', started.id);
const deadline = Date.now() + 180000;
let run;
while (Date.now() < deadline) {
  ({ data: run } = await api('/actor-runs/' + started.id));
  if (['SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'].includes(run.status)) break;
  await wait(2000);
}
if (run?.status !== 'SUCCEEDED') throw new Error('Inspect existing run ' + started.id);
const summary = await api('/key-value-stores/' + run.defaultKeyValueStoreId + '/records/SUMMARY');
if (summary.status !== 'completed') throw new Error('Inspect existing run ' + started.id + ': ' + summary.stopReason);
const rows = [];
for (let offset = 0; ; ) {
  const page = await api('/datasets/' + run.defaultDatasetId + '/items?limit=100&offset=' + offset);
  if (!page.length) break;
  rows.push(...page);
  offset += page.length;
}
console.log(JSON.stringify(rows, null, 2));
