# AI digest — 2026-09-28

## TL;DR

- Claude Opus 5.5 and GPT-6 Sol/Luna Launch a Frontier Price War
- Security Researchers Used Claude to Break Into OpenAI, Earn $6,500 Bug Bounty
- Claude Now Leads a Quarter of the Work Building Anthropic's Next AI Models

## Trending


## Claude Opus 5.5 and GPT-6 Sol/Luna Launch a Frontier Price War

Anthropic released Claude Opus 5.5 on September 22, accompanied by a 230-page technical paper; OpenAI fired back within roughly an hour by announcing GPT-6 Sol and GPT-6 Luna — two models pitched as bringing "frontier intelligence to everyday work" at different capability–cost tradeoffs. GPT-6 Sol and Luna are priced at roughly half their GPT-5.6 equivalents, and OpenAI simultaneously improved prompt caching with higher hit rates, explicit breakpoints, and new latency diagnostics. Simon Willison immediately shipped llm 0.36 and llm-anthropic 0.29 to expose both sets of models via his CLI, noting that GPT-6 Luna had already been his go-to for application development. Independent analysis on the AI Explained channel describes Opus 5.5 as explicitly designed to push toward recursive self-improvement, while Two Minute Papers calls it "an incredible leap forward."

**Why it matters:** Two frontier labs releasing competing models within hours of each other — each undercutting the other's previous pricing — signals that the cost of top-tier AI capability is dropping sharply and the competitive tempo is accelerating.

