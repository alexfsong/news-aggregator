# AI digest — 2026-07-20

## TL;DR

- China Flags "Security Backdoor" in Claude Code; Anthropic Pushes Back
- Moonshot AI's Kimi K3 Crashes Servers as Open 3T-Class Model Lands
- Claude Cowork Moves to Mobile and Web as 90% of Use Proves Non-Coding

## Trending


## China Flags "Security Backdoor" in Claude Code; Anthropic Pushes Back

China's security authorities issued an alert warning of a backdoor risk in Anthropic's Claude Code agentic coding tool, with Reuters, WSJ, CNBC, and CBS all covering the story on July 8. Separately, Malwarebytes reported that a hidden telemetry tracker inside Claude Code was described by Anthropic as an "experiment." Anthropic publicly disputed China's backdoor characterization and published a blog post on "an off switch for dual-use knowledge in AI models," apparently in response to criticism about safety controls.

**Why it matters:** The episode illustrates how AI coding tools — which execute shell commands and have broad filesystem access — are now geopolitical flashpoints, with national security framing on both sides.

Sources:
- [Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxQTmtuYVZDY0RoM0VTUW1Sa3poM1pYOHlYbVJwRk1lOXNPM1QwX25uMnlrdVUxUnlqSEhXZzlrWUxFQkRRa21HeEJWR1ZrY2UzeVUwdHBmcFR5bDR1OHNIQjRHNTZUYjd0NzJzZjNsQzdqNXRBUDZDdW1wekdXU1ZHcjNlbVVvM1NiSnJVQmppV2I3ZDNnSXIyZDBWMTZPQzhWTTRNUHo2WnZ0TG9RMzhmdjdBQnRzbUts?oc=5) — China issues 'backdoor' security alert over Anthropic's Claude Code
- [WSJ](https://news.google.com/rss/articles/CBMisAFBVV95cUxQQnhuNTk2eXJ6MFM2WmREY0pSNFN1REdpZXRFVU5FNElsTl9ZNFJ1YjFXQ084M19hN3FXWTFlY2ZDRnFLLWFXZGRybkhSa2hFbUtKRDJJUDR0QlNQcUZVZTVfOWRUUHRGenNleHFfcy1oS0NYVmN6QThLMjFBWF9qMDlwZ1hnNTE0cVAzNm1nNl9sOEVnM1Q0Vkg1WUNDQTlwUGVvWWsxRlVLVFNxS1ctVw?oc=5) — China Says It Has Found Security Vulnerabilities in Anthropic's Claude Code
- [South China Morning Post](https://news.google.com/rss/articles/CBMisgFBVV95cUxOellSU2ZVblNId0lhN2FnNXdkUjBkT2FhaUpEeUdNTkRHT0VjSC1IekFGVWtCVGpOTHRPYzZlYXZNMEVEZnZUSXBVMlluNHZVNGpwLVB4T3pQQWhmU3owZHdyWG16bkJ5OGNoQkZmRU1mSVp4NFFibnFCZEZ0MDdUNWpNTjhJRnh4Yk9TOE5ZZ2wwVkwwZ19vdTZoRGlvcmx0aVFKTVA3WTFTWXdaLTFCbF9n0gGyAUFVX3lxTFBsYk56aHEyeGRpdW9fbzBCSFl5dXNlTm9kSVF3c1k1aElJWVhWaDFFcE14M2ptVTBlbGpMdFdvOENxTmNQeThXeFhzb3llTjNkREl4YnQ3UkRPOFQtNk1yVzZlMzBVLUc1ZDhqZy1XU3ZCRnFJRnpjVWRNbnI0UTFZdlhBalhFRkpVWFlDNzh0QVVGVHdYYjBKb1F6c2hubkxBdUxQMWh2ZEVOblRfVFpiQXc?oc=5) — Anthropic hits back after China warns of Claude Code 'backdoor' risks
- [Malwarebytes](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPODBudnBldGVnY3pFRUhvS09kbC1oQ2FXUzhwT3VJZ2x2YmJSRXcwdjFhVlVsNHh0R3VVWTJUakNaUWpyc29BS1IwWTltR2VobUJtZVdWYnJFTGlDTEh6OHNEcHVCWnNfR1dhLTl2Qk1FNXVISGZhbk9pQUx2NXM5amFQQU9Fd0xxLWZzV0dIaHFzcEd0MS1mdGIzLWNnSGtyaDRIRWxTVDB4OTg?oc=5) — Claude Code's hidden tracker was an "experiment," says Anthropic

---

## Moonshot AI's Kimi K3 Crashes Servers as Open 3T-Class Model Lands

Chinese lab Moonshot AI released Kimi K3, a 2.8 trillion-parameter model it is billing as the first open "3T-class" model — more than double the size of DeepSeek's prior record-holder at 1.6T. Moonshot's self-reported benchmarks place K3 ahead of Claude Opus 4.8 max and GPT-5 on standard reasoning and coding evaluations. Demand immediately overwhelmed capacity: the company suspended new subscriptions within days of launch, and open-weights are promised for release by July 27, 2026.

**Why it matters:** A 3T open-weight model shifts frontier capabilities out of closed API-only products and into the hands of anyone with the compute to run it, putting direct pressure on Anthropic and OpenAI's premium tiers.

Sources:
- [Hacker News](https://news.ycombinator.com/item?id=48935342) — Kimi K3: Open Frontier Intelligence (2082 points)
- [Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything) — Kimi K3, and what we can still learn from the pelican benchmark
- [Hacker News](https://twitter.com/kimi_moonshot/status/2078855608565207130) — Moonshot AI suspends new subscriptions due to Kimi K3 demand
- [MIT Technology Review](https://www.technologyreview.com/2026/07/17/1140640/the-download-perimenopause-misinformation-china-moonshot-ai/) — The Download: China's latest AI leap

---

## Claude Cowork Moves to Mobile and Web as 90% of Use Proves Non-Coding

Anthropic launched Claude Cowork — its autonomous agent product — on mobile and web, expanding from its original developer CLI-only form. ZDNET highlighted that Anthropic's own data shows 90% of Cowork sessions are not for coding, suggesting the tool has evolved into a general-purpose long-running task agent. Coverage from The Verge, WIRED, and NBC framed the move as Anthropic competing directly with OpenAI's ChatGPT Work offering.

**Why it matters:** Opening an agentic product to mobile and web dramatically lowers the barrier to entry for non-technical users, putting autonomous AI task execution into millions more hands and shifting the competitive front from APIs to consumer surfaces.

Sources:
- [ZDNET](https://news.google.com/rss/articles/CBMihgFBVV95cUxPeS1WUVlvUTEtaU9vQW1UVVdSUW1tdE05dG9MQUEtV1ZGOWFnM0xrTW1oLXNuWEQ4MzJZQ0VRXzFLSTV1LW5EZzJILXF1N3FCcEVMcVhHeXRlUjBubzZUdDlrMExYcUp4cTk5RjlFQldBM2J0SE02QWZXYkc2c1lwRi1NMUFoZw?oc=5) — Anthropic's Claude Cowork heads to the cloud as data shows 90% of sessions aren't for coding
- [The Verge](https://news.google.com/rss/articles/CBMimAFBVV95cUxQdDVDSGhCMDRHZHRmVzJkOGI0ZkJwYmd5ZC0xVzJOemJaUk5ZVVNQNmRUVFJMdWdjOThSN2M2ZHE0UzBmSEUzQXdPR0VwTllxTkZ0X1A1bGQ3QkI5QVdlWmhIbjVSRW9hYkhZVnRZdFdrQVdGMmd3dTZ2SC1IekhqeHZCbE9FZXJfbkZ1S1NEN21jaDZRbHhxcw?oc=5) — Anthropic is launching Claude Cowork on mobile and web
- [WIRED](https://news.google.com/rss/articles/CBMiogFBVV95cUxQUUhySFRHNFhoWEhKQWJCaDYtR2hZbEZZS0dlNlctTjRtZ21KY1N4UVFGb21KdnFfUkJEUi1XTURfQzJ0VUhRYmlPZEJxUW9Ud2ZrMVZZeWQzSU01cEFpa3o5VXVpc0FtOW5ybjBwNFEtbEpUOXVuYk9QSnlqZXhmWXgwX0JYTXVPNnFBWUlMTm40UVdtTVVXX1BERlVKdEw5Z2c?oc=5) — Shut Those Laptops! Anthropic Puts Its Claude Cowork Agent on Your Phone
- [NBC News](https://news.google.com/rss/articles/CBMiqAFBVV95cUxObEp1eUMxeWdHeTdEZk93N2NsZmNBcDlwT3VObHZ3VkM0TDdOeERwTEJSeWpSUkZVRU15WnRWS1Fub0NtakpGUjVHRlFSQ3BjcWxjd01oSk0yeWJPdHZwNDktMXhZMDJKSml2NXhkYkVzTmVaZkUzUm9oWVhwTzYteEJ2WHA0clV2bXJRSGVPZXpUa3RoMnhJM3lTRWtrSWMxZFVjSThqcV8?oc=5) — Anthropic will make Claude Cowork available to users via the cloud

---

## OpenAI Launches GPT-5.6 with Microsoft 365 Integration and New Voice Model

OpenAI released GPT-5.6, framing it as "more intelligence from every token, stronger performance per dollar." Alongside the model launch, GPT-5.6 was named the default model in Microsoft 365 Copilot across Word, Excel, PowerPoint, and Chat. OpenAI also introduced GPT-Live, a new generation of voice models powering ChatGPT Voice, and rebranded ChatGPT's task-completion mode as "ChatGPT Work" — an agent that can work autonomously across apps and files for hours. Independent reviewers (AI Explained) suggested GPT-5.6 Sol may beat Claude Fable 5 on a price-performance basis.

**Why it matters:** Embedding GPT-5.6 into Microsoft 365 gives OpenAI the largest distribution surface in enterprise software; combined with the voice and agentic layers, this package move pressures competitors to match on both capability and partner ecosystem simultaneously.

Sources:
- [OpenAI](https://openai.com/index/gpt-5-6) — GPT-5.6: Frontier intelligence that scales with your ambition
- [OpenAI](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot) — GPT-5.6 is now the preferred model in Microsoft 365 Copilot
- [OpenAI](https://openai.com/index/introducing-gpt-live) — Introducing GPT-Live
- [AI Explained](https://www.youtube.com/watch?v=mWlCituW7wo) — A Model Explosion: GPT 5.6 Sol, Grok 4.5 and Meta Muse Rewrite the Rules
- [Hacker News](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6) — $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol (396 points)

---

## Anthropic Gives Teachers Free Access to Premium Claude Features

Anthropic launched "Claude for Teachers," a program providing K–12 and higher-education educators with free access to premium Claude features. The Hill, 9to5Mac, and Chalkbeat all covered the announcement on July 14, framing it as Anthropic entering the crowded AI-in-education market alongside OpenAI's existing teacher programs. Follow-up local coverage noted the rollout reaching Detroit classrooms.

**Why it matters:** Free premium access for teachers is a calculated distribution play — it seeds Claude into curricula, creates institutional familiarity before paid licenses are sold, and signals that AI labs view education as a strategic beachhead rather than a market afterthought.

Sources:
- [Anthropic](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5qdmFxWUxkdG9wTlNsZXE4ZVhfWUU0QjMtMmRvenk1cTVCb1B6dmgzMnR3ZWJRNGcxUWRiRDRGbVdzTkdWUUNIUF91Ml9ZZzVmTjRtc3dzNHdIWklWREUw?oc=5) — Introducing Claude for Teachers
- [The Hill](https://news.google.com/rss/articles/CBMifkFVX3lxTE9LZ0hrSDhsTHprNnhsc0tGSDd4aGpUQ095bmhWRHp6eTlrdmVzRHdtT1RqRUxOb1lXVmhMZlNDSG5sdUlKakR6b3hWQ1RvWDVmYlpvbUNKV3NEai1zX2FWdTdPenY1SkNFenJLbHpGQlU5NTZzT2lPclZHc1pWd9IBgwFBVV95cUxPVGg3MUxmUWp1TG5xbzZyN2VQVEZtT1p6MmNhR0lOdjNvN1N2NUh3dDlfSkdYaXAwWVoxTS0weWNOTlVNWERYdkdhdnlZWkt3LVRBQ0txc3FmaWdSNERqSmxWRjNWTnF4R05LWmdaZng4aTFXXzhyeE9FWkRBM0NIdC0xdw?oc=5) — Anthropic launches free Claude for Teachers
- [Chalkbeat](https://news.google.com/rss/articles/CBMitAFBVV95cUxOVVNCUzQtQlYtSTctLXNIUjAzRERaODhqcEplcFNkTTdxalZ3VUhhaFZzUFpYYUpoTDRZcGxjTzdNVXNENktfa1hRcENPQjZ2Qlo4V2NwMjA1Vnh1YVE4bU9sRTlwbUtLQkg1d1BjNk00cFpHSWNuMjJRSTk2MG5BLVdkTmtaZklNUW1FRmNvSmhqak5hOXB3aDBnZE5EUUR1YUY2ZlpBMVRTY1dpOWFwRkwzOG0?oc=5) — Another contender just joined the arms race over AI in schools
- [WDET 101.9 FM](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOaExwZW9pYjRBcXNiWEFDanhpMUIyTERFOW1TMEVrdS1qM185RVVIN3g0a2lIY21TYmNyd2d4OEEybXpnT2YtQnhEWnhIZ0Jtbjd0NTVSN2NmWXByRFNzWS11cFhDNDdlUTU4V1BCTjdCaWJ5eGtSR2JKdzF2N2R5UW1fY3Y4bno4dXJneG91R2pPRE8zLXdkck80OHFHNHZKa2UwaHQ5cVV0b3hCbUhqb1B4RmROTUxPcTFn?oc=5) — AI giant Anthropic bringing new artificial intelligence for teachers to Detroit classrooms

---

## AI Advice Makes People Less Accurate and More Confident, Studies Show

Two converging stories went viral this week. A widely-shared essay by consultant Nik Suresh documented executives setting $2B+ AI strategies without ever having used ChatGPT, and research coverage from The Next Web reported that AI-generated advice suppresses critical thinking — subjects who followed AI recommendations were less accurate than control groups yet rated themselves more confident. MIT Technology Review added a third data point: new research finds that LLMs are more likely than humans to form systematic hiring biases, and can generate novel biases not present in their training data.

**Why it matters:** The combination of executive AI mania and empirical evidence that AI assistance degrades human judgment raises serious questions about where autonomous AI decision-making is safe to deploy.

Sources:
- [Simon Willison](https://simonwillison.net/2026/Jul/19/ai-mania/#atom-everything) — AI Mania Is Eviscerating Global Decision-Making
- [Hacker News](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/#fnref:3) — AI Mania Is Eviscerating Global Decision-Making (404 points)
- [The Next Web via Hacker News](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study) — AI advice made people less accurate but more confident
- [MIT Technology Review](https://www.technologyreview.com/2026/07/20/1140655/ai-biases-hiring-humans/) — AI is more likely than humans to form biases when hiring

---

## Also noted

- [Claude make Fable 5 permanent](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) — *Simon Willison*
- [Fable gets another bump](https://simonwillison.net/2026/Jul/12/bump/#atom-everything) — *Simon Willison*
- [Anthropic Wants You to Pay Up for Claude Fable 5 - WIRED](https://news.google.com/rss/articles/CBMipgFBVV95cUxPRWFPUzFGbjVnQXpCQmh0d3BybFlmSnR1R0E0WUpLdXBVVTN6eENPajNoS25udGFHSmpITnptUWRScGlXb1o5NnNWMHNFY2pSRHpIS21hZGdpNi1PbHZ0NzJrVThQcDFNaVRSbGRJLVBSa21XX0RmTDBFOXNWRnhhWmdOVU1SV1Nsd1Z4N1BhRDFSSFVhWEdMM2ZaaVFDZlhGVkl6emp3?oc=5) — *Google News — Anthropic*
- [Here’s Why Anthropic Extended Access To Claude Fable 5 Extended—Again - Forbes](https://news.google.com/rss/articles/CBMixwFBVV95cUxPSXc2RnNtV08tVUtmMmdOUE1DbVVqM1ppYUpKX2YwRmtxZ2gtZU1oN1ZkX0pKVFNSTW5hLWJMaHV5T2I2V1BnZWNsVzd3UW53SXhuZ0V1S0VraXQ5bC0weGZWaDRqbFpwOWZpS1VGWjZSQ3hfT2xwUk9CNlBld1pSZXhVaV9hUDdEd2pCeGFwbTZwUHB0SVZjVk5QUTM3TmR6UlhsTUFFRXhqeG5vRmFHTWZURjVNVmIzUzZTSjlsbkVHV1BVMmJj?oc=5) — *Google News — Anthropic*
- [Claude Code uses Bun written in Rust now](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/#atom-everything) — *Simon Willison*
- [GPT-Red: Unlocking Self-Improvement for Robustness](https://openai.com/index/unlocking-self-improvement-gpt-red) — *OpenAI News*
- [Meet GPT-Red: an LLM super-hacker OpenAI built to make its models safer](https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/) — *MIT Technology Review AI*
- [The Download: OpenAI unveils GPT-Red and heat pumps rise in the US](https://www.technologyreview.com/2026/07/16/1140600/the-download-openai-unveils-gpt-red-heat-pumps-rise-us/) — *MIT Technology Review AI*
- [Anthropic Found Something That Shouldn't Exist](https://www.youtube.com/watch?v=0CqLVnx-2UM) — *Two Minute Papers*
- [Claude Just Revealed AI's Biggest Problem](https://www.youtube.com/watch?v=axOcn--n_lM) — *Two Minute Papers*
- [The Download: Claude’s inner workings, and the future of world models](https://www.technologyreview.com/2026/07/14/1140391/the-download-anthropic-claude-internal-thoughts-world-models/) — *MIT Technology Review AI*
- [Anthropic found a hidden space where Claude puzzles over concepts - MIT Technology Review](https://news.google.com/rss/articles/CBMiugFBVV95cUxPTVBLbm9aTGI4dlBYeGpyT2N4c3Zja214TUt2QllUQmswUzJTeXR4aWlsU25ibnJCaVlaZVFuMUtBbjBSQ0JEcjZfMnA1UE94cDBBdlBfbnZFY3RLR1Y0MjJrbVJNNjB6OUwyUTJRWXlYT1gtYTI2eGRDaDd1WThvZFYxaERDOEVYeS1UbU5iS0VjSmhUTExhajBDelFQSjUwdjFJd2ZoOEhkRmRBazZaYnRidzRlLUFEOHfSAb8BQVVfeXFMUFhtUFdVa1lqQk8zdFU3NE5QLTdrY0lFdERFRnRGNmtWMjNSdFhNSTF0M29qQnUweWc0Qm9HVEh3aWtGZUNuLVZHN3FmckxCZDJMYmY2ZC1OR0N0R1ZMcG5RU2tFdFlXYms3aEVyTjN2emh2YUVGUlRQRjh1MzBiMi1SUjlEOGVBUTlhaENnbS1lZXBHS3FvMS15YnFtdFZBa2xjQ3RqeWNCUHpOandrQnI1RjZSd2ZzN0RLXzZodm8?oc=5) — *Google News — Anthropic*
- [How Claude's values vary by model and language - Anthropic](https://news.google.com/rss/articles/CBMic0FVX3lxTE42R0NZbVlVSHl5WnhDQkFkTkVnN2pSMW5RQ3cxUDJNVWl4cVp3U1VFNVg0OVpzUmpjcnZ0aTN6WXIwY2YtaVdodENnSmdjanJMY21LM0ItOURxSFhsQ185UmdjejNzQTNRMDZiZUJpSjEwdVE?oc=5) — *Google News — Anthropic*
- [Twenty-nine countries sign agreement to establish global AI cooperation body - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxPTGF5ME1YRmJSTE42TWVWMDUyc1NkMlA2QVQxVlN6dkZuenF4RFcxSFlhUXk3eVZnUWZ3SzdZTDEzbTNVZzJ0NUhadERqUHQ1WmtvSl9aXzE1Qlh3UFdvR3ZXUmJDXzhycGJ0cUdtdXFVUFpzaTNWX3VBemlqUXh3UF95R2k5RTJKbjZFZ09MS3h0TUlnZ3FRMlN2T3lIc19qNGxLcmY1eTJwQVMyb2ZfNk03YjdST2hKRkg1TFFn?oc=5) — *Google News — AI*
- [The World Artificial Intelligence Conference Opens in Shanghai - sectsco.org](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9sb3BzQUZfMFR5Q1RveGYxNUUwVXVZbjYxcWJSMnBrMHR0LXRITGQ1T2JFMndTUmt5aUFvNXVtaWI3NFpRcWR2bXl0QWgyRURlUDZRWDluSEQ?oc=5) — *Google News — AI*
- [Guterres: AI must be shaped by 'all of humanity', not a handful of powers - UN News](https://news.google.com/rss/articles/CBMiV0FVX3lxTE90ZmtpdEdJek9jcFc5ckwyYUhybVNaZ2dseFYtRmxWcEtyNHg5UDNWVWZndWdsVUpySUYwTnA1SG10UjRnbzlvQ3VXNjlJa09yTHZBWUNmTQ?oc=5) — *Google News — AI*
- [Prioritize Equitable Capacity, Safety, Sustainability So Everyone Benefits from AI Revolution, Secretary-General Tells World Artificial Intelligence Conference - UN Meetings Coverage and Press Releases](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9aaG0tcUVyajVqZFJRaFQyU1M4Z09fXzYtVHJXZmN3aEs3blI0V29KbUF2MTRnZEM2OUhSdDkxM1B1YXV2Y3FzWEp2TFZZRlJqTE1jVVI1Qmd0dw?oc=5) — *Google News — AI*
- [Welcome Inkling by Thinking Machines](https://huggingface.co/blog/thinkingmachines-inkling) — *Hugging Face Blog*
- [Inkling: Our open-weights model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) — *Simon Willison*
- [Security incident disclosure — July 2026](https://huggingface.co/blog/security-incident-july-2026) — *Hugging Face Blog*
- [Quoting Sam Altman](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) — *Simon Willison*
- [SQLite Query Explainer](https://simonwillison.net/2026/Jul/18/sqlite-query-explainer/#atom-everything) — *Simon Willison*
- [nascheme/quixote](https://simonwillison.net/2026/Jul/18/quixote/#atom-everything) — *Simon Willison*
- [LLM cliché highlighter](https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/#atom-everything) — *Simon Willison*
- [Spot birds not golf](https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything) — *Simon Willison*
- [Firefox in WebAssembly](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) — *Simon Willison*
- [Quoting Thibault Sottiaux](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) — *Simon Willison*
- [Mermaid to ASCII art (mermaid-ascii)](https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything) — *Simon Willison*
- [Quoting Linus Torvalds](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) — *Simon Willison*
- [Mermaid to Unicode box art (grok-mermaid)](https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything) — *Simon Willison*
- [xai-org/grok-build, now open source](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) — *Simon Willison*
- [How I tricked Claude into leaking your deepest, darkest secrets](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) — *Simon Willison*
- [Quoting GitHub Changelog](https://simonwillison.net/2026/Jul/14/github-changeling/#atom-everything) — *Simon Willison*
- [simonw/pedalican](https://simonwillison.net/2026/Jul/14/pedalican/#atom-everything) — *Simon Willison*
- [lobste.rs is now running on SQLite](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) — *Simon Willison*
- [Quoting Armin Ronacher](https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything) — *Simon Willison*
- [datasette 1.0a37](https://simonwillison.net/2026/Jul/14/datasette/#atom-everything) — *Simon Willison*
- [Using uvx in GitHub Actions in a cache-friendly way](https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/#atom-everything) — *Simon Willison*
- [DOOMQL](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) — *Simon Willison*
- [datasette code-frequency chart on GitHub](https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything) — *Simon Willison*
- [Directly Responsible Individuals (DRI)](https://simonwillison.net/2026/Jul/12/directly-responsible-individuals/#atom-everything) — *Simon Willison*
- [shot-scraper 1.11](https://simonwillison.net/2026/Jul/12/shot-scraper/#atom-everything) — *Simon Willison*
- [sqlite-utils 4.1.1](https://simonwillison.net/2026/Jul/12/sqlite-utils/#atom-everything) — *Simon Willison*
- [A scorecard for the AI age](https://openai.com/index/a-scorecard-for-the-ai-age) — *OpenAI News*
- [Why teens deserve access to safe AI](https://openai.com/index/why-teens-deserve-access-safe-ai) — *OpenAI News*
- [How Cars24 scales conversations and builds faster with OpenAI](https://openai.com/index/cars24) — *OpenAI News*
- [The US is advancing AI safety through state and federal action](https://openai.com/index/advancing-ai-safety-through-state-and-federal-action) — *OpenAI News*
- [How to manage AI investments in the agentic era](https://openai.com/index/managing-ai-investments-in-agentic-era) — *OpenAI News*
- [How sales teams use ChatGPT Work](https://openai.com/academy/codex-for-work/how-sales-teams-use-codex) — *OpenAI News*
- [How data science teams use ChatGPT Work](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex) — *OpenAI News*
- [How Deutsche Telekom is rewiring telecommunications with AI](https://openai.com/index/deutsche-telekom) — *OpenAI News*
- [Getting started with ChatGPT](https://openai.com/academy/getting-started) — *OpenAI News*
- [GPT-5.5 Bio Bug Bounty](https://openai.com/index/bio-bug-bounty) — *OpenAI News*
- [Our approach to government and national security partnerships](https://openai.com/index/government-national-security-partnerships) — *OpenAI News*
- [Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations) — *OpenAI News*
- [Helping K–12 educators build practical AI skills](https://openai.com/index/k-12-educators-practical-skills) — *OpenAI News*
- [MUFG aims to become AI-native with OpenAI](https://openai.com/index/mufg) — *OpenAI News*
- [Australian Payments Plus moves faster with ChatGPT and Codex](https://openai.com/index/australian-payments-plus) — *OpenAI News*
- [Our approach to bioresilience](https://deepmind.google/blog/our-approach-to-bioresilience/) — *Google DeepMind*
- [Empowering India’s next generation of innovators with ATL Saathi](https://deepmind.google/blog/empowering-indias-next-generation-of-innovators-with-atl-saathi/) — *Google DeepMind*
- [Fine-tune video and image models at scale with NVIDIA NeMo Automodel and 🤗 Diffusers](https://huggingface.co/blog/nvidia/scale-diffusers-finetuning-nemo-automodel) — *Hugging Face Blog*
- [Newer Models, Same Advantage](https://huggingface.co/blog/Dharma-AI/newer-models-same-advantages) — *Hugging Face Blog*
- [What building Shippy taught us about building agents](https://huggingface.co/blog/allenai/shippy-tech-blog) — *Hugging Face Blog*
- [Model Routing Is Simple. Until It Isn’t.](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt) — *Hugging Face Blog*
- [Introducing Real World VoiceEQ: Measuring the human quality of voice AI](https://huggingface.co/blog/real-world-voiceeq) — *Hugging Face Blog*
- [Profiling in PyTorch (Part 3): Attention is all you profile](https://huggingface.co/blog/torch-attention-profile) — *Hugging Face Blog*
- [Native-speed vLLM transformers modeling backend](https://huggingface.co/blog/native-speed-vllm-transformers-backend) — *Hugging Face Blog*
- [From Hugging Face to Amazon SageMaker Studio in one click](https://huggingface.co/blog/amazon/one-click-to-sagemaker-studio) — *Hugging Face Blog*
- [Hugging Face Models on Foundry Managed Compute](https://huggingface.co/blog/microsoft/foundry-managed-compute) — *Hugging Face Blog*
- [Run AI workloads on any cloud, store on Hugging Face: zero-egress storage with SkyPilot](https://huggingface.co/blog/skypilot-hf-storage) — *Hugging Face Blog*
- [LeRobot v0.6.0: Imagine, Evaluate, Improve](https://huggingface.co/blog/lerobot-release-v060) — *Hugging Face Blog*
- [PRX Part 4: Our Data Strategy](https://huggingface.co/blog/Photoroom/prx-part4-data) — *Hugging Face Blog*
- [Import AI 464: Fables writes GPU kernels; AI automation; and analog computation](https://jack-clark.net/2026/07/06/import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation/) — *Import AI (Jack Clark)*
- [NYC may require landlords and realtors to disclose the use of AI in listings](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/) — *Hacker News (AI, 100+ pts)*
- [What AI did to stackoverflow in a graph](https://data.stackexchange.com/stackoverflow/query/1953768#graph) — *Hacker News (AI, 100+ pts)*
- [Why do AI company logos look like buttholes? (2025)](https://velvetshark.com/ai-company-logos-that-look-like-buttholes) — *Hacker News (AI, 100+ pts)*
- [Kaiser nurses say AI, surveillance are making their jobs and patient care worse](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/) — *Hacker News (AI, 100+ pts)*
- [The state of open source AI](https://stateofopensource.ai/) — *Hacker News (AI, 100+ pts)*
- [AI Meets Cryptography 2: What AI Found in OpenVM's ZkVM](https://blog.zksecurity.xyz/posts/openvm-bugs/) — *Hacker News (AI, 100+ pts)*
- [LM Studio Bionic: the AI agent for open models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) — *Hacker News (AI, 100+ pts)*
- [German AI consortium releases Soofi S, an open 30B model that tops benchmarks](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/) — *Hacker News (AI, 100+ pts)*
- [Detecting LLM-Generated Texts with “Classical” Machine Learning](https://blog.lyc8503.net/en/post/llm-classifier/) — *Hacker News (AI, 100+ pts)*
- [How to Train a Gen AI Kick Drum Model on Your Old Linux Desktop with 6GB VRAM](https://www.zhinit.dev/blog/training-a-kick-drum-diffusion-model) — *Hacker News (AI, 100+ pts)*
- [Generative AI Is an Engineering Disaster](https://www.theatlantic.com/technology/2026/07/generative-ai-engineering-disaster/687901/) — *Hacker News (AI, 100+ pts)*
- [The LLM Critics Are Right. I Use LLMs Anyway](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/) — *Hacker News (AI, 100+ pts)*
- [Stop saying that AI is just a tool and it only matters how it is used](https://www.frank.computer/blog/2025/05/just-a-tool.html) — *Hacker News (AI, 100+ pts)*
- [LLM Networking with MikroTik](https://blog.greg.technology/2026/07/14/llm-networking-with-mikrotik.html) — *Hacker News (AI, 100+ pts)*
- [We don't use AI in any of our design or production processes](https://mass-driver.com/article/from-human-hands) — *Hacker News (AI, 100+ pts)*
- [Minecraft Was Missing One Brilliant Idea](https://www.youtube.com/watch?v=Ae9q7KsRbuI) — *Two Minute Papers*
- [DeepSeek's Absolutely Insane AI Speed Hack](https://www.youtube.com/watch?v=1yBU41auQhw) — *Two Minute Papers*
- [🔬 The Lab of the Future Should Feel Like a Data Center — Andy Beam & Rafa Gómez-Bombarelli, Lila Sciences](https://www.latent.space/p/the-lab-of-the-future-should-feel) — *Latent Space*
- [Why AI Infrastructure must evolve for Agent Experience — Akshat Bubna, Modal CTO](https://www.latent.space/p/modal2026) — *Latent Space*
- [The Navy’s Strategy to Weaponize Data and Artificial Intelligence - USNI News](https://news.google.com/rss/articles/CBMingFBVV95cUxNbllHMmU1TG5zWTVnQ0VLMnl2TnZPT2lEQ3ZPcXFtcjQ3Ti1XcFlyRTJHWFVXN2xuVmVwV3NDMkpmN2xfQUx0MXJtczZnTTZzMkF5S0hnb21GdjFSeGVvdFFjZlNwUkFpQzY0OFVvZkxiSmVaUXdDMVlpcFM5dTcyM0FZRTVYRVpjeklWTERMQWJhZGJmUmMxNVQ3ZkhqZw?oc=5) — *Google News — AI*
- [The Hidden Cost of AI-Assisted Creativity - MIT Sloan Management Review](https://news.google.com/rss/articles/CBMihAFBVV95cUxPbU9VNVFncVVmWGxvNnBLRmM3dEwxczUzSFRDSXhIdzJQTkJSUWdhb0lmS0xsdTl6cWszeG9GSGNocmt2cWRnWlpzaEh2TjU0MHZic0NHMThGa3RDeEpRLTZYRVZLRVZUNmxoVlJMMXJCTHphcm5WRFp5NHlkWUZhTHNaQ3Y?oc=5) — *Google News — AI*
- [What Marx Can Tell Us About Artificial Intelligence - Jacobin](https://news.google.com/rss/articles/CBMickFVX3lxTE1SSVV6c1BEamQxby1ZaTlLMGRDbFFLS3JEYlB2dWRfdWIzeFA5QldNUVBWODJ1cVREZDR4X0Fmc1ExZ1l3bGRkdDQ0bmZPdVNJS05Gb0VGazJ0b2p4cmFkM1lROW93LXQ1LW95RmNxdEstQQ?oc=5) — *Google News — AI*
- [How Will AI Affect Cyber Operations? - RAND](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBOMmVWUmlTZVVaSDRyclNKTy1ZUnY1NWRFa1hWTGR5bnoxOXlVbjhPcjlYT3FoVVFnYk5aYjNpVXdBXzhLY2xkT3BoSElrWUtvY29sNm1jZUQtekZ3bnF0bUVwYw?oc=5) — *Google News — AI*
- [ALA Council adopts Guidance on the Use of Artificial Intelligence in Libraries - American Library Association](https://news.google.com/rss/articles/CBMinwFBVV95cUxPRnVXa1V5V3BGSC1XbWVlcHNJUDdldmJwWjRFczhNYk1BajJpYW53ZXJZeHdkYmplZXp5UGtFXzFCNGRYWWtPalpiek1ZUENYLXBDWHdIZzFzY0FCOXJaVnZENTJfNTBjYTdTZ3FVVlY1OC1Wc0F4TlcwOWw1SnlFRDRlUE1GcVZZaEJIZGxSVFRnSjhvalNOdjdTVWktY3M?oc=5) — *Google News — AI*
- [What can the 38th Church Doctor teach about artificial intelligence? - Catholic Diocese of Wichita](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPcFEtaHlMQklINnBUaU1tNU1TeERLMzFVSkFFb2JJVlpBbWRieHIzREtwS2l6NHBueC1qWHY5Y3Q5OWYxM011S1pOTkJWTWpmVlQ2WFBZaklnVkVvZzJWWDdkaXlCZEhyYjloMEI4bVV2VE0zZGQwWTBBTGFHUk1qYjJ2ZWlIRGY1b1pUSGY3QmVUU0Z2UG9TaUZ4dkRMT2lyb3hNYU5FY1I?oc=5) — *Google News — AI*
- [Artificial intelligence and the future of African mining - Atlantic Council](https://news.google.com/rss/articles/CBMivwFBVV95cUxOUFQ5RzI3RzlNWTFRLVQ3R3pmWkxOclJreFozN05iWkVIdWxYSUZ1Nlg5clYwVHd2R0xQYm5hUnRVNkM1NnQ5Vy1jUVhzZ0pHUVY2aFlibXUtUkdUeFVYb2xiUEU0a21xRFZieWNaZDViT2NtNE1PbWZybmRuUnNLeWt6ZEtrcDNUYUZGNmstaENMSFk5SGRicElXMVVHVEc2ekFfNWw0akdvLVRjQzlsTE1MOWoyX3V6YjhrUGM4NA?oc=5) — *Google News — AI*
- [FSU chemistry professor develops artificial intelligence songs to help students learn complex concepts - Florida State University News](https://news.google.com/rss/articles/CBMi8AFBVV95cUxONzNLRFhLeGpmWDEyS0V6VTNoS2hIZHJfN056TmlTSy13MlZfOFdZU1RWNFlGX3FyWmNiM2ZyT1V6R2QwTzdSNDl6Wmxzb3E2dXpndjFRTUxUT2JacUYyelAwTmJXWXBldlN2T09aaW01LWFnS0pzNFQ3dm1GLVFadHpZeFJuV1ZqQjN1RmpPcE1LRm1SM3gtcGNseXFvM3AyMTZsZUVoQ1lnR1BBQjk1czF1ZEpRNkZpSkxFbVNsVk1jekxHNk8wUmdraU5IOXFYR0dkdG1yV1VfRzRSVUhmclIzV3VYeTlMeExRdkNvLXk?oc=5) — *Google News — AI*
- [Morgan State University Launches Artificial Intelligence Degree to Prepare Students for the Next Era of Innovation - Morgan State University](https://news.google.com/rss/articles/CBMif0FVX3lxTE9fVVc1WUVaNzM4TEZsQmV3Zlg3RmNGS0JaX3MzdUMtQVVOcm5ZTkFuNUs4bEpmdlFRMS03dWlreGlTaVpwR1pLWkFJNnRJQzRITnpjRnhVZnQ2WUxGcU1fOFN0RUhfNWx2dXpzeFVBY2J0MUtGanYySDNhOXhIYzQ?oc=5) — *Google News — AI*
- [Artificial intelligence companies are coming to New York City - marketplace.org](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNalNWYnNTSGdQZjRJbTV2ZTYzZVVZd0swT1pVVERKMDAyaFRjVVpmeUd0dmtqQ2VJOEU0MUtTM1R5cmg0R3VsM01DYXVDaUVtZnlsaXdUY1NXaWJkb1dhbGdEUkhRXzQ5RUYxcVZuZ1NhenlkYk9rTm80VGg3UXdnSzlCZVQ1eDRHVWZuM0hkbEJSVUFiOVdHTDd3TmZWOHoxcTVfdXAxVnZ6QQ?oc=5) — *Google News — AI*
- [Nunn Introduces Bipartisan Bill to Put Artificial Intelligence to Work on Iowa Farms - Congressman Zach Nunn (.gov)](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPbnI1SGJnZnhCWkVVTE00QU1aRHRBMFlJUmZBMzF2bFVBdWFWeDY2ZEhoMlJUaDVweEdNVmh4aFB4a1ZtSk9ZaE9sREhLeWlvcDJPdVE0QlNyeXlWbHZfMVl5Z0F6NWxSTEFYWXMyVUUxc00yT2RINVczU3VrdFVEMXV5M1YwOGk0QXJOTFo2TUtJTGVZd3lESlVTVGRuQWg4RzVGTGdnQ2p2a0h0cWFBTWV1V3Z6MzhmS2hr?oc=5) — *Google News — AI*
- [UH Professor Uses Artificial Intelligence to Make Roads Safer - University of Houston](https://news.google.com/rss/articles/CBMiekFVX3lxTE5ETmN4OGNRTi0wa0xxbl9TQ1NjTjR6cU14YmdXenVTenFRRTFPT0Z0ZmxzNXo1QXRPSExNTXRFWldteEVXeFhrbzFZZnNjLVBDNWpJYjF6bWIweE9DSFdhZ05FRzBkV3V5cHlDMzVRSFRpWVh3OHhWOWlB?oc=5) — *Google News — AI*
- [Artificial intelligence, information technology, and employment, 2024–34 - Bureau of Labor Statistics (.gov)](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNWUpCVHNwVEVhak5Oc2pnUTRGYXFWREtZeVJsUElOOTFfbkxmYjZfY0p2bm5lMWdoU1ZMQURMNDNKaTFEODNjRkNETjRzXzBnNFIwUHVqOUs0QlpmR0Z6R2xiYWZVS0pia3dnM1ZfSi13UFFqX0daLUM5XzNEUHRsTEpWN2ZfZjZzakdRVGF0WjNFS09Wd1ZNdzdwWm5EbTdaLXp2VzVhZHJhaDQ?oc=5) — *Google News — AI*
- [Artificial Intelligence is Easily Fooled in the Search for Life - Universe Today](https://news.google.com/rss/articles/CBMipAFBVV95cUxONDZkSm4wM29rUzB3R2dfNnRTcnJYZ2JCcXNqcFExblh1NjJ3TjVmVzlya2dkTHVGTEVkZ0g1WTlyZEsxekQ2NlNRTkFSNGU1cjNXQ1JyWTVMZXNNWjliRFZGUG5ZdTBlc2hERjVGcGxMclhHc0ZDdmN6dndISGVtQUxMdm42QWtmQWJuWGZSUGt4T0R2Si1LcXFOM1dsaFQ3VmREVQ?oc=5) — *Google News — AI*
- [The Case for Nationalizing Artificial Intelligence - Jacobin](https://news.google.com/rss/articles/CBMidEFVX3lxTFBZOG5TTC0tUldnVzlLUkZGU3R0ejdlSXBsODJ3aDRfZUF4N1h6czA1SU1ZNzF2TDFDTFd0R0J3MlZxbmllMDNZU2x2ZWpiR2xaWmhPV2U1WTRpb0FkSTRKZFNnTFMzWjBpTTREZmEta3pXV1lw?oc=5) — *Google News — AI*
- [Strategic Autonomy in the Age of Artificial Intelligence - RAND](https://news.google.com/rss/articles/CBMibEFVX3lxTE5ybU5PdFVpYmwtT1JmMmdSOGp5QWl2Qm83djVTQnZ5MXBIVGUxblB4amktdDg2ekZYSmhTMk5IcFJlbG1pSUk1REV6bU5VYTdnZUl1X3VMR01OS2tlNjJ5ODZodWJrQzhfZmNBZA?oc=5) — *Google News — AI*
- [Artificial Intelligence Poised to Rewrite the Crop Protection Playbook - AgWeb](https://news.google.com/rss/articles/CBMirwFBVV95cUxOSERhTC1ETF9JbHZkbDdNTDQtNUpVdVRQN3JNM21Zam05NE1ZUkJBWUdpTTNZdVVxcGVYSklTdmhLMWQ5dGNlZXpvbi1ZRnJUZUN6bHM3c0k3RlUzZTlFT1JSX09xTDZtRzVMdmJpSEh4akQ1VGRtQVl2bk1UNmNqWDRDX2tRNmVueHhBYkNwZDhWTzhsUlUtREtFT2RiY0Nhd1BUTkVXUkRiVF9zMXdv?oc=5) — *Google News — AI*
- [Artificial Intelligence Lightning Talks - Iowa Now](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBVRlRYbXVlY1ExVWZ2Rml4MDE2MnNaT3V5R3RvNDNjVWNBNkxZS2preHBZZXJfdXFHLUVKRzRPN2NJM2xlVTNGekxZaw?oc=5) — *Google News — AI*
- [Artificial Intelligence Infrastructure Hits Bumps in the Suburbs - Princeton Perspectives](https://news.google.com/rss/articles/CBMioAFBVV95cUxQMGVfTkZNUzh6cnhVOUxSMXFXQlYtOHZ3aWZLaGNLZnpBZUFKOHVOeG52NS0wYVlvZDNLNXBaOEk1UmF0cVNkMndKbkl5R1B5T3NWOXg5RzB4TWhHOXBEMTFRcTJpWFAxQ1lXNDFzWDg0dHJGR19tbE9nVmt5ampYRENSeTZ5T3R6SWJyNFlOcUx1SlIwMWtieGhnY3Bfbmdu?oc=5) — *Google News — AI*
- [Mass-produced science is coming. What happens to scientists? - The Transmitter](https://news.google.com/rss/articles/CBMitAFBVV95cUxNb2VrZ3FidnBSdm5FT0Voa21tU0JmT09VTmtHTDdJOGM5ejF6Y2tTblhxM1ZxaVptb2k1TTdESlVNbk5Fa254TDRiRlViTW13bFJfZzhIR3dhSmQ3OGZNeVNzdTNYU2xCSDB5MHltSW53Rm40dTFhSVpjTW02cXNocmtEc2Rvbk1FdUo2YmlLVVpNZ2pFY01FN3ZGRlFXZjNOeXlXd0RFc28tOUVIZ1pFSFBHMjA?oc=5) — *Google News — AI*
- [Can the government require ID before you use artificial intelligence? - FIRE | Foundation for Individual Rights and Expression](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQOG5OREdPWkZoMWR6RnlITFQ3SXAtN2E5LW5KRWdTM0xNZXFXSGZFSFlsdjduVTBZMDlwQjlwcG95ZERTcjByR21tQ01BRVdtaUdXU2xJYjJiZDlZbnFJVndZR3h4SWJSN2YzdHFueDFNODBKSUxEWUI0RzlaWlVaV2h4UnJ2OG9oWkY0?oc=5) — *Google News — AI*
- [Humanity at the Threshold: A Declaration on Artificial Intelligence and Nuclear Weapons - The Elders.org](https://news.google.com/rss/articles/CBMiowFBVV95cUxNVk9SUW1mVmQtNVJpYjJydWhDWVlGRGtFMU1jSTRKUXVkblo1OXl3anduN3FsR0kzb0pubVRveEcyY3ZCOFV1NG9zUVpKWmVnNnBYTEl2cVZJblJkVnhzWlB6TDVDMkZIVjVKQmN5WHpaR0p2c3FLZEZYcWN4VUVHaUJUVUlzY2pVNkZhOFZEZGZQa1ZMNmFjYmFKdVAwUkpHZWZj?oc=5) — *Google News — AI*
- [Wasatch County sets artificial intelligence use guardrails - KPCW](https://news.google.com/rss/articles/CBMisgFBVV95cUxPNGt6NU9XbWZXNnQ1WjBST2VsRk1IbkhsRzFpZ3FoYzFJc2JGS0d2VnUwVjVXUzR5azBUUjM3ODJzTFJmaUJ5OXZESVlTdUFHUXZSRDdXV2VQYjFkelEzcE5QcG1jSHhUdDVqZWNDNnZha3h3R3hVcFpkN1BzTUZzb1c0bEJZWFZUZU9ReGgxRXFSUjJJMTB3UGdfcXh1THJDdzVfVmZSUElnQnN3YlczZ1J3?oc=5) — *Google News — AI*
- [Is artificial intelligence coming for California jobs? It depends | Opinion - Sacramento Bee](https://news.google.com/rss/articles/CBMiYkFVX3lxTFBNRU9UcFVQN1lIODVCRXBJYkdHRkN0a0tYUWctZ2NIbHlSOENJMXlKRGw5Y3NTa0FmeFNiamVLNk5HdFpUdzZJUTE3QzJXcjd3eHFxUzlNR1d6SlB3NFJMbFJ30gFiQVVfeXFMTVVROWlFbkEyaWNGNlNXNl9DMTUtMDFadFlIYnNZTkRqYmFzRWlrMlJJanNhX0ZFQmZHcm1jb2NuaHJRMXVFNlhzczZ1T0s3NUJjdkd3ZU1KNzBHRTVSWXgzMVE?oc=5) — *Google News — AI*
- [Opinion | Code Is Free Speech. Seriously. - The New York Times](https://news.google.com/rss/articles/CBMidkFVX3lxTE1NUXJYdDFkLUdfcUNoaWlhZjdmSFEwaFpxSWRBZ3RQeTlZaEtPQndESGduWmk3Z1dHWWFzV3BzMGFqQVE2aUJFSWZEU1NZeXl3VEtmQ3hrem00aDJ1UzVydHlQdkZMMElLT2RBaGxndnc1c0g4TXc?oc=5) — *Google News — Anthropic*
- [Anthropic bets bigger on healthcare with Optum tie-up, UST integration - Fierce Healthcare](https://news.google.com/rss/articles/CBMinwFBVV95cUxPS2FCbGtPRjM4V3JaWHpLeGc2Q0Q0M0pmQzNXdnFnQVFCVVVjMTZvMkxlcTgtNkh6Y3llZEcydDRvSWVsaHB1bEtuLUlzWWxMLTV5TVc4bGpvcENSUDNHZmdyRTlDdWdOeFY1THM3RXNFZ3RUVl9LMWozSzVoNjRSdWZkM2pZcmhFdEpxVVZSWlpZS3VoVnpjWjR6bTFkQzQ?oc=5) — *Google News — Anthropic*
- [Introducing a way to reflect on how you use Claude - Anthropic](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9uQmgzMW5SUGNxN3VQLUJmU3YtcEhCVXpyUl9aOVRMVEFDZU94NGJyVS1yV1NUMGoyY2Fycm1iamhuNVBNUlFEQjd2djFiRGRXSmRiZW14akhXdS1XZlNB?oc=5) — *Google News — Anthropic*
- [How Claude Performs on Robotics Tasks - Anthropic](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE91VmFtc1pJZHh6Nmk0MV9TQy1LWmRuTGxwdUlSSkljREEzYjRzSXRnX21tOWxfdFg5QlRDYWNkMUZyRVUtR0xmZXc0UEFPM2tVSU1JZ09OVWFYZ3ZucGdkVzR4TldYeGM?oc=5) — *Google News — Anthropic*
- [Inviting hard questions - Anthropic](https://news.google.com/rss/articles/CBMiWEFVX3lxTE0yeHlpRmsxaGNhVGwxREszVzFIZHh1T05XS0F2c0JrczVmd3hBaWNnMjB0N0xSYTdRd2hxREp2OGF4SEtDemFEanpLZVNlSFRSSThuQVBXMFY?oc=5) — *Google News — Anthropic*
- [UST is bringing Claude to physical AI - Anthropic](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9PWmhDajNFV09GX2ZrcFpRTHJUcFdwcFZDRDFvMlQ5MGhpclVkR1dYSFI4MllXTWRkaTR5cEhQN0RvcmFRVTVicXpxbUZkc2lDUTZj?oc=5) — *Google News — Anthropic*
- [Anthropic starts localizing Claude pricing for India, its biggest market after the US - TechCrunch](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPQmFacXVma1BoV2RmOXgwdFdpdEhlOHphVnVyWk5RRGxJYWpmM0t4d3BpUEpnRGNQbGJSTVZLeWdXdlJEZlV0QXdtRGJxMmR6SzJTN0JSUWdQMWFPemJMbnBjTUNPLThnaVFQTzMtdGQ0NEtoUUNmODdjaHZ1aWpHeWkzeXdfY2VsOWtiVU1WS2NieTQ4Umt5cnZvZl9HOFRLVVpTNXJIdXQtZUo1eGNNWDJIVjY0Z2FSMXZn?oc=5) — *Google News — Anthropic*
- [EXCLUSIVE Canada regulator cited Anthropic's Claude Mythos in warning to banks on cyber risks, email shows - Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxNVndVUlFjeXZyV1lrNVRsZzJEVXdIUTEwRmdBclIyMDJlRmVGcUNGREdVMVRIQ1l3NWpmNXM5UTdtV3RCZW01V2h5dk1VUy1OU3ZQSDk4b1I0Z0xybEQ2N0lkZUtOLWpvYnFEUWRNVEsyWnIydUtDZXY1cGN0T0RSM25oblAyVG1EaHR5WG9oUXVtRXFPWVR1M3NET1BMZ05mOE0yclA0eDFXTTBLS01wUEx2dG5qUGN4MWJtbWpB?oc=5) — *Google News — Anthropic*
- [Anthropic’s Claude Science is coming for Kendall Square - STAT](https://news.google.com/rss/articles/CBMiggFBVV95cUxNamNka00wWVVwR3hkZjdWUThuZDZRbDc4LXZxYVE3eFZlbjRIQy1sbXRtVUQzX1IzdmFrUktBM3RUeHVNTWZwT25wd29iVFZGZVI3TGJweEVVVjQ4cnNNa2REY3l4UWZrZkFIY2Z5b1BDSkhHdVlFX2NZcUgtQ0ZiWUt3?oc=5) — *Google News — Anthropic*
- [Anthropic Just Gave Its AI Coding Tool a Built-In Browser—Here’s Why Users Will Love It - inc.com](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQbFBRU053WVRiX3NPQ0FBdHJzNUxJMk9xY19CMEJkUFZ3LVk5UjctQm9FM2tlSzAxMHo2WnBBdnJzVjRjWk1RemZGSk9SMDk2TWZLNmt4YkhRTDBhRDFGbjVjM1ViRmVHeVZ5cEc2WlhBNzQ1bmZnNDh3NXZBb0phUzg2UktJUW10ZWNHTHQ4a0xCUVN4NjJsSXNpRVctTHN2NWdkNTFndTRtZldhMXdlY3kyUk5YcTNsdEc1U3h4NGNhLWc?oc=5) — *Google News — Anthropic*
- [There’s a lot of hype around perimenopause. Don’t buy it.](https://www.technologyreview.com/2026/07/17/1140608/theres-a-lot-of-hype-around-perimenopause-dont-buy-it/) — *MIT Technology Review AI*
- [The risk of weather data sabotage is rising](https://www.technologyreview.com/2026/07/17/1140622/weather-data-sabotage/) — *MIT Technology Review AI*
- [Why heat pumps are still so hot in the US](https://www.technologyreview.com/2026/07/16/1140505/heat-pump-sales-us/) — *MIT Technology Review AI*
- [The Download: a useful quantum machine and a record-breaking subsea tunnel](https://www.technologyreview.com/2026/07/15/1140498/the-download-useful-quantum-computer-subsea-tunnel/) — *MIT Technology Review AI*
- [PsiQuantum has a plan to make a massive quantum computer out of light](https://www.technologyreview.com/2026/07/14/1140356/psiquantum-plan-massive-quantum-computer-out-of-light/) — *MIT Technology Review AI*

