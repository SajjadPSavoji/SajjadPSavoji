<p>
<a href="https://sajjadpsavoji.github.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" width="100%" alt="Sajjad Pakdamansavoji, Lead AI Research Scientist at Upwork. I post-train foundation models and keep them improving after they ship: today the LLM behind Upwork's job-post agent, before that robot VLAs and world models at Huawei.">
  </picture>
</a>
</p>

<p align="center">
  <a href="https://sajjadpsavoji.github.io"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-website-dark.svg"><img src="assets/link-website-light.svg" height="34" alt="Website"></picture></a>
  <a href="https://scholar.google.com/citations?user=DZzLzNwAAAAJ"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-scholar-dark.svg"><img src="assets/link-scholar-light.svg" height="34" alt="Google Scholar"></picture></a>
  <a href="https://huggingface.co/savoji"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-huggingface-dark.svg"><img src="assets/link-huggingface-light.svg" height="34" alt="Hugging Face"></picture></a>
  <a href="https://www.linkedin.com/in/sajjadpsavoji"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-linkedin-dark.svg"><img src="assets/link-linkedin-light.svg" height="34" alt="LinkedIn"></picture></a>
  <a href="https://x.com/saavoji"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-x-dark.svg"><img src="assets/link-x-light.svg" height="34" alt="X"></picture></a>
  <a href="https://forall-labs.github.io"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-forall-dark.svg"><img src="assets/link-forall-light.svg" height="34" alt="Forall Labs"></picture></a>
</p>

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/highlights-dark.svg">
  <img src="assets/highlights-light.svg" width="100%" alt="Highlights: 1st place in the NeurIPS 2026 BEHAVIOR Challenge with team The North Star. 1M+ daily users on the LLM my team post-trains at Upwork. 13 papers and preprints on LLM post-training and evaluation, robot VLAs and world models, and 6D pose estimation. 3 patents filed on robot VLAs, world models and 3D vision.">
</picture>
</p>

## About

I take foundation models from research to real use: I post-train them on real data, measure exactly where they fail, and keep them improving after people start using them. Over the last six years that has meant LLMs in production, robot policies in simulation and on hardware, and 3D vision for warehouses and city streets.

**What I do now: LLMs at Upwork.** I lead a five-person team that owns the model writing job posts inside Upwork's AI agent, used by more than a million people a day. We replaced a paid API model with an open Qwen model that we post-train ourselves on 100+ GPUs. It costs about 70% less, judges rate its posts 18% higher, and in A/B tests it raised post-to-hire conversion by 9%. The product keeps changing, so I built the loop that keeps the model current: it picks which new data is worth training on by matching gradients, guards against forgetting old skills, scores outputs with a panel of LLM judges we calibrated, and ships changes through A/B tests.

**Before that: robots at Huawei Noah's Ark Lab.** I post-trained vision-language-action policies (π0.5, GR00T, OpenVLA) and video world models for long household tasks, generated synthetic training scenes with diffusion models, and built simulation benchmarks that show where robot policies break: clutter, distractors and new environments. Our team, The North Star, won the NeurIPS 2026 BEHAVIOR Challenge. I also built zero-shot 6D and 9DoF pose estimation, so warehouse robots can pick up boxes and objects they have never seen, even when they are partly hidden.

**Earlier:** at the Vector Institute I built multi-agent LLM workflows, RAG and evaluation for banks (CIBC, TD), and at Trans-Plan I shipped a multi-camera 3D tracking system for traffic analytics.

