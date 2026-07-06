# AI digest — 2026-07-06

## TL;DR

- Anthropic Launches Claude Science, a Standalone Workbench for Drug Discovery
- US Lifts Export Controls on Fable 5 and Mythos 5; Claude Sonnet 5 Ships with Silent Price Increase
- Anthropic Accuses Alibaba of Illicitly Extracting Claude Capabilities, Tightens China Access

## Trending


## Anthropic Launches Claude Science, a Standalone Workbench for Drug Discovery

Anthropic unveiled Claude Science at an event for pharmaceutical executives, biotech founders, and researchers — a full-featured product designed for scientific work in the same way Claude Code supports software engineering. Available immediately to all paid Claude subscribers, it can autonomously execute high-level research instructions, run code on computing clusters, and prioritizes reproducibility so scientists can trace every figure back to its source. Its initial focus is computational biology and drug discovery: during the launch demo, the system autonomously identified drug candidates for phenylketonuria, a rare genetic disease. Anthropic also announced it will use Claude Science to pursue its own research into neglected-disease drug candidates. In a notable talent signal, AlphaFold co-creator John Jumper recently left Google DeepMind for Anthropic, and the company framed Claude Science as taking up DeepMind's scientific mantle. Multiple outlets noted that Anthropic expects its first profitable quarter soon, and pharmaceutical contracts would help sustain profitability ahead of an IPO later this year.

**Why it matters:** Scientific AI just acquired a serious enterprise product tier, and Anthropic is positioning itself — not DeepMind — as the dominant force in AI-for-biology.

