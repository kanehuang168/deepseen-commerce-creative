# Media review input

Build authority from confirmed requirements and observation from actual viewing/listening or reliable records, never from a production plan.

- authority.scriptHash: SHA256 of the confirmed requirements; observation.scriptHash must match.
- authority.audioMode: SILENT only for explicit silence, SPEECH for required speech, ENVIRONMENT for required ambient sound; otherwise unspecified.
- authority.checks: stable id and applies; eventWindowSeconds only for confirmed timing, in seconds.
- observation.mediaSha256: actual final file SHA256.
- observation.videoCoverage/audioCoverage: FULL, SAMPLED or NONE, truthfully supported.
- observation.speechPresent/audioMatchesRequirement: booleans only from actual audio evidence, not track presence.
- observation.checks: matching id, PASS/FAIL/NEEDS_EVIDENCE; evidence has kind=OBSERVED, startSec, endSec and descriptionZh. Despite its legacy key name, descriptionZh may contain the observer's English description. observedEventSec may locate a timing event.

Missing hashes/observations remain unverified. The script cannot establish whether the caller truly watched/listened. Do not pass credentials, internal generation prompts or full chats. --lang en localizes tool-authored receipt explanations; source observations are not rewritten. Use new output paths. Missing dependencies/read/decode failure is a collection/check failure, not zero defects.