**On the side:** I run open studies with [Forall Labs](https://forall-labs.github.io), such as how robot policies cope when a task changes halfway through and how open LLMs fail at writing robot code (below).

**Next:** multimodal agents that keep learning from real-world feedback.

<a href="https://github.com/SajjadPSavoji/Resume/blob/master/Sajjad_Pakdamansavoji_CV.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-cv-dark.svg"><img src="assets/link-cv-light.svg" height="34" alt="Read my CV (PDF)"></picture></a>

## Featured open source

<p align="center">
  <a href="https://github.com/forall-labs/CALVIN-MAX"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-calvin-max-dark.svg"><img src="assets/card-calvin-max-light.svg" width="49%" alt="CALVIN-MAX: 7,828 cases of mid-task changes across 10 robot policies. Pooled task success: 69.9% with no change, 60.5% when the change is already in place, 63.0% when it arrives mid-task."></picture></a>
  <a href="https://github.com/forall-labs/OpenCaP"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-opencap-dark.svg"><img src="assets/card-opencap-light.svg" width="49%" alt="OpenCaP: 21 open-weight LLMs writing robot code in 7,560 trials. Removing high-level helpers raises frame errors from 4% to 47% and API misuse from 26% to 60% of failing programs."></picture></a>
</p>
<p align="center">
  <a href="https://github.com/forall-labs/AutoPolish"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-autopolish-dark.svg"><img src="assets/card-autopolish-light.svg" width="49%" alt="AutoPolish: one editing round. An image goes to Qwen2-VL persona critics, FLUX Kontext edits it, and the edit is kept only if the score rises; then the next round starts."></picture></a>
  <a href="https://github.com/SajjadPSavoji/awesome-weight-space-programming"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-awesome-wsp-dark.svg"><img src="assets/card-awesome-wsp-light.svg" width="49%" alt="Awesome Weight-Space Programming: the list grew from 31 to 606 entries between Nov 4 and Nov 15, curated by an agent."></picture></a>
</p>
<p align="center">
  <a href="https://github.com/SajjadPSavoji/MiniVLMDocEval"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-minivlmdoceval-dark.svg"><img src="assets/card-minivlmdoceval-light.svg" width="49%" alt="MiniVLMDocEval: mean score over five document benchmarks. Qwen3.5-0.8B 70.3, InternVL3-1B 63.3, LFM2.5-VL-450M 59.9, LLaVA-OV-0.5B 52.8, SmolVLM2-500M 49.4, FastVLM-0.5B 36.8."></picture></a>
  <a href="https://github.com/SajjadPSavoji/colabctl"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-colabctl-dark.svg"><img src="assets/card-colabctl-light.svg" width="49%" alt="colabctl: start, check and stop Google Colab GPU runtimes from the shell with colabctl up, colabctl status and colabctl down."></picture></a>
</p>

## Selected publications

| Venue | Paper | Links |
|:--|:--|:--|
| **Preprint** | **OLGA: Online Label-Free Gradient Matching for Continual Language Model Training**<br><sub>First author · LLM continual learning</sub> | [arXiv](https://arxiv.org/abs/2611.03496) |
| **Preprint** | **Prompt Lottery in LLM-as-a-Judge: Measuring and Mitigating Sensitivity to Syntactic Rephrasing**<br><sub>LLM evaluation</sub> | [arXiv](https://arxiv.org/abs/2610.38076) |
| **Preprint** | **Fragility Is Not Reducible to Hardness: Conditional Causal Difficulty for LLMs**<br><sub>LLM robustness</sub> | [arXiv](https://arxiv.org/abs/2611.02065) |
| **IROS 2026** | **How VLAs (Really) Work In Open-World Environments**<br><sub>Robot VLAs</sub> | [arXiv](https://arxiv.org/abs/2604.21192)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/How-VLAs-Really-Work/) |
| **ICRA 2026** | **Improving Robotic Manipulation Robustness via NICE Scene Surgery**<br><sub>First author · Robot manipulation</sub> | [arXiv](https://arxiv.org/abs/2511.22777)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/NICE-Scene-Surgery/) |
| **ICRA 2026** | **Distracted Robot: How Visual Clutter Undermine Robotic Manipulation**<br><sub>Robot manipulation</sub> | [arXiv](https://arxiv.org/abs/2511.22780)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/Distracted-Robot/) |
| **Preprint** | **Do World Action Models Generalize Better than VLAs? A Robustness Study**<br><sub>World models · Robot VLAs</sub> | [arXiv](https://arxiv.org/abs/2603.22078)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/World-Action-Model-Robustness/) |
| **WACV 2026** | **WALDO: Where Unseen Model-based 6D Pose Estimation Meets Occlusion**<br><sub>First author · 6D pose</sub> | [arXiv](https://arxiv.org/abs/2511.15874)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/WALDO/) |
| **ECCV&nbsp;2026&nbsp;W** | **AnyBox: Efficient Zero-Shot 9DoF Pose Estimation of Boxes for Robotic Manipulation**<br><sub>Equal contribution · 9DoF pose</sub> | [arXiv](https://arxiv.org/abs/2511.15884)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/AnyBox/) |
| **ITSC 2024** | **Ground Plane Projection for Improved Traffic Analytics at Intersections**<br><sub>First author · 🏆 Best Application Paper</sub> | [arXiv](https://arxiv.org/abs/2511.12342)&nbsp;·&nbsp;[Page](https://sajjadpsavoji.github.io/Ground-Plane-Projection/) |

<sub>Full list on <a href="https://scholar.google.com/citations?user=DZzLzNwAAAAJ">Google Scholar</a>.</sub>

## Experience

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/experience-dark.svg">
  <img src="assets/experience-light.svg" width="100%" alt="Experience: Lead AI Research Scientist at Upwork (2026 to now); Senior AI Researcher at Huawei Noah's Ark Lab (2024 to 2026); Machine Learning Engineer at Vector Institute (2023 to 2024); Machine Learning Engineer at Trans-Plan (2021 to 2023).">
</picture>
</p>

**Education:** M.Sc. Computer Science, York University · B.Sc. Electrical Engineering, University of Tehran

## Toolbox

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/toolbox-dark.svg">
  <img src="assets/toolbox-light.svg" width="100%" alt="Toolbox. Training: PyTorch, JAX, DeepSpeed, FSDP, TRL, PEFT, LoRA/QLoRA, SFT, DPO, GRPO. Serving and agents: vLLM, SGLang, TensorRT, Triton, LangGraph, MCP, RAG, LLM-as-a-judge. Robotics: Isaac Sim, MuJoCo, ManiSkill, OmniGibson, LeRobot, CALVIN, ROS 2. Vision: SAM2, DINOv2, Diffusers, Open3D, PyTorch3D, OpenCV, OpenGL. Infra: Python, C++, AWS, Slurm, Kubernetes, Ray, Docker, Weights and Biases.">
</picture>
</p>

## Recent

- **Nov 2026** · Released [Awesome Weight-Space Programming](https://github.com/SajjadPSavoji/awesome-weight-space-programming), a daily, agent-curated map of LLMs that read, edit and write network weights
- **Nov 2026** · Released [OpenCaP](https://forall-labs.github.io/OpenCaP/) and [CALVIN-MAX](https://forall-labs.github.io/CALVIN-MAX/), two open Forall Labs studies of robot code generation and mid-execution task changes
- **Nov 2026** · [OLGA](https://arxiv.org/abs/2611.03496), online label-free gradient matching for continual LM training, is on arXiv
- **Oct 2026** · 1st place in the NeurIPS 2026 BEHAVIOR Challenge with team The North Star

---

<p align="center"><sub>Say hello on <a href="https://www.linkedin.com/in/sajjadpsavoji">LinkedIn</a> or through <a href="https://sajjadpsavoji.github.io/contact.html">my website</a>. More work at <a href="https://sajjadpsavoji.github.io/projects.html">sajjadpsavoji.github.io</a>.<br>Icons: Lucide (ISC), Simple Icons and SVG Logos (CC0); brand marks belong to their owners.</sub></p>
