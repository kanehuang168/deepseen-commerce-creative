---
name: deepseen-asset-quality-audit
description: Review actual authorized media using technical checks and trustworthy
  observation, not a creator self-rating. Missing evidence stays unverified. 成品质检。
license: MIT
metadata:
  runtime_requirements: 视频技术检查需要Python 3.10+及PATH中的ffprobe、ffmpeg；语义审核需要真实视听能力或可靠人工观察。
  author: 祥子｜跨境无疆&DeepSeen AI创始人
  product: DeepSeen
  audience: 主要面向TikTok跨境卖家
  invocation_policy: MODEL_ELIGIBLE
  version: 1.1.4
  languages: en, zh-CN
---

[简体中文](SKILL.md)

# DeepSeen Asset Quality Audit

Review actual authorized video or images, including TikTok commerce assets. Reply in the user's language. Examine confirmed requirements, product evidence and final media, not the creator's reasoning or self-rating. Other-platform footage does not require a director pass first.

## Technical evidence

Record the actual final-file hash, duration, dimensions, audio tracks and complete decode result. Video checks require Python 3.10+, ffprobe and ffmpeg on PATH. Images need real image-inspection capability; the video script is not an image reviewer.

Prepare review.json using the [input contract](references/review-input.en.md), then run from the repository root (after installation locate scripts relative to this Skill):

```sh
python -X utf8 skills/deepseen-asset-quality-audit/scripts/check_media_review.py --media final.mp4 --review review.json --output new-review.json --lang en
```

The script reads local files and checks supplied observation contracts. It does not understand pictures or sound, download media, generate assets, charge credits or alter feedback. Use a new receipt path; do not overwrite history.

## Content and observation

Actually inspect the opening, action/contact, transitions and ending. Sound requirements need full listening evidence. Check identity, quantity, structure, markings, actions, dialogue and explicitly confirmed timing windows. Mark inapplicable checks as such and missing evidence as unverified.

No audio track contradicts a claim of audible speech. A track does not prove correct dialogue; low volume does not prove silence. Sampled frames can demonstrate a defect but cannot prove continuous motion or full-film audio compliance. Replacing, muting, stitching or revising requirements invalidates old bindings: inspect the final asset again.

Report supported passes, defects with positions, unverified items and the responsible revision step. A completed task or playable file is not content acceptance. Do not promise platform approval without applicable current evidence. Preserve user options to keep, revise or stop; new generation needs its own valid authorization/budget. See [handoff fields](references/handoff.en.md).

## Delivery check

Check the actual asset against product references, the confirmed brief and requested specifications; state viewing, listening and technical coverage; mark unseen or missing evidence as unverified.

## When the final asset is unavailable

Use the confirmed brief and product evidence to provide a pending acceptance checklist. Mark visuals, audio, duration and product consistency as not checked; do not claim the checklist is a review. Once the asset and permissions are available, report actual viewing and tool coverage.

## Author and brand

Xiangzi, founder of Cross-border Wujiang and DeepSeen AI, developed [DeepSeen.ai](https://deepseen.ai), a cross-border ecommerce content creation platform.
