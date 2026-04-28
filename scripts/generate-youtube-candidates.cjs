#!/usr/bin/env node
/**
 * YouTube Shorts アップロード候補生成
 * 毎日 1-3 本の動画候補をランダムに選択
 */

const fs = require('fs');
const path = require('path');

const OUTPUT_DIR = path.join(__dirname, '../shorts-output');
const CANDIDATES_COUNT = 3;

function getUploadedFiles() {
  const trackedPath = path.join(__dirname, '../.youtube-uploaded.json');
  if (fs.existsSync(trackedPath)) {
    return JSON.parse(fs.readFileSync(trackedPath, 'utf-8')).uploaded || [];
  }
  return [];
}

function getAvailableVideos() {
  const uploaded = getUploadedFiles();
  const uploadedSet = new Set(uploaded);
  const videos = fs.readdirSync(OUTPUT_DIR)
    .filter(f => f.endsWith('_shorts_v2.mp4'))
    .map(f => f.replace('_shorts_v2.mp4', ''))
    .filter(slug => !uploadedSet.has(slug))
    .sort();
  return videos;
}

function selectCandidates(videos, count) {
  if (videos.length === 0) return [];
  const shuffled = videos.sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(count, videos.length));
}

function generateCandidateInfo(slug) {
  const videoPath = path.join(OUTPUT_DIR, `${slug}_shorts_v2.mp4`);
  const srtPath = path.join(OUTPUT_DIR, `${slug}_captions_v2.srt`);
  const videoStats = fs.statSync(videoPath);
  const srtContent = fs.readFileSync(srtPath, 'utf-8');
  const lines = srtContent.split('\n');
  const textLines = lines.slice(2).filter(l => l.trim() && !l.includes('-->'));
  const previewText = textLines.slice(0, 3).join(' ').substring(0, 100);
  return {
    slug,
    title: `【${slug.split('-')[0]}】 ${slug.replace(/^mote-/, '').replace(/-/g, ' ')}`,
    videoFile: `${slug}_shorts_v2.mp4`,
    subtitleFile: `${slug}_captions_v2.srt`,
    videoSize: `${(videoStats.size / 1024).toFixed(1)}KB`,
    preview: previewText + '...',
    uploadURL: `https://studio.youtube.com/`,
    instructions: [
      `1. Download: shorts-output/${slug}_shorts_v2.mp4`,
      `2. Download: shorts-output/${slug}_captions_v2.srt`,
      `3. Go to YouTube Studio`,
      `4. Click Create → Upload video`,
      `5. Upload MP4 file`,
      `6. Add subtitles: Upload the SRT file`,
      `7. Set Privacy: Private (for testing)`,
      `8. Click Publish`
    ]
  };
}

function main() {
  const availableVideos = getAvailableVideos();
  const candidates = selectCandidates(availableVideos, CANDIDATES_COUNT);
  const result = {
    date: new Date().toISOString().split('T')[0],
    totalAvailable: availableVideos.length,
    todaysCandidates: candidates.length,
    candidates: candidates.map(slug => generateCandidateInfo(slug))
  };
  console.log(JSON.stringify(result, null, 2));
}

main();