Sources:
- [Simon Willison](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) — Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
- [OpenAI](https://openai.com/index/introducing-gpt-6-sol-and-luna) — Introducing GPT-6 Sol and Luna
- [AI Explained](https://www.youtube.com/watch?v=R9momwXV9w4) — Opus 5.5: How Close Are We to Automated AI Research?
- [Two Minute Papers](https://www.youtube.com/watch?v=SA9kdAX2Zj0) — Claude Opus 5.5 AI: An Incredible Leap Forward
- [OpenAI](https://openai.com/index/better-prompt-caching-for-gpt-6) — Better prompt caching for GPT-6

---

## Security Researchers Used Claude to Break Into OpenAI, Earn $6,500 Bug Bounty

A trio of security researchers used Anthropic's Claude to conduct an authorized penetration test of OpenAI's systems, ultimately accessing OpenAI's source code and collecting a $6,500 bug-bounty reward. The operation — reported exclusively by the WSJ and quickly confirmed by Forbes, The Guardian, TechCrunch, and Fortune — represents a rare and ironic episode: one frontier AI lab's model being used to expose vulnerabilities at its main rival. Coverage emphasizes it was conducted within OpenAI's bug-bounty program rules, making it an authorized ethical hack rather than an attack.

**Why it matters:** The incident shows both that LLM-assisted hacking has matured to the point of cracking production systems at a top AI lab, and that AI safety research and bug-bounty programs now need to account for AI-powered adversarial tooling.

Sources:
- [WSJ](https://news.google.com/rss/articles/CBMikgFBVV95cUxPQmNxc081M1NZa0l1MDZtRG16czdBY2M3X09PVUNCcFUzdS14ZEk1dEdDS0diT2toWlY4VmtMMkNaU1pVVDRaOEpDY0tMRi0zc3dweFpEMWZQOFpPQklqTUcwelZXelBDVXJQWE1GM25BYXgxbHc3ZHBBTk1xV3ViUzloX2s2d0tCd0RLS3lKZmFNdw?oc=5) — Exclusive | Hackers Used Anthropic's Claude to Break Into OpenAI
- [TechCrunch](https://news.google.com/rss/articles/CBMikwFBVV95cUxQS0tYS0VHd1I0cEFmd0JuMHh0SEg0NGxoMUprUDFPWVRlWWZvWE9LN0ZWMWd6Z2Utc2dlYWY2elB3Nk1xTGtRZm5aSzFDZlhfR0JRSms0NkJmVDlDY3JJYkxzU0M4ZWFLak1RSnNGNTlzWTJRZmxkbGZfUWppNUVDc3hxQUlVd01Ha1Z1U1ZYUzJReUU?oc=5) — Researchers used Anthropic's Claude to hack into OpenAI
- [The Guardian](https://news.google.com/rss/articles/CBMikwFBVV95cUxORGtkcDVTUGdMQW5OWHpxVmFVLXlyel9IRVJhNVVmTWF6NFk2enhmOFNVdnJyY3RkMzRhbWpXaXBjVWk4YzJxekdLSzM4SHJWRW56QzFWZDlncUtPdUlZb1Zva1VtdWF0anZSejVWanJnWlNhb0xXSUU3R0VRRmlneWVqMmRoUWdwMGNSd3p3TUJObUU?oc=5) — OpenAI 'ethically hacked' with help of Anthropic's Claude chatbot
- [Fortune](https://news.google.com/rss/articles/CBMikAFBVV95cUxQVW80YlEwQkJ0MlpGREhiRy12UGVkdUpULW1GUm1WenpEM2NQbGk0Z2lETGNNVlZtQVJFN3lna2Mzb0xKSWoxVzN5T19lZmwycnRJNmVlc3RRVmZLdU9Md3pDd1BVUDFiLXVXR0ZFVWhCaW9OOFM1bWxoNXFwNWlSelFVYjhCcU5kS181RUQ2VjM?oc=5) — Three guys using Anthropic's Claude hacked into OpenAI and accessed its source code for $6,500 reward

---

## Claude Now Leads a Quarter of the Work Building Anthropic's Next AI Models

Anthropic disclosed that Claude is now responsible for approximately one-quarter of the engineering and research work required to build Anthropic's next generation of models — a milestone described by AP News, Reuters, and The Washington Post as the clearest public signal yet that AI self-improvement is operational at a leading lab. Simon Willison's September 27 keynote talk "2026 in LLMs (so far)" — given at the WeAreDevelopers World Congress in San Jose — placed this alongside a broader trend of labs using their own models to accelerate development cycles.

**Why it matters:** A 25% share of self-directed AI R&D output is a concrete threshold that suggests recursive self-improvement is no longer theoretical; the rate at which AI capability compounds now partly depends on how fast the AI itself can work.

Sources:
- [AP News](https://news.google.com/rss/articles/CBMipAFBVV95cUxQTGVRMWttSER2aTljc2w3RjQ4WVNSQno4Z3FmaUVGSmllOXFKRzkzUmJXT2R6MHhZSzhaTVp2RTBXSzNJNzQ3YThfNmdWNUdEN0dNUXhwRWdxa0p0V2FFaGtlRHVHLUpmdDctWDg1N2ZnM2FWeVFZXzJOS2g5T05yYnZPYmJOMzdqeDAwUlNvMFV1TDc0MDhoVjVvVXhyRmRwQUVGdg?oc=5) — Anthropic says its model Claude is helping to build the next version of itself
- [Reuters](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPOTlkTk8zR3FVNjBtYTRfeEZQWU9zWHhWUE00dUhyMDhMUHZDRF90dlhuUDhYS3QweW9ZejB1U0tNQ0dFQjIxZ1lFLXhfdEliaHN3MzJZV0JYRnJMc0pyU2k4dmdyX2tPR1VOX0RRdmVJUkZ1bWZCcVJ5czg4XzlXQmRXaXpVYzB1a0QwRGdzUkFVbGtVY3ZJVEpKSEwzUXdMT0NaV0F1cTVQOEFhSzRTR0ZURUlzM3NL?oc=5) — Anthropic says Claude now leads a quarter of work building its next AI models
- [The Washington Post](https://news.google.com/rss/articles/CBMizwFBVV95cUxOM2lTT1pubVg3a2k2VUUzWmJEUUd4STN4UkZCLXRjb1hwcmNEUlRQYWdFQmkxeWkyR25FUEFwWXBWQWlwSUt1TldyVW1ncHhhNGpfRXhRVk9hZkk0YTBmV0RJcUpHb0dTLUZYRlF2TDRIUmd6OFpZdUpyMXlna2FGai1nNl83RDBxR1RIdjNGNnk1ZU5QSWNyUmgzREpLTTU4aU9KMkpQTXZpa3E0RjE1SEhsSk5oQmd3bEFNMkx3eVA0dXI1VDZkc3B5ZjhsbkU?oc=5) — Anthropic says its chatbot Claude is taking over the work of building its own successor
- [Simon Willison](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) — 2026 in LLMs (so far)

---

## Claude Achieves Three Independent Scientific Breakthroughs in Two Weeks

Anthropic published a cluster of results showing Claude autonomously advancing multiple scientific fields: it discovered a novel enzyme system with CRISPR-like repeats (confirmed by Reuters and Al Jazeera as a genuine molecular biology finding), computed a nine-loop amplitude in N=4 super-Yang-Mills quantum field theory — a symbolic-math problem so complex it had resisted human effort for years — and broke the existing mathematical record for computing the most complicated algebraic curve, reported by Scientific American. A fourth paper details how Claude is broadly uplifting biomolecular modeling workflows across Anthropic-partnered labs.

**Why it matters:** Four distinct scientific contributions in under two weeks, spanning molecular biology, theoretical physics, and pure mathematics, suggest AI is now capable of not just assisting research but driving novel discovery across disciplines.

Sources:
- [Anthropic](https://news.google.com/rss/articles/CBMidkFVX3lxTE9JT0FwTVctZXNkYnJXeW44aHhoZmJfbDYwN3B4a2tMTThJZm9XRklxMkEzdFlxb2Z6VGM2UnpDTGlaQ09PODJUMkJFWWl1UVZOTDJ0WU1UQ1pZMDlrbS0tM3FTS0RGWmNSeGt5QlJjZktQWkl4N0E?oc=5) — Claude discovers a novel enzyme system with CRISPR-like repeats
- [Reuters](https://news.google.com/rss/articles/CBMizAFBVV95cUxPSy1hZUZTdFRxVmt6XzZubm9GeGFET0hMaVBkaUh1aEpJVWRnbVgzdGlPZE5KQXFHOFdiRHZEQ2JZTmtaeTgzY25rY3Z6VFpMYVdkekp5SG81bEJ6Q2RRaF9VMUcwem1NS2N5dE5wcmI5ZkNoeE9TaGdNWFVtekFPVUN6eWRUeXluUFQwNVp0N18xanFEU0xwNVhiNUxnMF9xZHVMLVRwYU9LSWJmWERKSlBtdktoZ2RXbm8yY3BuRk1sSmYtX0xTSEY1M00?oc=5) — Anthropic says Claude AI helped discover novel enzyme system
- [Anthropic](https://news.google.com/rss/articles/CBMicEFVX3lxTFA0cmtPNG1Fa0prVnBpWXZmaDh4VXRGOE5haUQzQ1VjY3BpUnRJNks2UFhNdEhXdjdDaDFGbHdTX3FCTVhmeDBLdWIyZWVBVlY1T2tUMWNZYWNXX3NoaWIxdWxNQ3NLczNiSWRuTjZjWkQ?oc=5) — Claude computes a nine-loop amplitude in N=4 super-Yang-Mills
- [Scientific American](https://news.google.com/rss/articles/CBMiswFBVV95cUxOQURZTjVJM1hoVzJnSGdacHcydUhOUHR0NUhnd0pLNGw5UzBINkE1N1BSU0FjM2RZZFNGcWZWZGVZdUlwZGlXSmhqdnZMeERQMmpIcnpYRUNGN3d2aGRrWWt1UURNMzhNQU9TQnQ4SUk3YjdrZ2FJX1dJYkREbEVwVDNvZXdLVjlwYWNuZDdodHBCc2pGdWVvUk1CVWdLWlB2N3ZMdkdPcG03R01UUGFuSFo0QQ?oc=5) — Anthropic's AI steals mathematicians' record for most complicated curve
- [Anthropic](https://news.google.com/rss/articles/CBMie0FVX3lxTE5PbzNJUlpWVXZ6VzVsNU13YVBoQUNmTDNEUG83cTFoZk1oU0ZQMFJCWFhqNTFZSGVZWkg3RjBRNktiaXZjd1ZoNTRLM3NpS2V4a3lVUXRJVXFDbXVwRmhfdDlPSy04ZVBzUHB3aHFEUjRtcHVzd0dvN0NYMA?oc=5) — How Claude is uplifting biomolecular modeling

---

## Trump Orders US Government to Replace "Artificial Intelligence" with "Super Intelligence"

President Trump directed US diplomats and federal agencies to stop using the term "artificial intelligence" and substitute "super intelligence" in all official documents and communications, according to AP News and The Hill. The directive follows Trump's personal push to rebrand the technology in terms that emphasize American dominance rather than the field's academic origins. The Hill reported the policy is being applied across diplomatic cables and will eventually extend to all federal documents.

**Why it matters:** A formal government-wide rebranding of the term signals that AI policy is now being shaped by political narrative as much as technical reality — with implications for how US agencies communicate about AI risks, regulation, and international agreements.

Sources:
- [AP News](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWDBXSVlKYjVLV1hzNnphbmpRampOMGcxUDBCVDdfanV2QmNUWk5fTW5PMFJ1SzB1VUZUQ25GUG55YXgycE13eU5jSlNiUGk1MUZTSFhHQU9pSlJXX1g3Uk82QXc0YktHdVUycnF4OEplZWRyY2txSVZEQTBHMHU3VHhHSW9NUW9HdnUwelBYdHFFSWlhWnJyUVdTUWI0dE5IODNGY2NDZC0?oc=5) — US diplomats told to say 'super intelligence' — not 'artificial intelligence' — after Trump's call
- [The Hill](https://news.google.com/rss/articles/CBMijAFBVV95cUxONGozbTN6WUprdTNWTzFEemhVemQ3Zl9TTXBWVy03QVFxVnpweldHRU1hUmtOa3Y0ZHlXNGFRRkcxTzJaWEQ2ZXotVHFnQkpVUUxHT2xjYnJpa1YxdDBsSEFzNUJhRjQwSnhNcTF4R0NzTjlYTE80YkFVWU85eEVFYUsxekVJcHJ4V2JSNdIBkgFBVV95cUxNQUNPOEgtT1F0UXB1YW9rcGkwcVZWckhwN0k4bTVXdWV1aDV6MVh1c0hKR1hVVGtPWDNpMlQtZ1ZZOVV0clg3dU5XaUJKTUhabGU3Y3lFZkFPRTNxUzFyUTcyRkY3dm1TREFJdFB2Q0ZPM2RYcE5mZUFIRmN2YTBBY3VnWE51MUtBXzV5UFY2Z3poUQ?oc=5) — Diplomats ordered to use 'super intelligence' instead of 'artificial intelligence' in Trump push
- [The Hill](https://news.google.com/rss/articles/CBMikgFBVV95cUxPTHFSRVlHOGRzQlVzcWRvcHlCU2pyMGhSXzlPLUxvNnFqaldRVnpIYWJWMHpvRHY5OUR3UmV1eGtCS29LbHlHUFFDaHc5YjVhN1owS0RfT2Y1X0FSVVJsZ09WZUNNOUV4MGtZLTRMeS01bVJ2MHdaaE5VMUI3M3laVEZGejJCNHZSWDFuNWZ1NjBHd9IBlwFBVV95cUxQTnJVNkJmdXZuX2pHN0pqd1JKczNfM21JVHFLaHU5QVFHN1VERkxtNUhqQVZuZi1xaUZrZms3SzFWU201SUs2Y0cySEN2SG4wUmQ1TnVOMEo5T2lacDJpMzVoS2RwQWdUOUV2cG93bkZURUxNb2JhRkE1R1RyZlk1dkhvS1k2cGxSTjRlallVRzF4RzB4RkJr?oc=5) — Trump says AI will be renamed 'super intelligence' in all US documents

---

## AI Takes Center Stage at UN Security Council Amid US–China Race Concerns

The UN Security Council held a full session (Meeting 10228) on AI and international security — the first of its kind at that level — with OpenAI CEO Sam Altman delivering remarks calling for human control, international safety cooperation, and shared governance norms. The UN Secretary-General warned the world "cannot afford a race to the bottom on AI safety," while a separate AP report noted the US and China are competing intensely for AI dominance but share concerns over existential risks. A New York Times analysis observed that the US currently holds a technical edge on frontier models but that China possesses structural advantages in deployment scale and state coordination. On the margins, OpenAI also announced it is extending its Daybreak cyber-defense program to the Government of Ukraine for civilian infrastructure protection.

**Why it matters:** The Security Council's direct engagement on AI governance signals that world governments now treat advanced AI as a geopolitical and security issue on par with nuclear proliferation, making international regulatory frameworks a near-term reality rather than a distant possibility.

Sources:
- [UN Meetings Coverage](https://news.google.com/rss/articles/CBMiTEFVX3lxTE5LSEJvTWFHN3AwODlsTFpON2syOEVnRVJhT3BueFFGbkZsWl9ZbzJHS3ZELUxOdXZSSmNyZUFuM1ZUbHpZMjJCeFFrVnc?oc=5) — Security Council, 10228th Meeting — Artificial Intelligence and International Security
- [OpenAI](https://openai.com/index/sam-altman-un-security-council-remarks) — Sam Altman's remarks at the United Nations Security Council
- [AP News](https://news.google.com/rss/articles/CBMisAFBVV95cUxQVFZiWDFYOEI1THJDSkNUek1MV3VXcVFpOWIzLTJZMU1YLVp2bndjWEFGRkVudFZfc29USWpEYlNldnk0ZmxreTFWTWV3Q1lVNmY5UUxwUzM5bmtMcXYzSGNZUHliTXZsWUhySlZ2bkVZajJVaVJDZC12b0ZUSWNiV2tBNE1EVVphNnJNT1pPR2twaU9FSFJlUTZUQTg4RUJ2bVdXaXZrVTJxM2c4ckQ4bw?oc=5) — UN chief urges global AI cooperation
- [The New York Times](https://news.google.com/rss/articles/CBMihwFBVV95cUxNem8xbkdnZmlJMGlOaG42RHkxRDZaT2Uzd0IyVGZ1MWcyM01YOVpEbDg4WkVIam9MSThGSm12SjlsaE1WUnp0a2VOTHdCd1kxSUZPXzliLXRmQ2g0Wl9jV2w5M21BNGdIVi1xb01ZMDBhbVRuTHMwWXBiWjF0T2FHWjVhSVFWR28?oc=5) — In A.I. Race, U.S. Models Have the Edge, but China Has Other Advantages
- [OpenAI](https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense) — OpenAI extends cyber access to Ukraine for civilian defense

---

## Also noted

- [Introducing Gemini 3.8 Live with Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/) — *Google DeepMind*
- [Advancing Private AI Compute with secure, server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/) — *Google DeepMind*
- [Gemini 3.8 text-to-speech says hello](https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/) — *Google DeepMind*
- [Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking](https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/) — *Google DeepMind*
- [Gemini 3.8 TTS Playground](https://simonwillison.net/2026/Sep/23/gemini-tts-playground/) — *Simon Willison*
- [Who’s liable when AI agents go rogue?](https://www.technologyreview.com/2026/09/28/1145197/whos-liable-when-ai-agents-go-rogue/) — *MIT Technology Review AI*
- [There are no "rogue" AI agents](https://eoinhiggins.substack.com/p/there-are-no-rogue-ai-agents) — *Hacker News (AI, 100+ pts)*
- [Early rogue AI agent activity and attempts to hack found on urlquery.net](https://transluce.org/agent-activity) — *Hacker News (AI, 100+ pts)*
- [Gemini Hacked Three Companies in First Known Breakout by Google’s AI](https://simonwillison.net/2026/Sep/18/gemini-hacked-three-companies/) — *Simon Willison*
- [Jev introduces a new shape of LLM - System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/) — *Simon Willison*
- [Yes, Jev Is Insane, But There's A Catch](https://www.youtube.com/watch?v=qBBRRsH0rQc) — *Two Minute Papers*
- [Jev: System One models for Prod, not God — with Diogo Almeida, CEO, TypeSafe AI](https://www.latent.space/p/jev) — *Latent Space*
- [llm-typesafe 0.1a0](https://simonwillison.net/2026/Sep/22/llm-typesafe/) — *Simon Willison*
- [Anthropic debuts Claude Docs, raising stakes for Microsoft - Axios](https://news.google.com/rss/articles/CBMickFVX3lxTFAyNjJZVWhzbEpjOFlFOEliQzhkUjhFZllKbmlHN1dCR1FzOVpEZHRXTTdhcjFCbHJqb2twZ2dERGJUQ1JNWXZEdEVRWExaMXRhSDZ3WFBpTVM2OFhnU2FNVGRzR3FsR0djQTFZR2NRTnhiZw?oc=5) — *Google News — Anthropic*
- [Anthropic merges its chat and agentic products into one AI assistant in push to build a superapp - Fortune](https://news.google.com/rss/articles/CBMi8wFBVV95cUxQRXhiM3FncG40bjVXMDFLMTV5RnBpMzFMWTY2Qml0dUNJeWVFSTZLZ1V0bU9PUk11aC03VDZQUFdpN01sZXUtdEUwblVFUjBSN183bWNEd09pR1FTQmowdzd5ZEk1Y0RTRUhwb0hxWEtqVUQyS3ZBaVFVZzk2NXA3TEhGZmJJb1poSWFvWE1yQWNmazBsM29rbjlmQVR4ZGtPTU5GcFg1aVBJd1lWdE43NHBrMzRVb1E2UENac3Brd3JPQVJNM1E1aHN1VWV3YzlvaFFLWF9mM0F6c05kLTRHTWl5Z09vLVB1b1Z3aV9KeGFoamc?oc=5) — *Google News — Anthropic*
- [Anthropic merges Claude chat and Cowork in one interface - TechCrunch](https://news.google.com/rss/articles/CBMilgFBVV95cUxOLTEzdFVRZC1oTllOZlEzMms5b3ZHeTZHRXR4SXBlX2U2RW1Ick04YUFJeW5SdVNsTzJzeXpaRmFsX2ZRZWh5eEVocU1QVEM0UkQ5Qm5qZTNocVA1LVY0Sms1cjVDQXhaMVpydWtFV1JoRGFlZVpkTU9GbjJ0ZVV6ZUVxMng2T0ZhalVON0ZmNjI0MkNrSFE?oc=5) — *Google News — Anthropic*
- [Anthropic's Claude Can Now Create Editable Documents For You - Engadget](https://news.google.com/rss/articles/CBMitAFBVV95cUxPOTk4eFFyWTNOczB2S3NaazNrN2dXYzI1elFIbFVGMzZjT0J2YlRDdWhHeEFwbW1ES3ZQSGduRUFLWjN5ekpoS0YtalBreklOX3lWNXpjWkdiMUp4Z2JLLWkzVlA4eHV4UE8zV29hYXVXMXRfZ1RWbUZ2RGVPblVrUEJKaWlLUzRKRzYxTlctSHdIYjdENTJ5RGVuMjhfbTB4b0VISFhsU2RVVGRFVFkxQmtLNDc?oc=5) — *Google News — Anthropic*
- [Anthropic Launches Claude For Advisors With Schwab And BlackRock - Forbes](https://news.google.com/rss/articles/CBMitwFBVV95cUxNRktmYWhfak5Yd1VDdGtxeWVSYUFrYjhjZ1Bqbms4X0k3cXpFN1lPVUhha3ZqQURCeWlPX3A3N0s5a1pFZnByOVVsbW85ZzRWSDZwRDJNdXg0akpKenBUV1JPXzFtYkl3eF96aEpxci1YVWJKRHdIekRJU0Y1RFgtUUg2OUVwc3RlbkRFS2xrR1haVHhhOUJ6UEhRTmItZ3Bzd3dfaXY4VW44bGNFNnljdjZpWHZhUGM?oc=5) — *Google News — Anthropic*
- [Anthropic Just Put Claude Inside Schwab and BlackRock. The AI Agent War Has Reached Wealth Management - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQc0xOSXo1enNVYTJheU9Yb2tORjZGTng4bmdDTDJFbmNwOG9QVWFqTi1RSVF3TVRKQXZFeHJqVmx3NllTTXFhd3pIcEVBQV9tcTZlVkljVTdUZEFaNm5iYUJZM2lIeFV5dEw5VDFNV25ZMmlheWFOeGZSRWQ4QVZwQVJBMjI3VVVNNFlqcjM1RnJfejNDNlBjZlhjaXY?oc=5) — *Google News — Anthropic*
- [Anthropic launches Claude Code Projects, an ‘always-on’ conversation that remembers and delegates your long-running dev work - VentureBeat](https://news.google.com/rss/articles/CBMi8AFBVV95cUxPbzFBR1I0TUFsdkpnMFY2amNCMzJuRFlxS2tCZ1JiWEFhOVl0WkJBU1pBSkZha0hHWEdMYTFGc201QmtVUGFFU2VnQUh2UW9ucHp5V1Y2Uk10WlBWbjdvYTBjX0JfTDB2MUJDMnFRNkstUG9iNU1hQnV0TXJDcHhhbkdKenEyMVREQ3BVMzdEdnlEN1VKLXpGQXRMRTJGMHlLSzY1TUZSeWEyU0pqMy1SX20wRHJIVTgwZXpqWHVLY184Y09GS0M1M2VCU29ZN1JjYWNGelUya0NmOGxkdVRubnVGM21SM0t1OTJNUmZLbFI?oc=5) — *Google News — Anthropic*
- [Anthropic’s new Claude Code feature could drain your plan before lunch - The New Stack](https://news.google.com/rss/articles/CBMiY0FVX3lxTE0xMkdGYnpZQ0E5SU1yelZSVVM5d3dqV0g0aWVzNUw1WVItbjBnNFF6dG85TlZNc09rQ3IzZnR0bjUzbmhSNXBjdWdTTWNwQTdTU2Jjbm5Fa1I5V2tCZDc4ZXFkRQ?oc=5) — *Google News — Anthropic*
- [Introducing the Life Sciences Verification Program - Anthropic](https://news.google.com/rss/articles/CBMic0FVX3lxTE1tdEtSOC1PRVFaSWU5TmlaMEtiZjRMdDdJLWg1bVIyUzlUTUV0UHZVa1Z3Y2JYeVVVLVEyeGZIQnVHR01tdC04X2x5Vk5LNDRKa3VyWnB2Vks0U3JpZDNNemZxczNDOFBNeGxrQnViOFNJQVU?oc=5) — *Google News — Anthropic*
- [Pentagon says overreliance on AI contributed to missile strike on Iran school](https://www.bloomberg.com/graphics/2026-iran-school-attack/) — *Hacker News (AI, 100+ pts)*
- [The Pentagon wants $30 million to build an AI-powered lie detector](https://www.technologyreview.com/2026/09/25/1145144/pentagon-ai-lie-detector/) — *MIT Technology Review AI*
- [Classified estimates show the NSA is paying billions to test AI models](https://www.washingtonsun.com/technology/classified-estimates-nsa-paying-billions-to-test-ai-models) — *Hacker News (AI, 100+ pts)*
- [The Download: the Pentagon’s AI-powered lie detector and young organ limits](https://www.technologyreview.com/2026/09/25/1145157/the-download-pentagon-ai-lie-detector-young-organ-limits/) — *MIT Technology Review AI*
- [S3 Is the Future, S3 Is the Past](https://simonwillison.net/2026/Sep/27/hn-49871741/) — *Simon Willison*
- [Bluesky reply bot checker](https://simonwillison.net/2026/Sep/27/bluesky-bot-check/) — *Simon Willison*
- [Kākāpō Party](https://simonwillison.net/2026/Sep/26/kakapo-party/) — *Simon Willison*
- [Quoting John Gruber](https://simonwillison.net/2026/Sep/25/john-gruber/) — *Simon Willison*
- [Northern Gannet, Great Blue Heron, California Brown Pelican](https://simonwillison.net/2026/Sep/25/sighting-403293902/) — *Simon Willison*
- [Note on 24th September 2026](https://simonwillison.net/2026/Sep/24/harder/) — *Simon Willison*
- [commit-rewriter 0.2](https://simonwillison.net/2026/Sep/24/commit-rewriter/) — *Simon Willison*
- [datasette 1.0a41](https://simonwillison.net/2026/Sep/24/datasette/) — *Simon Willison*
- [We just shipped support for the ugliest part of HTTP: Vary](https://simonwillison.net/2026/Sep/23/hn-49823961/) — *Simon Willison*
- [SF October 14th: A Birds of a Feather Session on Agentic Engineering](https://simonwillison.net/2026/Sep/23/bof-agentic-engineering/) — *Simon Willison*
- [Quoting @therealcornpop](https://simonwillison.net/2026/Sep/22/therealcornpop/) — *Simon Willison*
- [Quoting voxium](https://simonwillison.net/2026/Sep/20/voxium/) — *Simon Willison*
- [MCP was always a bad idea?](https://simonwillison.net/2026/Sep/20/hn-49779718/) — *Simon Willison*
- [llm-keys-ui 0.1](https://simonwillison.net/2026/Sep/20/llm-keys-ui/) — *Simon Willison*
- [datasette-explain 0.2.2](https://simonwillison.net/2026/Sep/20/datasette-explain/) — *Simon Willison*
- [datasette-auth-github 1.0](https://simonwillison.net/2026/Sep/19/datasette-auth-github/) — *Simon Willison*
- [California Sea Lion, Brandt's Cormorant](https://simonwillison.net/2026/Sep/19/sighting-401567341/) — *Simon Willison*
- [Note on 18th September 2026](https://simonwillison.net/2026/Sep/18/probably-gonna-eat-you/) — *Simon Willison*
- [Quoting Thariq Shihipar](https://simonwillison.net/2026/Sep/18/thariq-shihipar/) — *Simon Willison*
- [Quoting Muse AI Agent](https://simonwillison.net/2026/Sep/28/muse-ai-agent/) — *Simon Willison*
- [Proaction boosts sales 60% and saves 75+ hours with Codex](https://openai.com/index/proaction) — *OpenAI News*
- [Two years of OpenAI Academy](https://openai.com/index/two-years-of-openai-academy) — *OpenAI News*
- [Harvey turns legal context into stronger drafts with GPT-6 Astra](https://openai.com/index/harvey-from-context-to-confidence-with-astra) — *OpenAI News*
- [How invideo improves color grading 3x with GPT‑6 Astra](https://openai.com/index/invideo-builds-with-gpt-6-astra) — *OpenAI News*
- [Ringg’s AI agents resolve up to 65% of customer calls with OpenAI](https://openai.com/index/ringg) — *OpenAI News*
- [Introducing MentalHealthBench](https://openai.com/index/introducing-mentalhealthbench) — *OpenAI News*
- [ChatGPT Ads expands to Southeast Asia and Taiwan](https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan) — *OpenAI News*
- [Airbnb widens access to GPT-6 Astra and OpenAI frontier models](https://openai.com/index/airbnb-gpt-6-astra) — *OpenAI News*
- [Grab and OpenAI bring practical AI skills to Southeast Asia](https://openai.com/index/grab-openai-ai-skills-southeast-asia) — *OpenAI News*
- [Priorities and principles for effective third party assessments](https://openai.com/index/priorities-principles-third-party-assessments) — *OpenAI News*
- [Higgsfield AI ships new video features in a day with GPT-6 Astra](https://openai.com/index/higgsfield-from-prompt-to-production-with-astra) — *OpenAI News*
- [Advisory Group on Mathematics and Artificial Intelligence](https://openai.com/index/advisory-group-on-mathematics-and-ai) — *OpenAI News*
- [Building standards for the next phase of AI](https://openai.com/index/building-standards-next-phase-ai) — *OpenAI News*
- [Expanding OpenAI Academy with new learning paths](https://openai.com/index/expanding-openai-academy-with-new-learning-paths) — *OpenAI News*
- [V7 cuts costs 78% while boosting accuracy with GPT-5.6 Luna](https://openai.com/index/v7) — *OpenAI News*
- [Introducing the Australian Youth Safety Blueprint](https://openai.com/index/australian-youth-safety-blueprint) — *OpenAI News*
- [How Cooley is accelerating IPO work with ChatGPT](https://openai.com/index/cooley-gopublic) — *OpenAI News*
- [Introducing Astra for Law](https://openai.com/index/astra-for-law) — *OpenAI News*
- [Helping older adults use AI in everyday life](https://openai.com/index/helping-older-adults-use-ai-in-everyday-life) — *OpenAI News*
- [Reimagining advertising with AI](https://openai.com/index/reimagining-advertising-with-ai) — *OpenAI News*
- [Hex turns complex analysis into visual reports with GPT‑6 Astra](https://openai.com/index/hex-gpt-6-astra) — *OpenAI News*
- [How to connect AI usage to business value](https://openai.com/index/how-to-connect-ai-usage-to-business-value) — *OpenAI News*
- [Our framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework) — *OpenAI News*
- [How workers are unlocking new ways of working](https://openai.com/index/unlocking-new-ways-of-working) — *OpenAI News*
- [How Fyxer built an AI executive assistant people trust](https://openai.com/index/fyxer) — *OpenAI News*
- [Accelerating vision-language models with LFM2.5-VL-DSpark](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark) — *Hugging Face Blog*
- [How to Use NVIDIA Warp and MjWarp to Accelerate Robotics Simulation and Learning Workflows](https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp) — *Hugging Face Blog*
- [How UK AISI and EvalEval Are Making Benchmark Results Reproducible](https://huggingface.co/blog/evaleval-aisi) — *Hugging Face Blog*
- [Transformers now runs llama.cpp quants](https://huggingface.co/blog/transformers-llama-cpp-quants) — *Hugging Face Blog*
- [Jun Kim, oMLX creator and maintainer, joins Hugging Face to support the MLX community](https://huggingface.co/blog/omlx) — *Hugging Face Blog*
- [Pruning LLMs Like a Physicist: Block Removal as an Ising Optimization Problem](https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an) — *Hugging Face Blog*
- [tokenizers v1: encode, decode and scaling, measured](https://huggingface.co/blog/tokenizers-v1) — *Hugging Face Blog*
- [Your Agent Aced the Task. Will It Do It Again?](https://huggingface.co/blog/ibm-research/altk-evolve-consistency) — *Hugging Face Blog*
- [Import AI 473: The US’s superintelligence strategy; human brain in a mouse skull; and machine hermeneutics](https://jack-clark.net/2026/09/21/import-ai-473-the-uss-superintelligence-strategy-human-brain-in-a-mouse-skull-and-machine-hermeneutics/) — *Import AI (Jack Clark)*
- [Show HN: TinyAIArena watch AI agents battle it out](https://tinyaiarena.com/) — *Hacker News (AI, 100+ pts)*
- ["As a Language Model": Chat Template Switches LLM Self-Referential Voice](https://arxiv.org/abs/2609.25021) — *Hacker News (AI, 100+ pts)*
- [Too AI; Didn't Read](https://www.tai-dr.com/) — *Hacker News (AI, 100+ pts)*
- [Microsoft abandons personal AI chatbot race with Copilot reboot](https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot) — *Hacker News (AI, 100+ pts)*
- [Evolving programming languages in the AI era](https://dashbit.co/blog/evolving-ai-era) — *Hacker News (AI, 100+ pts)*
- [AI safety is mostly a sex cult in Berkeley](https://www.verysane.ai/p/ai-safety-is-mostly-a-sex-cult-in) — *Hacker News (AI, 100+ pts)*
- [Best LLM for every budget, updated daily](https://bestmodelforyourbudget.terrydjony.com/) — *Hacker News (AI, 100+ pts)*
- ['That's so AI ' What gen Alpha's biggest insult tells us](https://www.theguardian.com/society/2026/sep/24/thats-so-ai-what-gen-alphas-biggest-insult-tells-us) — *Hacker News (AI, 100+ pts)*
- [Meta takes down a critical video about meta AI Glasses after filming at Meta](https://www.reddit.com/r/facebook/comments/1wotwrk/meta_takes_down_a_critical_video_about_meta_ai/) — *Hacker News (AI, 100+ pts)*
- [Feds Target AI Critics as "Foreign Agents"](https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign) — *Hacker News (AI, 100+ pts)*
- [Mercury 2.5 LLM hits 770 tokens per second](https://artificialanalysis.ai/models/mercury-2-5) — *Hacker News (AI, 100+ pts)*
- [Stripe's Knowledge AI Platform](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform) — *Hacker News (AI, 100+ pts)*
- [LLM Ass Bench](https://www.assbench.com/) — *Hacker News (AI, 100+ pts)*
- [Psychiatry, Insane Asylums, Mental Illness, ECT, Lobotomies, Freud & Jung | Lex Fridman Podcast #502](https://www.youtube.com/watch?v=s7d2d8FhevU) — *Lex Fridman*
- [DeepSeek’s Insane New Architecture](https://www.youtube.com/watch?v=vIHw_2VjSUw) — *Two Minute Papers*
- [Claude Is Now Leaving Invisible Fingerprints In Its Text](https://www.youtube.com/watch?v=YoEWjZSwoys) — *Two Minute Papers*
- [What AI Researchers Saw, Before Their Demand to ‘Pace’ AI](https://www.youtube.com/watch?v=J3ljHm57yU0) — *AI Explained*
- [OpenRouter: from Seed to Stripe — with OpenRouter’s Alex Atallah & AMP’s Anjney Midha](https://www.latent.space/p/openrouter) — *Latent Space*
- [Runway’s WorldPrompt and the Engineering of Real-Time Worlds](https://www.latent.space/p/runway) — *Latent Space*
- [🔬Bio-security is an AI Arms Race - Eric Nguyen (CEO, Radical Numerics)](https://www.latent.space/p/bio-security-is-an-ai-arms-race-eric) — *Latent Space*
- [🔬 An Oscar, Two Asteroids, and the Algorithm in Your sklearn: John Platt on AI for Science](https://www.latent.space/p/john-platt) — *Latent Space*
- [Underwriting Superintelligence: Backing Agents you can Sue — Rune Kvist, AIUC](https://www.latent.space/p/aiuc) — *Latent Space*
- [Humanity’s Last Invention — Richard Socher of Recursive](https://www.latent.space/p/recursive) — *Latent Space*
- [How Insurers Are Responding to AI Risks - RAND](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBGM2VWeUxRTGJWLV9IU2lFRXlNZkR5ZlhCMzRHRFAxZlg1TklBM0RpeEtEaUs5aVI0ZUhOZWxqX0QxT1FNcW1DSTh0NFNQbkEwZUE2djg2TmVWMWdIc3FYakNkYndlY1h6?oc=5) — *Google News — AI*
- [Artificial intelligence now beats some of the best human forecasters - The Economist](https://news.google.com/rss/articles/CBMixwFBVV95cUxNOVE2WlNjSlVyUjdJZzRYT1ZTSlI1cWFHdHJYcHhMNnREaXYzRzhINE8xWHZIZmh2TTFaOGllS0lTVU5sNDctUzhuOXpNQi1BbjBwalduUkE3SllUbEp3ZTFveEVZajZwOGRSVXhDaS02bnVCMkM3OWdBZTd5STl4a2dBbjNidGhpSlQ1OXlCanZRaXpoay02TU45cXk5b2c5dndkQnRCVHdCbUxvV1ljTkNtMmY4aDFnUEFHNm5iMGdhWjB4SHNR?oc=5) — *Google News — AI*
- [Advisory Group on Mathematics and Artificial Intelligence - openai.com](https://news.google.com/rss/articles/CBMib0FVX3lxTE50TVpFbHFkWkJyVkNRV1l3T0VTb3V4YmFhOWZsd19nNEYwV0ZsVURHeElOMG8zYVNRc0NEYUxMYkNua3ozeXBGTTdoRlY5amo1b3dIU3o3TkxUQ0VHRnZ1STYta0FkM3NxZ0dob2Npdw?oc=5) — *Google News — AI*
- [Artificial intelligence and machine learning in nanoparticle drug delivery systems - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBtbjJsZ0xhQ1VCN0lrWHNGaXk5bnlnMFc4RUh4dUJhSU45cHZLdUJWVzlLWDA0eHZFLVVBTmI5TlFWYkJ0MWhRUU1oWVc3ekE5c3c0Si1hT2xGNVRyVjdv?oc=5) — *Google News — AI*
- [Rice University to offer Master of Artificial Intelligence degree program in 2027 - Houston Public Media](https://news.google.com/rss/articles/CBMi3gFBVV95cUxNakNpSWY4VDVyWDQ1QWlZR2lZWkExY3dlMGJMNTdQWEFJOVFWYXAzSDVlQWdaZmp0a0tOcjEzcW9YZDEzNXFVam93UWFkZWV5bFBxcXh0MkNyZTVNMkUyTkpLWDMtNGl3OUdZWVNKNjh2bkx5ajFCMjVUMkI5N3dELUZhT21oSFpaM1ZxbTIzQ2FaaW9IcGM3QW1MUFcySXRtZXlfelhUYk00Q0U1ZUExem1lS1FMRE0zdDZ3TUlibnhPX2V5RGZ0LUNTTnFCVzc2b1ZhSGMtdVpTRGxTY0HSAeYBQVVfeXFMTzlKbi1DbVE5TGkyU1E2VnJ4TjBBLWdxelRnR2FNNFExbWllUy0wQWhfUUlNMjhWM0xzRnB3bHdacFlNOGcyaS1xYnlwUUsxcnF1bXhReXA5cnpnLWM0cU1Bc25DZkoxY05XbzdtZkN4ZzJ2ZzFib3NjSFFseFFUQXJCeS10RWN0VlZ4LTB5bkpqclRDWHNNUzNibWFHZDg1blBWMHFEanhlaHpGOS1VRXpiN3Exa1Ezb2NjOEdBNGxNZ3QwZlBYcjlrOUVzdzQ1XzJfREg0NlhqUjFsQnBXZzZOT1NxMnc?oc=5) — *Google News — AI*
- [Rice to launch Master of Artificial Intelligence program in fall 2027 - Rice University](https://news.google.com/rss/articles/CBMilwFBVV95cUxOTXQtQUg4TzFRWUlFSWNjR2o3RVpUMnQzZWxjYWV6Y2ZZZV91OFlRT3RBZkNLdHlhcGNObFBhUUFOcExYVVR6M2x0RWxsVU1GNUVMUC10X3ZpdVZHZW5SQW1FVXBSV2hVdG5zMFhTOW9STVQ2RGkteWx0WEk5Ym5URTVtVTJ1YjhSSkZTUHNQVzA1ZXY0RFJR?oc=5) — *Google News — AI*
- [Syracuse University Launches Institute for Artificial Intelligence - Syracuse University Today](https://news.google.com/rss/articles/CBMioAFBVV95cUxPZE1XYmgyRkg3cWI2bmM1d2hVQmViV3lmT3NxQ05kQXFhbnBBYXFKVzZrU0E0dHpSRDRHbWY2eEJTYmJnR2pHX2hBWUJIMno1MWN3eWFHVHRXZFdUdmxJR0g3RzktemxNZWtHQkplOHhTbmJxNW1kR1lXS0ItblBZcWxOTGFLYlV5aXRQdVRva25MWjBHSGtPU1RpNmpGbjNz?oc=5) — *Google News — AI*
- [Why I’m talking about coffee in a column about artificial intelligence: Letter from the Editor - Cleveland.com](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNQ1ZHZkVBal9EREw5c0lTSndMN1JkN1g4dWxfdzYtcDFSWUVBOXpJQzFieHNsYjcwUHZ1UU1oSWZXbFJCMWM4VkNGLUxSaF91Wl9Ic2xTakxuRlFHQ3pPWmd6aHRLbGR1TUlUcHo1MGtva3ZBLWx0SS1ZN00tSWp6c2dMb3k1NVJtUXZCOFpnNmw3M1ItUEkxUm4xeC02eGZia2ZWOG9vWTNWRW91N2JyYlF0TVFjejVKUGdaQkx3Vkt6dEZYSGV1YmtkRGdSMmVvcVHSAeYBQVVfeXFMUHpjcnhpMTRhd2l5Ml9DSUhXNU9HQWNsb2NyX3RnTHE1b01IQnEtWDUzMXdvTFEtaF9xa3RxZjN2TGhCanJuN3FLdkE3ZlNleVlwcC1BRVpWZDA3dm5neG5RUzFxTzhEdVVOUEgxNmUwRlZ3T0NGQXl1bDVQelhRQTducTlZUndQSUg5czNUcjVQZ2wtRkpCSlc4NVh6b2ZHQ0xBTTg2ek8tb1JVblFFUWpXZVF0VU1EWTZiNzhSN0p6Y183V3FNLTJfT0dmQ1pGdmRMS3JzakZsZ19sWGgyUWhLNW5Dbnc?oc=5) — *Google News — AI*
- [Artificial Intelligence, the Erosion of Mystery, and the Degradation of Questions - Spectrum Magazine](https://news.google.com/rss/articles/CBMitgFBVV95cUxNeGpsMHU1OVFvY014amNpMXZ6NmJ1YWRqdVhaWHZLY3lFekVwQm1YMGhnYjZOX2xDTjVPYjc3dTl0MTI0MUJMdEVIZG9pekw1WlIwcW1TVzVRS05pUHIzYkdBYnFtNEdWTVlPbFV1Yk9tWlB6eFRYTnRmcDktaFFiM2ZxNlVnSHI1aHBJNDlkWm5Qa2M2enNjUW1wa0I3MUNreHdHMzRRSGc0ZW5oR0RpQjBsaVU4QQ?oc=5) — *Google News — AI*
- [Will artificial intelligence really kill us all? - CBS News](https://news.google.com/rss/articles/CBMigwFBVV95cUxNYnNRUHNqeU5NNTVIVVhEd3F1QnY1d3JlYVZaUUJPejViZ0ZuU2c5dkNFS0F2M2x0Y1dDYUFaU3hXV2NkMk5scksteWRROHNMQjV5UEU4cnQzSU5BWW5uNHIzX1Q4TmhjWFRBVFNlYlUzLUhRVmt3RjdNT3psaUREdzRUNA?oc=5) — *Google News — AI*
- [AI risks: Will artificial intelligence really kill us all? - CBS News](https://news.google.com/rss/articles/CBMihAFBVV95cUxOc2xwbHJFXzhsbEhGWTV3N1hQbTJONzFSZ2VrOUZQYlNWRGNoVHEyZGlYU3hRNEczdkhZQmhMU21DQjM4cHoyX1VoN1hqT3h4eHBLQVNaWXBvV1RoRU01dlJhNFowbTdoalk3N0JKU3lrZGxhUWtTQjFnWS1SejJJUnFSdE0?oc=5) — *Google News — AI*
- [The intersection of human evolution and artificial intelligence - news.asu.edu](https://news.google.com/rss/articles/CBMikgFBVV95cUxQaGV3bHk1eDRUeEpHYnNEbzdZUzdsbGY2WUtSQ1o4TWVDNXRWRGJlQTBfZlNRNXY5SFVsaGY0ZG83OTh3ZktlZGJQVUU0MU15Y1p0TFAyaHNyWllaQXZmSERNcWFuU2sxNnNaNWtQc0tqeGt5VEZUa1ZzUGNFT2FhNFVWNTlXTEZBOHQ0NC0zakkxZw?oc=5) — *Google News — AI*
- [The next AI divide is between learning and earning - The World Economic Forum](https://news.google.com/rss/articles/CBMigwFBVV95cUxNTG5RQ3pSQWJMM0l1czh6dXo0NlFmWWtkOE9WZUx3c3dSQng3U28xNGdPY09iWlRfWUp4YU1vcDFKNHlEWHBoc1UyRV8yUXlSNnZCWHpjcFB6UjJNemdJRG9SU1h4N29qcWtVUng4UW9aeGJ2dUlPd0h4Unh5ZmYtQktlcw?oc=5) — *Google News — AI*
- [Positioning Artificial Intelligence to Help Explain Unexpected Cancer Trial Outcomes - OncLive](https://news.google.com/rss/articles/CBMiswFBVV95cUxOZklWcy16d1lYMTNhcUxSLU9iUXI1NHIyVGVBZjZ2Rlphd3JKN002aklUMExBdlRKVXBka1B5MWNpSGFzVE16cVZPMEIzSHk0dFFYX3pVSU0yUmxGZU5nSTMyc1lHM0RVdmROOXVwWFZZeHlTRXktWmlZaXhndk9QVk9MQVBSMXdXdE5jQ1J4X2R0eGE0VnV2Z0hVX3ExS2JRRzlEMmRZUU00Z2VuYm1iekJBYw?oc=5) — *Google News — AI*
- [Opinion: Colorado should turn artificial intelligence skills into apprenticeships - The Colorado Sun](https://news.google.com/rss/articles/CBMie0FVX3lxTE5lUUFPWnFaampEWGJmT0o3X3JwRENzb0NnbEJLaGFDLTZldGxHcGJBNTk4cHdLWW1aR1ZaT1YwbnJ3N2RaaXVSUkJDU3liUjk3bTkydXFuQXpxRzV6bTRLNlJiWENUY2Z0WjUtc2ZERHNPcDVYOWRGZFhpbw?oc=5) — *Google News — AI*
- [Counter-terrorism operation leverages artificial intelligence to identify 126 terrorism suspects - Interpol](https://news.google.com/rss/articles/CBMi4AFBVV95cUxPYnd3WjRQQmR0R29RNGp0VVQyRmdxX25yQ0Z1Y0NTZTJjeHlrTW9xU240Y09ZUzlJUHNTTGIxbWF4emtUbXNRcmpXWDl4M1lFb3hwS2MzQ0NKWXoxV2E2RjY5N0pURzd4SnNWajNuYVhQV2VSMmVrWUVCdU5IVXNrMXBaNHUydVNabklhaFZSYTlPaS1YMmZlQzNkamVvdTZOZ2VhRzNzNGhzS3M5ZzBQcUZ3UUN6VVpsQlAyekUyUWVDd1I0TTl3WkNqVThOQ0tjYlhPNXU4VDhueEs2OVE3Tg?oc=5) — *Google News — AI*
- [Call for papers: Advancing research on the Ethics of Artificial Intelligence - UNESCO](https://news.google.com/rss/articles/CBMinAFBVV95cUxOYnM5SmxmRGY5Z1NzeVVjX1VZX1dpZU1VRlB6UTNPVWRLYklpMzhSd3JaV0Z4VlZrTDdqQmdvRjhQZDlOMEYzMGFYSGFieVpMdVpKZDBZTnZTTEprUm9lMlhxT3F1X0VNbjNILTRWMkE5eHMtWXBrMTN1OEZJdENKSExRSl9iNlU4Wmp6b2RiSGxab0hCOVdWd1YxN2c?oc=5) — *Google News — AI*
- [Atrocity Alert No. 495: Artificial Intelligence and Climate Change - Global Centre for the Responsibility to Protect](https://news.google.com/rss/articles/CBMibkFVX3lxTFA3YlE4S2d0ZnlWRE5oVGNGb2hzaHI3WVJuU1JtZllEUnZIdmw2ZXVZbnoxaXlxMGszR3lZY1k2cGNMZ0hiWU5IMjREd2JoamRuU3Q4bldpa2cxM0RNdVUwbks3Y1phbk04T3NmLUR3?oc=5) — *Google News — AI*
- [OpenAI, Anthropic and other artificial intelligence companies hire Tennessee lobbyists - Tennessee Lookout](https://news.google.com/rss/articles/CBMixAFBVV95cUxPckVSaWJHSVkybmpSWmhPN3NuLUNYWGM3ZDBvQ1E1R2NkLS0tWWVTeFVTTTNiZFdHZWdkQ0pibXlQd0FIZUktQUtqUElXT0E5NV9wUGd2V2RoZ2hJMWFjaTRaSV9fbjdUVmt2VEpWWFFmVlJCbjBheXF4NTA5QW5qVWt4blpCbTdiQWRkRER6SElabkl0WTRmYnVyaEFtVjVVSVVlU3l0Rk5QYjBUVGo0WGFvT3ZkV3F6anYxdVN2ZkZDYWpv?oc=5) — *Google News — AI*
- [Could AI pose a serious threat to our existence? | Letters - The Guardian](https://news.google.com/rss/articles/CBMinwFBVV95cUxQMUVzaDBWS09WZWNFRkNlS3RObzI4S2RhaDJweFZVWFpGaFVUU2REUlN1SDVFWWFVWUMxV3JNZTVTLTZVYTVFa3dXSGczalFiQVQ1R0cyOU9LQks0Qm5XczV0aDBUNVFBZ2Z5MlBDc2pDRy1ZeGxVemxSdGdPTFBUWkF2ZFVJRkFFcm40RG9vYTJEVGJranlBREVoTHRGV0U?oc=5) — *Google News — AI*
- [How New York Can Influence the Future of Artificial Intelligence - New York Focus](https://news.google.com/rss/articles/CBMijgFBVV95cUxNUVhKRW1KVzJ0NzBwWHAzWUxnbUtRMlhpZF8wdGFqMFRhdWhLUU5HQWxVdzdhWFplODJfUGcyS3h6cXFUdFlPMFdYU25jV1UtZG1leXdCU2c4QlJtTi1XVjNXNTNHRExoSjZxOHZNQ01EQWtQZktTV2JvY3V0cFhTQ09rRk5lTV9ZMUI1U0VB?oc=5) — *Google News — AI*
- [Young organs may not be a fountain of youth for recipients](https://www.technologyreview.com/2026/09/25/1145083/young-organs-may-not-be-a-fountain-of-youth-for-recipients/) — *MIT Technology Review AI*
- [The Download: a bid to scrap the virtual wall and AI hits Climate Week](https://www.technologyreview.com/2026/09/24/1145064/the-download-bid-scrap-virtual-wall-ai-climate-week/) — *MIT Technology Review AI*
- [AI is dominating the conversation at Climate Week](https://www.technologyreview.com/2026/09/24/1145048/ai-climate-week/) — *MIT Technology Review AI*
- [A congressional representative just proposed killing America’s border tower program](https://www.technologyreview.com/2026/09/23/1145002/a-congressional-representative-just-proposed-killing-americas-border-tower-program/) — *MIT Technology Review AI*
- [The Download: India’s smart glasses menace and AI’s trillion-dollar gamble](https://www.technologyreview.com/2026/09/23/1144966/the-download-india-smart-glasses-ai-trillion-dollar-gamble/) — *MIT Technology Review AI*
- [The AI Hype Index: AI loves cheating](https://www.technologyreview.com/2026/09/23/1144940/ai-hype-index-ai-loves-cheating/) — *MIT Technology Review AI*
- [Smart glasses are already causing havoc in India](https://www.technologyreview.com/2026/09/23/1144953/smart-glasses-havoc-india/) — *MIT Technology Review AI*
- [Project Swap: What happens when agents trade for us? - Anthropic](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9QNW9yOVdvcUdTcThnUGpqSzJjbmZoY2lneThEZFNacjBKdzN6N2xFYXQzSjBKSXdsVk9ZRXotZjhjeVVtcXRJbGpNTDhSSUc1ajVKUTZOamVMcVE?oc=5) — *Google News — Anthropic*
- [How I changed teaching after AI managed to do all my homework assignments](https://thelastsoftwareengineer.substack.com/p/how-i-changed-teaching-after-ai-managed) — *Hacker News (AI, 100+ pts)*
- [Tutoring company tells parents to save their money and 'use AI instead'](https://www.afr.com/policy/health-and-education/tutoring-company-tell-parents-to-save-their-money-and-use-ai-instead-20260923-p60z0r) — *Hacker News (AI, 100+ pts)*
- [One Month Without AI](https://blog.bustikiller.com/2026/09/25/one-month-without-ai.html) — *Hacker News (AI, 100+ pts)*
- [Parallel cut research time and cost in half with GPT‑6 Astra](https://openai.com/index/parallel-cuts-time-and-cost-with-astra) — *OpenAI News*