Sources:
- [MIT Technology Review](https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/) — Claude Science is Anthropic's newest flagship product
- [CNBC](https://news.google.com/rss/articles/CBMinAFBVV95cUxNck84aEo5SERWUzlnMzBaY3ZYdnhRZ3gtMkgtSmlUS3gtamhsRUR5ZkNwbEtCUk5BOEkwY1NvMmpSVDlfLTc5WWg0c0xqX1lLR3ZRMV9qSmQ3bnFlWlBUQU16N1pTWGVwZXpjekVUV2JKc3lUbGxPdXNGZXJTLVRMV1UtZ0xEQ0pSM2c1XzB0N2s1RWdJcmlHc3NaaGvSAaIBQVVfeXFMT0lDWjZWV1hWcWs4YXNsWERycW1sM2p4dkFaMERBcm1Jd1BmbjhaeXdyMnlBYzF2Z00yVVNLeHJvLWxSTzlBSGFVYWlNRmxndkczM2FqdjM3YVJ4azlUd2xyU2ItR1ExTDc2WVVmT0pRWWd2eUdvcHRHdnJ2SFdXaDFZVDZ5MEdpLXpycVpXYzRvMW1lZUQzdGQ0cWxha0dmcWln) — Anthropic launches AI drug discovery program, joining tech giants in betting on healthcare
- [Reuters](https://news.google.com/rss/articles/CBMirAFBVV95cUxQVW04WFFFTWxrMWR2WFBhNUZlZGkzV3V4czZ4WE1KV3FDTWNQd19XZGpuM1V4dmw0ZjM2c24zRVhOOFVVLUtzT3lrM19nVDdxNmhuNFlCUTlOMGJvaDE1Rks3ZlZ5c1dKdGtoNVRjbFFCUmxpVEdIWURWWUw4emVfalV0dGVQMGJfYklVQUw5TS1MVWdoLUotSHZJN1lvaktqWXZBeFBEX3NOZHRN) — Anthropic unveils 'Claude Science' for scientific research
- [TechCrunch](https://news.google.com/rss/articles/CBMitwFBVV95cUxNTWFMLUFicUpQcmdVbGVZS1VmekY5c3Bmc0pFQmxtX01mRnd0aFNmNTVkUm41R1FWMy1HWFlfOEU3TWpsZEZDeUZiOUs1QXNFRE1jQ2ktRTgzT2p1dU1hbkM5WWhZVXlRckVhaUU0Y0huZ19nLWctVVEzVW0weDdWRU45dlAtTjVFSFdIcW55YXVWa0dGS3dLY3diUDJsV19QdVZQLUluWWFwNkZWX0pVc2VBWWlwbU0) — Anthropic's Claude Science bets on workflow, not a new model, to win over scientists

---

## US Lifts Export Controls on Fable 5 and Mythos 5; Claude Sonnet 5 Ships with Silent Price Increase

The Trump administration lifted export controls on Anthropic's two most powerful models — Claude Fable 5 and Mythos 5 — clearing the way for international distribution and government use after earlier restrictions had blocked some deployments. Alongside this, Anthropic shipped Claude Sonnet 5, described as "close to Opus 4.8 performance at lower prices," and separately published details on Fable 5's jailbreak framework and cyber safeguards (the system card explains why Sonnet 5 could clear export review: it is "significantly less capable at cyber tasks than Mythos 5"). Simon Willison's analysis of the Sonnet 5 API revealed a practical gotcha: a new tokenizer generates approximately 30% more tokens for the same English text, effectively raising real-world costs by 30–40% despite unchanged list prices; Simplified Mandarin is unaffected. Claude is also now generally available in Microsoft Foundry. The "Fablepocalypse" — July 7th, when even Claude Max subscribers lose discounted Fable access and face full API pricing — is driving a rush of last-minute Fable-intensive projects.

**Why it matters:** The export control lift opens Anthropic's frontier models to allies and enterprises that were locked out, while the Sonnet 5 tokenizer change will quietly increase bills for many production deployments.

Sources:
- [Simon Willison](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) — What's new in Claude Sonnet 5
- [CNBC](https://news.google.com/rss/articles/CBMivgFBVV95cUxQZldDREpCR3h2NTUxODFwLWU5OHVLLWVOQXFzaExVeUk0MUkwR3dhNk9OWk41c29kX2o0OXA1MkNUdTAxTVdOQVh6ZzNqTE5rMVBuaUt4Nm5vZzNVcThFZHIwZ0Y2cjdhTWtuMVEtWkszWDBwNnd2TUVrTnh1elUyYmk1TUhuVmczUm11UVp2Qml2dmt5Nzc2NlBGdVBpVEZrbkkyRDAzQW9Jbkp6QWFMU3VaT0F1V3Q5VzFXM2VR) — Anthropic says Trump admin has lifted export controls on Claude Fable 5 and Mythos 5
- [Anthropic](https://news.google.com/rss/articles/CBMidkFVX3lxTE5aUmUwaFFoeGMxbmo1RWtnemM2dFRFS1pCZUlUWTd6ckJEUC16ZzFwVFZ4QW5jeGdCa0VzbGpFQW96TmpUTmpYd1pyb1U2X3hRQXRyZG9CY1R4RFo0QnhlWlc0YVVLZjVyTEc2TkUxNnpuZllxUmc) — More details on Fable 5's cyber safeguards and our jailbreak framework
- [Simon Willison](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) — Fable's judgement (tips on delegating model choice to subagents)
- [AI Explained](https://www.youtube.com/watch?v=y24lF1q4SFY) — Fable 5 vs GPT 5.6 Sol: The Early Results

---

## Anthropic Accuses Alibaba of Illicitly Extracting Claude Capabilities, Tightens China Access

Anthropic publicly accused Alibaba of running a "brazen" campaign to illicitly extract Claude AI model capabilities — claiming Alibaba used technical means to access Claude in ways that violated its terms. Reuters confirmed Anthropic's accusation that Alibaba extracted model capabilities without authorization. In apparent retaliation, Alibaba subsequently moved to ban its own employees from using Anthropic's coding tools. The Financial Times then reported that Anthropic is moving to close loopholes that had allowed Chinese entities to access Claude, a separate structural effort that coincides with the broader US export-control framework around frontier AI models. This sequence — accusation, retaliation, and then systemic loophole closure — marks a significant escalation in the AI geopolitical divide, with Anthropic taking unusually public and confrontational steps.

**Why it matters:** This is the sharpest public confrontation yet between a US frontier AI lab and a Chinese tech giant, and Anthropic's loophole-closing measures signal that frontier model access is becoming a formally managed geopolitical boundary.

Sources:
- [WSJ](https://news.google.com/rss/articles/CBMisAFBVV95cUxPZzFjNGxxemdjbjRQUVhXek1KQktLM2RlU0ZCTTYwRVRWZ3p6Y0ZrYUxVVHZKb1BBT1BTOGI5T0UzQ2x6bUdJUzU5a0drcjIwZVU3SlktRWxpRU51cldaWU01aE5nSllLMXpneGxnck1FY1lYdUdnOFF2Y2Rnbkh6WU41MERiVFhWSmFQNFYwVmpRbjN1UzZyRjZVV3BsMk5lclRCZVVXSWZVbTd5Uks3SA) — Anthropic Claims Alibaba Ran 'Brazen' Campaign to Access Its Claude AI Model
- [Reuters](https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUjhQd2FfckN3bVZ1MS1YQUs1OUJ2R0lsVDREY0tJMlRPbVBTMHFscE92X3B5UnVOajZaYnhsSUhNSHdmNE1md3hIc0FJWWRfcEktajFjTjBkX04tNEIxOVpFajd3eWJJRk05T1d2WTJhRjF5Mkl1TFNjbTJNY0czVGR2bDNFVTdrOUI5czR1dUZpckVzMXdqenJNbGppNjVVWXZNbHpUMlIteTJ1Q3hnSDltTnpSSFBhWmpZ) — Anthropic says Alibaba illicitly extracted Claude AI model capabilities
- [Reuters](https://news.google.com/rss/articles/CBMivgFBVV95cUxPc1ozV1JIcjJDWWRCZGZZZEN0Z0p4dHVpMkw3eXBWMF9EMlJOemlKSEg1WVRjV2I5VklmMGFFT3FLblVuTEtKa3dYUXctSmpMS0tQdzJhbmhGTEVlRjhHSWdrUUlXZXJydTN2Q3JQTXRSWUVzVkh5TThmaEtVZURBMzdFTHFHaWI0UE43aUw1QS1vbXRoS3BmRUQ0bExHZ0hDQzRmc09kSkxlNUVDOGxNRXctN2dWWGwtX21DSnN3) — Alibaba to ban employees from using Anthropic's coding tool, source says
- [Financial Times](https://news.google.com/rss/articles/CBMihAFBVV95cUxOSU9qQVN5REsxUUQtTTBFSEhPbE0zeF9ZSFJ2UWJvRVBQb0oyMFBSX1gxaEF5RjVvV1ZPOTJVT1Jibkw2bVZFNG1lVEo1WUdRWE9OY0JYenhhZWFnVUhzRk1RM01POF9LMWhSa2pKWXltVFNsWm44REVRVHcxTkdMS0lmOEM) — Anthropic moves to close loopholes that allow Chinese access to Claude

---

## OpenAI Previews GPT-5.6 Sol and Co-Designs Custom Inference Chip "Jalapeño" with Broadcom

OpenAI previewed GPT-5.6 Sol, describing it as a next-generation model with stronger capabilities in coding, science, and cybersecurity, paired with its "most advanced safety stack." Separately, OpenAI and Broadcom announced Jalapeño, a custom LLM inference chip designed to improve performance and efficiency at scale — OpenAI's first publicly named custom silicon, aimed at reducing its dependence on Nvidia and Microsoft Azure for inference workloads. The one-two announcement suggests OpenAI is pursuing vertical integration: a more powerful flagship model at the frontier, supported by custom hardware to drive down per-token inference costs. Two Minute Papers dubbed the moment "AI Just Entered A New Era" in a commentary video. Early benchmark comparisons against Anthropic's Fable 5 are already circulating, with AI Explained publishing preliminary results.

**Why it matters:** Custom silicon from OpenAI signals a fundamental shift from renting compute to owning it — the same playbook Google used with TPUs — which could structurally lower OpenAI's cost base as inference volumes scale.

Sources:
- [OpenAI](https://openai.com/index/previewing-gpt-5-6-sol) — Previewing GPT-5.6 Sol: a next-generation model
- [OpenAI](https://openai.com/index/openai-broadcom-jalapeno-inference-chip) — OpenAI and Broadcom unveil LLM-optimized inference chip
- [Two Minute Papers](https://www.youtube.com/watch?v=qks6dGQFd_c) — AI Just Entered A New Era

---

## Zuckerberg Tells Staff AI Agents Are Behind Schedule; Meta Caps Internal Token Spending

In an internal address, Mark Zuckerberg told Meta staff that AI agents have not progressed as quickly as he had hoped — a notable admission of a gap between public AI hype and internal delivery timelines. Reuters separately reported the same story, with the HN thread drawing 220 points and 386 comments. Independently, Meta has capped internal AI token spending after costs approached billions of dollars in 2026, signaling that the economics of LLM-intensive workflows are forcing even the largest AI spender to impose controls. Together, the two disclosures paint a picture of a company that ramped up AI investment faster than agents could deliver productivity returns, and is now recalibrating both expectations and cost structures.

**Why it matters:** The world's largest social-media company publicly admitting agents underdelivered and simultaneously rationing compute is a real-world stress test that every enterprise deploying agentic AI will face.

Sources:
- [TechCrunch via HN](https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/) — Mark Zuckerberg tells staff that AI agents haven't progressed enough
- [Reuters via HN](https://www.reuters.com/business/zuckerberg-says-ai-agent-development-going-slower-than-expected-2026-07-02/) — Zuckerberg says AI agent development going slower than expected
- [MLQ.ai via HN](https://mlq.ai/news/meta-caps-internal-ai-token-spending-after-costs-approach-billions-in-2026/) — Meta caps internal AI token spending

---

## Claude Fable Wrote Most of sqlite-utils 4.0 — and Found a Data-Loss Bug Before It Shipped

Simon Willison handed Claude Fable the final pre-release review of sqlite-utils 4.0 and what followed was more than a polish pass. Fable identified five "release blockers," including a serious data-loss bug: `table.delete_where()` never committed its transaction, leaving the connection perpetually `in_transaction=True` and silently rolling back all subsequent writes when the connection closed. Over 37 prompts, 34 commits, and +1,321/−190 code changes across 30 files, Fable rewrote the transaction model, fixed the blockers, and updated documentation — while Willison enjoyed the Half Moon Bay Fourth of July parade, checking in from his phone. He then had GPT-5.5 review Fable's work, which surfaced two additional P1 issues (both confirmed and fixed). The estimated cost at full API rates: $149.25. Willison is on a Claude Max $200/month subscription, racing to exhaust his Fable quota before July 7th ("Fablepocalypse"), when even Max subscribers lose discounted access.

**Why it matters:** A seasoned developer letting an AI find and fix a data-loss bug in an existing production library — and cross-reviewing with a rival model — is a concrete, documented example of how frontier AI changes the economics and safety floor of open-source maintenance.

Sources:
- [Simon Willison](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything) — sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
- [Simon Willison](https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything) — sqlite-utils 4.0rc3

---

## Also noted

- [Start building with Nano Banana 2 Lite and Gemini Omni Flash](https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/) — *Google DeepMind*
- [Introducing computer use in Gemini 3.5 Flash](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) — *Google DeepMind*
- [Nano Banana 2 Lite](https://simonwillison.net/2026/Jun/30/nano-banana-2-lite/#atom-everything) — *Simon Willison*
- [Google DeepMind and A24 announce first-of-its-kind research partnership](https://deepmind.google/blog/google-deepmind-and-a24-announce-first-of-its-kind-research-partnership/) — *Google DeepMind*
- [Anthropic launches Claude Tag, a tool that works like a virtual employee within Slack - Fortune](https://news.google.com/rss/articles/CBMihwFBVV95cUxOemlxN2NjY2JHZlQweGxfOFBYc3pqbExwWFhXMjVzUmFxa2RyMURaQTFkQ2Y3dEJYdHo5V2EtdHRvd0RnUUdTWnRuQ0tESDR6c3VWX2hTVFRxVk9xRU0tUnpSRzdCRHNvWnZ3YnNEUGxRbWxvam1Zc3RFbWFKMGhhcmJicmtrTEE?oc=5) — *Google News — Anthropic*
- [Anthropic’s Claude Tag is learning your company, one Slack message at a time - TechCrunch](https://news.google.com/rss/articles/CBMirgFBVV95cUxNYVQ5VktmelZuekFOV3k5TDBQN3E0VHpCNnVqOExoTDNLUzlqTGJfemlja1ZVMU4tdFh0WDc2VFRaY1BYODNyb1VBcVJhMTZvMnl0LVFaN0R1ODZ5SHRHSDdwaW4wRFJwS0t6N3RkN3hEZ053RDA0VEhndzJCNjZCWVZtSnN2VkFIY2NZdDA0RVNDeXlVV0EwaDBLeTF2SlhWYldvaldZWTFnUXByYlE?oc=5) — *Google News — Anthropic*
- [Introducing Claude Tag - Anthropic](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9iZjJCVWRWdnpWLWtMTGVEcy1RbmFuWGY3UHhfVmFlQkRZalpoOFZMMzhLeEZhYVBTcjhKR0FZaEF5QlpNVzB2bXVIczF0X0RWbmN4NDM4VmUtZGxyU2dHbGRSWQ?oc=5) — *Google News — Anthropic*
- [Anthropic launches Claude Tag in Slack with plans for wider rollout - Reuters](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMXZ2NGkzVnpxZ1NkOHloUkVWRmVMcGNYSG82TTBYWXRuZHh6UW8xV1I2TDlpWkJpMGRoaHplMFJfa3dHdDlyOUUzWVM1VkpsRDRCTlZ1blFoZXgwVU1WWDE5OHB1Y2NDVDRtRm40bUpOTVhMOUNFV3QyN1FqajVUenFxaXBOR1prQ3BoQkh6dURSaUtLWDlxTTBYUzUxdnZuSjVVc1YtUHo?oc=5) — *Google News — Anthropic*
- [Governor Newsom announces a first-of-its-kind partnership, providing Anthropic tools to state agencies and improving services for Californians - California State Portal | CA.gov](https://news.google.com/rss/articles/CBMihwJBVV95cUxNNVdrb0JtdWt6OU1tU2FicENIa0R3SFBPaHVPYjJHQThPX1ZQR0dZNndHeEI1Nlo1eDVJMDJNQlJUOEcxZldnUUtGQVUyWEhrV29SMGhFMmpubEt6MWxUai0zdmluM1k4YTBNUVBkUmsyZUFwVXRpWVhpcDJKRnpBR1ppNjBMZXhoX0RNUTlOUERKenlyQkc4Tjd3aXh1ZHpzSV9wWGdvWlRDNHpsWUEwVE1BVS1ZVHYwVnNackQ0ejl4NElKVHpXS1NkX2VaMDA3TFRjX3kzVEloS3Q2S1Yzc1phekx0UjE1clFzQVN1NkZRb3VfMGZETWV3cXV6ZnNMQWUwSzNkOA?oc=5) — *Google News — Anthropic*
- [Newsom, Anthropic ink deal to expand government use - Politico](https://news.google.com/rss/articles/CBMirwFBVV95cUxPN2ZSeVJSNTdYWFpXdkFzSVBHelFiTXhwTmtKUFNkcm5kM1hMbjhZQXFxVFZfVXBKLURHdlM2UXNjRHl4eXBRaGZWYWJJYU5pZkcydUZwRWpzWDR6Yzk2TFR4ck9HeEotcG9oZmMxZ2VPS0xMSjlaMWNFSkVfWHlBZ1RKWkliWnJwa3VlblBNMzBzQVljeDFzMGJlLWk2cGNGLV9kdHBwWXFwR09WTURB?oc=5) — *Google News — Anthropic*
- [New AI tutor achieves 0.71-1.30 SD effect size in Dartmouth course [pdf]](https://intextbooks.science.uu.nl/workshop2026/files/itb26_s1s2.pdf) — *Hacker News (AI, 100+ pts)*
- [Professor denounces mass AI fraud on an exam at Brown](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) — *Hacker News (AI, 100+ pts)*
- [Incident Report: CVE-2026-LGTM](https://simonwillison.net/2026/Jun/26/incident-report/#atom-everything) — *Simon Willison*
- [What happened after 2,000 people tried to hack my AI assistant](https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything) — *Simon Willison*
- [Red-Teaming after Mythos — Zico Kolter & Matt Fredrikson, Gray Swan](https://www.latent.space/p/gray-swan) — *Latent Space*
- [Godot will no longer accept AI-authored code contributions](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/) — *Hacker News (AI, 100+ pts)*
- [Building a World Map with only 500 bytes](https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything) — *Simon Willison*
- [Better Models: Worse Tools](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) — *Simon Willison*
- [Open Source AI Gap Map](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) — *Simon Willison*
- [Quoting Josh W. Comeau](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) — *Simon Willison*
- [June 2026 newsletter](https://simonwillison.net/2026/Jul/3/june-newsletter/#atom-everything) — *Simon Willison*
- [llm-coding-agent 0.1a0](https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything) — *Simon Willison*
- [Using DSPy to evaluate and improve Datasette Agent's SQL system prompts](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) — *Simon Willison*
- [Understand to participate](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) — *Simon Willison*
- [The AI Compass](https://simonwillison.net/2026/Jun/30/the-ai-compass/#atom-everything) — *Simon Willison*
- [Have your agent record video demos of its work with shot-scraper video](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) — *Simon Willison*
- [shot-scraper 1.10](https://simonwillison.net/2026/Jun/30/shot-scraper/#atom-everything) — *Simon Willison*
- [HTML table extractor](https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything) — *Simon Willison*
- [Count the number of Safari tabs](https://simonwillison.net/2026/Jun/29/safari-tab-count/#atom-everything) — *Simon Willison*
- [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) — *Simon Willison*
- [Quoting Jon Udell](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) — *Simon Willison*
- [Hack Your Summer](https://simonwillison.net/2026/Jun/28/hack-your-summer/#atom-everything) — *Simon Willison*
- [Quoting Dean W. Ball](https://simonwillison.net/2026/Jun/26/dean-w-ball/#atom-everything) — *Simon Willison*
- [Quoting Timothy B. Lee](https://simonwillison.net/2026/Jun/26/timothy-b-lee/#atom-everything) — *Simon Willison*
- [AI and Liability](https://simonwillison.net/2026/Jun/25/ai-and-liability/#atom-everything) — *Simon Willison*
- [datasette-export-database 0.3a2](https://simonwillison.net/2026/Jun/25/datasette-export-database/#atom-everything) — *Simon Willison*
- [How ChatGPT adoption has expanded](https://openai.com/index/how-chatgpt-adoption-has-expanded) — *OpenAI News*
- [Inside Genebench-Pro](https://openai.com/index/genebench-pro/case-studies) — *OpenAI News*
- [Introducing GeneBench-Pro](https://openai.com/index/introducing-genebench-pro) — *OpenAI News*
- [Core dump epidemiology: fixing an 18-year-old bug](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) — *OpenAI News*
- [Mapping Europe’s AI Workforce Opportunity](https://openai.com/index/mapping-ai-jobs-transition-eu) — *OpenAI News*
- [HP Inc. launches Frontier strategic partnership with OpenAI](https://openai.com/index/hp-frontier-partnership) — *OpenAI News*
- [How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work) — *OpenAI News*
- [Helping build shared standards for advanced AI](https://openai.com/index/helping-build-shared-standards-for-advanced-ai) — *OpenAI News*
- [How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery](https://openai.com/index/gpt-5-immunology-mystery) — *OpenAI News*
- [How Omio is building the future of conversational travel](https://openai.com/index/omio) — *OpenAI News*
- [Patch the Planet: a Daybreak initiative to support open source maintainers](https://openai.com/index/patch-the-planet) — *OpenAI News*
- [Daybreak: Tools for securing every organization in the world](https://openai.com/index/daybreak-securing-the-world) — *OpenAI News*
- [The Rise and Fall of the Roman Empire and the Byzantine Empire | Lex Fridman Podcast #498](https://www.youtube.com/watch?v=pv1TUJSEM2k) — *Lex Fridman*
- [They Said This Will Never Run In Real Time](https://www.youtube.com/watch?v=uO5cvkzh3P0) — *Two Minute Papers*
- [DeepSeek Just Solved AI's Billion Dollar Problem](https://www.youtube.com/watch?v=mG4SmhWyeFA) — *Two Minute Papers*
- [🔬 The Coolest Diffusion Research Isn't in LLMs — Evan Feinberg & Sergey Edunov, Genesis Molecular AI](https://www.latent.space/p/the-coolest-diffusion-research-isnt) — *Latent Space*
- [Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin, Databricks](https://www.latent.space/p/databricks) — *Latent Space*
- [Import AI 463: Self-improving robots; a 10k Chinese GPU cluster; and an elegiac essay for the human era](https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/) — *Import AI (Jack Clark)*
- [Import AI 462: Superpersuasion; self-sustaining AI; paths to ASI](https://jack-clark.net/2026/06/22/import-ai-462-superpersuasion-self-sustaining-ai-paths-to-asi/) — *Import AI (Jack Clark)*
- [Al Vigier: Canada's AI strategy shouldn't include secret Palantir bills](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt) — *Hacker News (AI, 100+ pts)*
- [Please stop the AI confidence theater](https://www.elenaverna.com/p/please-stop-the-ai-confidence-theater) — *Hacker News (AI, 100+ pts)*
- [Protect your right to run local AI](https://righttointelligence.org/) — *Hacker News (AI, 100+ pts)*
- [Claude-real-video － any LLM can watch a video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) — *Hacker News (AI, 100+ pts)*
- [No LLM Code in Dependencies](https://joeyh.name/blog/entry/no_LLM_code_in_dependencies/) — *Hacker News (AI, 100+ pts)*
- [AI can't be listed as inventor on patent applications, Japan's top court rules](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/) — *Hacker News (AI, 100+ pts)*
- [AI fake news complaining about how AI fake news is the death of real news](https://www.niemanlab.org/2026/07/now-were-getting-ai-fake-news-complaining-about-how-ai-fake-news-is-the-death-of-real-news/) — *Hacker News (AI, 100+ pts)*
- [Working With AI: A concrete example](https://htmx.org/essays/working-with-ai/) — *Hacker News (AI, 100+ pts)*
- [Tidal AI Policy](https://tidal.com/ai-policy) — *Hacker News (AI, 100+ pts)*
- [AI boom risks global financial crash, warn central bankers](https://www.telegraph.co.uk/business/2026/06/28/ai-boom-risks-global-financial-crash-central-bankers-warn/) — *Hacker News (AI, 100+ pts)*
- [We need tech news sources which exclude AI](https://news.ycombinator.com/item?id=48713041) — *Hacker News (AI, 100+ pts)*
- [Ford rehires 'gray beard' engineers after AI falls short](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/) — *Hacker News (AI, 100+ pts)*
- [Reflections on software engineering in the age of AI](https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/) — *Hacker News (AI, 100+ pts)*
- [Would Claude Refuse an Illegal Military Order? - The Atlantic](https://news.google.com/rss/articles/CBMinAFBVV95cUxQWTYxdFNVdlI0QXdQMDhyTVg5c2pLQnNKU3dwZExNbzc1bnFJdUdoZ183UzNMeGNZRkcxbEliVHB5b1RDbGRGdWhoSmE2NUJTc2tENzVCSlNacnRaOXU2TzBYSUx3NXlUMjFOLW5kTTNybVRxRnc4V2RSb3BjRjhoWWExLW94VFdaVHVTRDJyQXZEemxjd1VCeUh1Z1Y?oc=5) — *Google News — Anthropic*
- [Anthropic’s Claude is winning over paid consumers, a market owned by ChatGPT - TechCrunch](https://news.google.com/rss/articles/CBMirgFBVV95cUxQVksxQlFkblFNRlhaZTNfX3o1ZXE0WEpGdmNrMmw5anQ3dTNXWnYxU0tGSE9LczVKTmo4cEk5WHJIM19qUlZJLWg3YlJHUERVdWItcmlSMFppYXBMWVJXUTdZN2Z5Mk5DUGR1Y2lVaWZ4N1RJOTFZcDFRZFNKcWprZjc2SjZLcFpDNGZBTHJURjd0WTRxcnJDTWY0M0hubzBkSThEYV84X1BmVXNPLWc?oc=5) — *Google News — Anthropic*
- [Anthropic Economic Index report: Cadences - Anthropic](https://news.google.com/rss/articles/CBMidEFVX3lxTE5fNVR0S19Od3hZaWJSaTdlRkpZOVZJa0M4TzhldFg0WElpY3duXzlHT3AtZXNoazJSbXlUSTE5dEpiUmVWc0FRaTJOc2tValRaOFJmRnlHS3IwYk5DNnp6OGtCY3p0cWFRR0dNQjVfcVhXbk5X?oc=5) — *Google News — Anthropic*
- [The Briefing: AI for Science - Anthropic](https://news.google.com/rss/articles/CBMibEFVX3lxTE5fbm5oWi02TE93S3FObHowMk9MUkRxS0NvWnpOcHZWd3UyQWhPN3g3OFE0WERWckpQa2U3T3dyQ2tCWm9Qcy15bWd1OTNQTTJvMHM4ZDNuNDkzNWpXRWt2STRqSzBhZTNocGpxYg?oc=5) — *Google News — Anthropic*
- [The future is now: College of Computing & Artificial Intelligence officially launches - UW–Madison News](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPeFk3N2hnN0d4MHo5bmFJUW9NMm92WERQYThJR1RERm5NMXQtTkJKRkl4UW5LMHlSanNTYkVhN045RGFndmVCMEhEcEQ2cEh4RHZ0aTNVM2ZPcjdFbDFJYnhsbzEwV1dVbFQ3VGVfNzNSVF9HMWxwSk9uZlVNdlBtZEcxRjhkOVFfU05UaHRvSFVoT0stOHNLZnlHUHJJNnI2b1VyNTJWMmQ?oc=5) — *Google News — AI*
- [Artificial intelligence for food innovation - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9XMG1mV0ZMUTk3UzAzRlVxRTRBdWFrOFdRUnlITXRWUER0OHl4a2VUOWhyTld3RHV0ZWtXUnRsSVNmTHFwaXRYR0ZMMUNudVFQVlE4RGEtMllNZW53a3R3?oc=5) — *Google News — AI*
- [Public University Boards and Artificial Intelligence - Manhattan Institute](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQnhIYWpua09vUjhJbGk0dGNyNUEwLWlwZWQ1c1lZWEZNMFZjX1YwVm1hcXBwdndqeTQ0cFdYeWEyd2lmWmJPcGdid01nYzQyb3pSY2NYRGMtTlRVS0xaUEFESWgxb1lROEEySHlmX2Qyd3UwMjA3TFNCYlBrUDl0dzdJMVIwUHdPcFVRN1BzU0RFZw?oc=5) — *Google News — AI*
- [Proprietary Intelligence: How to Win with AI - Bain & Company](https://news.google.com/rss/articles/CBMif0FVX3lxTFBWNG9DRVl5TjNadVhUUTB5ZHZneTg3TC11eEtYbTA2aE1Qdkl5NUNNTGZxelVDN3ZSbEFOMDZXb2xRaUd2eS02Nm42MDNWb205dHJydHhUclJBZm1fRUkxM3pjMGNzcnFCRHpxeWtrWF9nZDF0aGU1ODlCX1dhSDg?oc=5) — *Google News — AI*
- [Research at Middlebury College reveals nuanced story about artificial intelligence use - VTDigger](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQVlNSMWtndHgyRlcyVWZVMnZBNVMwTU0wTmJqaGJyS0tfZDhoWHphaDVmSmVoeUdKZUtxcTNIR3gxem5LNWdNRFVrVU1jVi1vTEg3UndCa2F4NzNsUGQxWDhyYjlpeGt1MExPMmhLODlJQ25NbXhRaGpRbnBSRTREdFFEb1VIWXI0UHcwNEUtN1R0R0JZcW1sSnhWMU50a2hJOVk1bnJvMnpMd1VST1Mwbk85cWdCVk5FVHJJ?oc=5) — *Google News — AI*
- [Artificial intelligence could usher in a new era of vaccine development - CIDRAP](https://news.google.com/rss/articles/CBMioAFBVV95cUxPWGlPaUVNdnVRVzc0Y3FzRWQxTWg4UnJSTXhlU0hybGVwYTdiTnkwaXVSVXB3ZU9teGlkamZLLVZfR25MMm1Xc3JUVzdMN2QzOVoxMDhzR3ZybUhVcndZY1pMcFpVOUwxVHhsSi1GbVFueTd1WlFxZEZycjl6T1ZDR0lhcUpGdFhLR0Y0ZWc3N042aDlWdkt6OHdwcnBTc3Zw?oc=5) — *Google News — AI*
- [More than half of Georgia teachers now use artificial intelligence to prepare for class - Georgia Recorder](https://news.google.com/rss/articles/CBMixgFBVV95cUxNeHNncE9Pd2thRk1rOVdUa1RLeDFKQ25tRnRUa3FvUkVRdkhuaHdENVRGeU5PVmdnXzM5MlJTaWgzVU1NQzNEYml4Ym80OWJrYVE0d3hqTGs2V0pzZlFXejVFMHNlbmJPV1ZhSnBxdHVrN21ZckJHTVU1OEhtYWM2OXdzTHFnaUpVRmVfQzRrQ2FyVmRiSzhuSVZYWkJ6MEFpWlZwUzJrYkxlY09lR3g4T0syWDk4MER3elgtclNXRzRDVC1ISlE?oc=5) — *Google News — AI*
- [Artificial intelligence becomes ripe target for taxes - Roll Call](https://news.google.com/rss/articles/CBMijwFBVV95cUxOa2xpbnQ0WkNlaFJfUmtBbGN1SXJ5eHJZVXZieUhWR0JvaGZadjBMdzQ3VC1RVzA2QnZKTWZQSUdOZHIxOHZSUndJQ09vNDZxNXlTb29sNGdqaXVQRXZQaE5aZzdsMHVZdEdZMTBQTjE4dmFNTEVDanJpdkJrMXUxc01fc3M4dXVrdEg3ZllaRQ?oc=5) — *Google News — AI*
- [Artificial intelligence and Engels’ Pause - Financial Times](https://news.google.com/rss/articles/CBMicEFVX3lxTE5HclNINnBwTURrZ3lVQmxGV0tLT01uaE1FQUo5a2hRTHJRUmRlUUNrUFNlZU4yZnZmN2hmOTNhOUdHWFhUSEVBd3gxRzhSbFY1YjQxNjdJaXR1Q2UwODhhSGdYWnV0RHk0dl92NjNPbm0?oc=5) — *Google News — AI*
- [An Optimist’s Account of Artificial Intelligence - Lawfare](https://news.google.com/rss/articles/CBMijgFBVV95cUxNSUVoYmRXSV9fajZDbGEwQVA2STJEQWwxLVJBcTZqd2ttY3AyTWFGMzdEU1dpdFhhTDBZbVptcTc2aTQxRV90UGhBbkhMZ3VCU1hSN1A1Z2JhUXdVZXRNMlpmeGhMVE9pOFhDWEFsd2pqUHR3enRLbXU4ZVk0NUpPbl9xUE5jMThvS3lwWkJR?oc=5) — *Google News — AI*
- [Artificial Intelligence is Unlocking New Possibilities for Parkinson’s Care - Parkinson's Foundation](https://news.google.com/rss/articles/CBMihgFBVV95cUxQOEJOTUdLWUtObjBJZGNwdGJRQXZDV210M0FKaVduWlZIVUE2b3NrdmlZbE5WM1B4VEEteWVDcEg5dXFzV1QtZzVLdzdnWW1SVE1odHB4SlQwdV9EbGVRaHlGcFBSbGFzYnNfQ0w4WS1LaGNiWWJFR2VSMTYwdkxKcFB1YUtqUQ?oc=5) — *Google News — AI*
- [Nonprofit aims to help displaced workers as businesses adopt artificial intelligence - PBS](https://news.google.com/rss/articles/CBMiugFBVV95cUxNMm5vQ0xYX3QzLUVaYkhWOHU4QkV6eEFZTzZVRkNjX2x5RWU3UUlPdFVLbm9VQ3AwZXRpUENfN0dxcUdLOVBTR1U5blZhd2JHTFhsZF9IaVpsZ042eFdEUXVDaUFrdTZlZHo3emhibGFpYS1ULWd3S0ZYZ3BwOXY1WVJDLUc2ZlRtaGxmcW5naGduUXIzbm4wZmN1cWlfV3Y2TVNRTGFOelQtc0R6TjRVaXpYWjFUQWdqRVE?oc=5) — *Google News — AI*
- [‘The science is here’: UN chief welcomes first global AI assessment - UN News](https://news.google.com/rss/articles/CBMiV0FVX3lxTE9lSHZWQXl1eG5lUDVRTTRDdFNDdGRkRVhKbEs4T3RGTi11eFN1eG1nX2JDcHlueFJBQ1pvTHpEZ0N6RmpxUXBiQUxfVzJwWEs2dWRSRU1odw?oc=5) — *Google News — AI*
- [Why Facebook, Video Calls and Artificial Intelligence Matter for Age-Friendly Communities - Rutgers University](https://news.google.com/rss/articles/CBMiswFBVV95cUxPcGVQdXIzZHlnVUhaQkdNeDg2bjZIcVNsa3cxUFc0Sk5Pc3JHbGpRMzB2dGlhdmpBTERkMTVCc0U0Z1gySE53M1NERkE2TDB4UFRFSXdBd0VXdlh1dVNQSm5HbGxFVkdYV2VrX1hjT1RUZHk3QzJqbEN1WkpTNlo5M3Z0QVMxdFVWZXZVdEtLcWpkOVc2WG91Y3M1alBzQWlpUTNZWmhQWExrZW04ZGhMWHBTSQ?oc=5) — *Google News — AI*
- [Bailey campaign embraces artificial intelligence in new era of politics - Capitol News Illinois](https://news.google.com/rss/articles/CBMirgFBVV95cUxNUWd6XzN2NUJ2WDM1WjJ5b2JwVGR3Tk1fQVJ4blFEams5ck16UEFJbjFzNWhaZzNsRFFXUjZFOTZWU2ZndjVuaGFQY09tOU9QWEt3SkN0MXZoSHh3ZWh1Q3hjM2VJQW1oNWE3OXdJekhVdmxJTnluLWVWOVladEJScjhmMVRFQ1llZndUYXp1U1FtLTA3Qy0tS2VKNXdCVTlBbkhZeTNRN0FiVVZ5OEE?oc=5) — *Google News — AI*
- [Virtual outreach event on FSB sound practices for financial institutions’ responsible adoption of artificial intelligence - Financial Stability Board](https://news.google.com/rss/articles/CBMi4wFBVV95cUxOdzdWQnIwYTczR3lOY2dpa0REbFpGVWRscFdSSWl5clRXbGVlRnZIYUZxVGNrUDRuaEU5cndsV0dPOXNodXFiS0IxeVJVcjBqNm1iSUJhdG9PcDFGMUFndk5GY0I0c0RWTGRMXzhxRGwtLUQ3bWJYQl9OVHRzSG1qODlCSlVMRmRqN1Y2d3MxRUNnZk5zVGJBLUt1bVQxSWN3aWp1NUlsajVVUEVWNWs2cEV5cjVaTGUwOExxVkgtNlFCRHFkYVZORE9IMzZpU0p6TkJ5WjZYOWw4OEtKYUEwbUItaw?oc=5) — *Google News — AI*
- [Bailey campaign embraces artificial intelligence in new era of politics - NPR Illinois](https://news.google.com/rss/articles/CBMiygFBVV95cUxNSXVrSXhJN18yUzdVLS03NS15SDZsekQ2ZjRfMHBVdEtEczQzdlBFNHE5MHVmUTdoaWNSMVVvX3lmRlV3U1BISmhaUWVBakt1bG14eWNLdFkxSTdwYWxOc0tiSjRMVXBUQWFGOUhvNjBObVI2UXN1LWs5bDVoWlFweXZYa1hRQ1RpYkZKb21NZTRqVmlFY3F1aFZMQ0REa2N3SUp1ajVyd2sxRC1nUWpUb0ZKeWRjYXFMVHh2UlhoU1VsVkF6VW9la3RB?oc=5) — *Google News — AI*
- [Moving artificial intelligence from research to real-world clinical use in neurology - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTFA5R2hxWVZiUTVtSmVFV2pYZnFUVjFVRTVnX2F6eTNiaklmYVlua0Zob25xX1U5elM4VzVrNnJxTUJ5a1BlTWZpVV92VF9oRDlGYWY4RFRwZ2lqcVdwdzBR?oc=5) — *Google News — AI*
- [Disparate privacy risks from medical AI - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5BdHJHODc1ck41N29adnZCZlMtVURGUEV6X1k0Tjhyc1ZpcUJJTkxRaHIxQkc0WnhSVklLNGhrUVRQYkJZVjBYUjI2a3Z2TlZyNlF3a19Td3pJdFJXRFhj?oc=5) — *Google News — AI*
- [Generative artificial intelligence creates delicious, sustainable, and nutritious burgers | npj Science of Food - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9hVEJOYk5oRkZRSVM0SFU0WU9BWm1XNXlsdzZMUVU2VThvd05yLThoZkc3N0l0ZmJoUjZ6YWl2NUZZMzEtcWtxTTctWUNOdXNKMGxfMVpIVWxrUk5hb2lV?oc=5) — *Google News — AI*
- [UN Artificial Intelligence Panel Launches Report Ahead of Global Conference - ipsnews.net](https://news.google.com/rss/articles/CBMirAFBVV95cUxQVktZOUo5eS1zWThsaGRRNkVMcVZoZENNa2k4Qm1KaldoeTRfNjRtSWhKZkNaVkNEUmN4djlSMmZjTVRXZ1pCZ1JRbVlJaWNBRXNuTUFHUk9pTkN6V3FvalVGWXEyY3laUVYyZnFfSDQxeWhySWRVUF80UEYtTFY3RzBoU3phNTloZWRqbm91VHMzNVJ3SUg1QlJUWUZPWGdNbndraUd4TVF0TjVZ?oc=5) — *Google News — AI*
- [Signal in Noise: How Can Artificial Intelligence Benefit Psychiatric Practice? - Psychiatric Times](https://news.google.com/rss/articles/CBMitgFBVV95cUxPOXhCb2pCbVU5T2lfZ0J4TFdleVdMU1JycVk0Z05RWEhjY3o5RWJQNDE5TUJHRXBtcFFYTnJXSnktQmNsN1lWN1A0VG82aEFMbTBvT0ZGb0xIUEg1cjVJQlhOVXJqaTdtVnFIdTU1V0lJT3ZVWFNUSXhJMFZCZXU0ZzBUbGFydkFHTnlrVGFoeS1PakVjQWhPRkV3cW5CZF8tOWRvdG1VbGRvU29ZZVVEYkFwcng5dw?oc=5) — *Google News — AI*
- [NSF Prepares To Announce Artificial Intelligence Coordination Hubs - AFCEA International](https://news.google.com/rss/articles/CBMisgFBVV95cUxObFZTOE9fclJSWkJIVmR5cl95NVhBXy1iVjl1Qk80dDhya0tXTC12Slh2cXBnbjJOVGhNcHFEcEJRSWpqb2I2dEM4QTl1eGVOdnczRlFPLS1GZHhKQTJyZ1VmWnFsVkZTcllONk1XUWZ4ZWZkVGtzOXJ1Z3BOR0tSeERzeV9lUjcydHluYXViMHdhc3pnSVY2Yng4LUpMSHpLdFdIMExBOUI2amR0T0JvM2dB?oc=5) — *Google News — AI*
- [1 Artificial Intelligence Stock You Can Buy and Hold for the Next Decade - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxQME9uNHV2MzZhM3JZSW85Y2lFSVlJZzhVellPZ2duM0xQVTBfNmdjWTJ6WXFIaFFpR3pVbllyaGFnUjBVTTBTaENFMExWX0FKdzJOcmtHbDhvM0lXT3o1Rlp0alBPeGhGRFFDd2Zhak40WHEyYXlhMGhWNDBUWVRERkhzS29SMkdmU2k1SzBVMHREUmZaUVA4eFU3cVJHTnZPWUE?oc=5) — *Google News — AI*
- [We’re Only Starting to Grasp the Pitfalls of Using A.I. at Work - The New York Times](https://news.google.com/rss/articles/CBMimwFBVV95cUxORFFITnFHSGhKdWwyMUxnYmYxVmROZHpCSzloT2pOWUZCRFhFSlNURVQ5UWNMRXVURm9BeVNXNHhkcjhRSDdYaFBsYU9RMmphSVpGWjRaRXBmSTNhTXlsZl8wYU95SDUtdG5hQm8zSHUxRUdOWWM3cndhc3NfbUpmcFFPS2tEdEV2bzMwdjJGLS1NaktXbENEcFEtdw?oc=5) — *Google News — AI*
- [The Role Of Artificial Intelligence In The SKA Era - Astrobiology Web](https://news.google.com/rss/articles/CBMikAFBVV95cUxQZzViSjgwcWpLWG1BSWFSZE9GaGllWFNqNWdhdkJGZUpzV3oySzNHbW0tdXZCLTFjZWE4aUgxbU5wTm9HUzRKZXJNdVhQOW10UEFCVm5FZ1ZmV3JTUk5YY2N3VmJ4Tzh2a1BLbUd5empiWG02NFdtMmxTWEU4bmhrOVNDdjFSU00ySF91ZlY3OXI?oc=5) — *Google News — AI*
- [Nearly 100% of patients surveyed say they’d want to know when AI is used in imaging - Radiology Business](https://news.google.com/rss/articles/CBMiygFBVV95cUxPVXlocXFqYjMycjc0Ny1YN2h4LW51M1dfZzVRZXZKSDBsM0VQeGZ4Wi1rYXVBbmhMckhXYnNiTzlvZ2VJcTNvRGRHa0VwYXBSYUhnVHFuWGFqaWxKVE5VMHJsOHctNThjSjhiRzJJRmx0MFhJUUIzU1Qxb0w5b0c5RS1RdEV2ZHpycnVIR0h6TmJibjY3cHhfbTI3XzhnY2lBZFctSlVxMnMzUmFyV3lXaS1EbThqMVJVT2JTT1NsTjRiMUNOZTk1VnhR?oc=5) — *Google News — AI*
- [Latin America and the Caribbean Consolidate a Regional Roadmap for - UNESCO](https://news.google.com/rss/articles/CBMixwFBVV95cUxNLWpDU0o4aVJUZGpWZUJWTl9IZnRBbVc5ME1tR3Bob0FQS3c1ZnFmcUtEOW80VVZzOWR1V05vc1ZfV0l4V19maWRFLTQtaEcyVXE0QXJTV2RIZEpqSlBHY01kT2c1OUJZdF8xNTJ0d3RBYW9FY2dJSmRCOTRaVlRFZkE1Z05PWnUxeGlDdnVjRnlwLVdNSzhlR1JnN3lOQnRwWmtQUUM2Zmd2cGN0dnoyblp1SExMa0g2eUtKbkpTTHpKbkt5SjRR?oc=5) — *Google News — AI*
- [The oversight paradox: Why human control over AI may be eroding the very competence it requires - The World Economic Forum](https://news.google.com/rss/articles/CBMigAFBVV95cUxOWDNZaUVBb2NfLXRvZWpEZ05MUEpmZlJmbmtwcGp3N00xOWJJMjNtR0FCWnFaMGxXbFdIeFJIbDdEQzhkZWdqWDFUVWhEaEpxOWJxSUJGa20wVU9uZGlaMWRkaTRZTEFYR1gzZWRfZFJyM1Uta0VGS2ZvNnNrRzM1TA?oc=5) — *Google News — AI*
- [Spirituality, Religious Moral Precepts and Artificial Intelligence - Jewish Journal](https://news.google.com/rss/articles/CBMitwFBVV95cUxPWF9DbHEwVnJFdHBCQ2phaGFWblotdWlNRUZodFhQaWYtNkMtdmF1S1l6Ql83bWJjOFhHcERLa0gzWG5VV3pWaUNBMFFwMlVfZWVINmI2bk16cnp2V3NST0dEVW0zMEJKaTBPRGdmRm11RXlKS1E2NlhGUTNsdnZqdm80M0dXZTFtN3FIV2tWTF9kLTdYVnRBdTBlQTFEVmExQUZ0Rk1zQmVic09XUUtmZ29aOTh6WEU?oc=5) — *Google News — AI*
- [A device that revives eyeballs from dead donors could make eye transplants possible](https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/) — *MIT Technology Review AI*
- [The Download: a smoking “endgame” and a new Elizabeth Bear story](https://www.technologyreview.com/2026/07/03/1140134/the-download-uk-smoking-ban-elizabeth-bear-story/) — *MIT Technology Review AI*
- [The UK’s generational tobacco ban might not work. I’m supporting it anyway.](https://www.technologyreview.com/2026/07/03/1140036/uk-tobacco-ban-might-not-work-children-smoking/) — *MIT Technology Review AI*
- [Achieving operational excellence with AI](https://www.technologyreview.com/2026/07/02/1140045/achieving-operational-excellence-with-ai/) — *MIT Technology Review AI*
- [Teaching AI to run with the turbines](https://www.technologyreview.com/2026/07/02/1138433/teaching-ai-to-run-with-the-turbines/) — *MIT Technology Review AI*
- [The Download: a startup has a solution for AI’s groupthink problem](https://www.technologyreview.com/2026/07/02/1140027/the-download-ai-groupthink-llms/) — *MIT Technology Review AI*
- [Why California’s carbon manure math doesn’t add up](https://www.technologyreview.com/2026/07/02/1139981/why-californias-carbon-manure-math-doesnt-add-up/) — *MIT Technology Review AI*
- [LLMs are stuck in a groupthink groove. This startup is trying to get them out.](https://www.technologyreview.com/2026/07/01/1140003/llms-are-stuck-in-a-groupthink-rut-this-startup-is-trying-to-get-them-out/) — *MIT Technology Review AI*

