<a href="https://sajjadpsavoji.github.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" width="100%" alt="Sajjad Pakdamansavoji, Lead AI Research Scientist at Upwork. I post-train foundation models and keep them improving after they ship: today the LLM behind Upwork's job-post agent, before that robot VLAs and world models at Huawei.">
  </picture>
</a>

<p align="center">
  <a href="https://sajjadpsavoji.github.io"><img src="https://img.shields.io/badge/Website-24292f?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIvPjxwYXRoIGQ9Ik0yIDEyaDIwTTEyIDJhMTUgMTUgMCAwIDEgMCAyME0xMiAyYTE1IDE1IDAgMCAwIDAgMjAiLz48L3N2Zz4=" alt="Website"></a>
  <a href="https://scholar.google.com/citations?user=DZzLzNwAAAAJ"><img src="https://img.shields.io/badge/Google_Scholar-24292f?style=flat-square&logo=googlescholar&logoColor=white" alt="Google Scholar"></a>
  <a href="https://huggingface.co/savoji"><img src="https://img.shields.io/badge/Hugging_Face-24292f?style=flat-square&logo=huggingface&logoColor=white" alt="Hugging Face"></a>
  <a href="https://www.linkedin.com/in/sajjadpsavoji"><img src="https://img.shields.io/badge/LinkedIn-24292f?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik00Ljk4IDMuNUM0Ljk4IDQuODggMy44NyA2IDIuNSA2UzAgNC44OCAwIDMuNSAxLjEyIDEgMi41IDFzMi40OCAxLjEyIDIuNDggMi41ek0uNSA4aDR2MTZoLTRWOHptNy41IDBoMy44djIuMmguMDVjLjUzLTEgMS44My0yLjIgMy43Ny0yLjIgNC4wMyAwIDQuNzggMi42NSA0Ljc4IDYuMVYyNGgtNHYtOC4xYzAtMS45My0uMDMtNC40Mi0yLjctNC40Mi0yLjcgMC0zLjEgMi4xLTMuMSA0LjI4VjI0aC00Vjh6Ii8+PC9zdmc+" alt="LinkedIn"></a>
  <a href="https://x.com/saavoji"><img src="https://img.shields.io/badge/X-24292f?style=flat-square&logo=x&logoColor=white" alt="X"></a>
  <a href="https://forall-labs.github.io"><img src="https://img.shields.io/badge/%E2%88%80_Forall_Labs-24292f?style=flat-square" alt="Forall Labs"></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/highlights-dark.svg">
  <img src="assets/highlights-light.svg" width="100%" alt="Highlights: 1st place in the NeurIPS 2026 BEHAVIOR Challenge with team The North Star. 1M+ daily users on the LLM my team post-trains at Upwork. 13 papers and preprints on LLM post-training and evaluation, robot VLAs and world models, and 6D pose estimation. 3 patents filed on robot VLAs, world models and 3D vision.">
</picture>

## About

I take foundation models from research to real use: I post-train them on real data, measure exactly where they fail, and keep them improving after people start using them. Over the last six years that has meant LLMs in production, robot policies in simulation and on hardware, and 3D vision for warehouses and city streets.

**What I do now: LLMs at Upwork.** I lead a five-person team that owns the model writing job posts inside Upwork's AI agent, used by more than a million people a day. We replaced a paid API model with an open Qwen model that we post-train ourselves on 100+ GPUs. It costs about 70% less, judges rate its posts 18% higher, and in A/B tests it raised post-to-hire conversion by 9%. The product keeps changing, so I built the loop that keeps the model current: it picks which new data is worth training on by matching gradients, guards against forgetting old skills, scores outputs with a panel of LLM judges we calibrated, and ships changes through A/B tests.

**Before that: robots at Huawei Noah's Ark Lab.** I post-trained vision-language-action policies (π0.5, GR00T, OpenVLA) and video world models for long household tasks, generated synthetic training scenes with diffusion models, and built simulation benchmarks that show where robot policies break: clutter, distractors and new environments. Our team, The North Star, won the NeurIPS 2026 BEHAVIOR Challenge. I also built zero-shot 6D and 9DoF pose estimation, so warehouse robots can pick up boxes and objects they have never seen, even when they are partly hidden.

**Earlier:** at the Vector Institute I built multi-agent LLM workflows, RAG and evaluation for banks (CIBC, TD), and at Trans-Plan I shipped a multi-camera 3D tracking system for traffic analytics.

**On the side:** I run open studies with [Forall Labs](https://forall-labs.github.io), such as how robot policies cope when a task changes halfway through and how open LLMs fail at writing robot code (below).

**Next:** multimodal agents that keep learning from real-world feedback.

📄 **[Read my CV (PDF)](https://github.com/SajjadPSavoji/Resume/blob/master/Sajjad_Pakdamansavoji_CV.pdf)** · [LaTeX source](https://github.com/SajjadPSavoji/Resume)

## Featured open source

<p align="center">
  <a href="https://github.com/forall-labs/CALVIN-MAX"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-calvin-max-dark.svg"><img src="assets/card-calvin-max-light.svg" width="49%" alt="CALVIN-MAX: a 7,828-case benchmark of mid-execution changes for robot policies on CALVIN."></picture></a>
  <a href="https://github.com/forall-labs/OpenCaP"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-opencap-dark.svg"><img src="assets/card-opencap-light.svg" width="49%" alt="OpenCaP: how open-weight LLMs fail at writing robot code, across 7,560 trials of 21 models."></picture></a>
</p>
<p align="center">
  <a href="https://github.com/forall-labs/AutoPolish"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-autopolish-dark.svg"><img src="assets/card-autopolish-light.svg" width="49%" alt="AutoPolish: training-free image aesthetics editing with a synthetic audience of VLM critics."></picture></a>
  <a href="https://github.com/SajjadPSavoji/awesome-weight-space-programming"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-awesome-wsp-dark.svg"><img src="assets/card-awesome-wsp-light.svg" width="49%" alt="Awesome Weight-Space Programming: a daily, agent-curated map of LLMs that read, edit and write network weights."></picture></a>
</p>
<p align="center">
  <a href="https://github.com/SajjadPSavoji/MiniVLMDocEval"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-minivlmdoceval-dark.svg"><img src="assets/card-minivlmdoceval-light.svg" width="49%" alt="MiniVLMDocEval: six sub-1B VLMs benchmarked on five document understanding benchmarks."></picture></a>
  <a href="https://github.com/SajjadPSavoji/colabctl"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-colabctl-dark.svg"><img src="assets/card-colabctl-light.svg" width="49%" alt="colabctl: scriptable connect, status and disconnect for Google Colab GPU runtimes."></picture></a>
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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/experience-dark.svg">
  <img src="assets/experience-light.svg" width="100%" alt="Experience: Lead AI Research Scientist at Upwork (2026 to now); Senior AI Researcher at Huawei Noah's Ark Lab (2024 to 2026); Machine Learning Engineer at Vector Institute (2023 to 2024); Machine Learning Engineer at Trans-Plan (2021 to 2023).">
</picture>

**Education:** M.Sc. Computer Science, York University · B.Sc. Electrical Engineering, University of Tehran

## Toolbox

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/toolbox-dark.svg">
  <img src="assets/toolbox-light.svg" width="100%" alt="Toolbox. Training: PyTorch, JAX, DeepSpeed, FSDP, TRL, PEFT, LoRA/QLoRA, SFT, DPO, GRPO. Serving and agents: vLLM, SGLang, TensorRT, Triton, LangGraph, MCP, RAG, LLM-as-a-judge. Robotics: Isaac Sim, MuJoCo, ManiSkill, OmniGibson, LeRobot, CALVIN, ROS 2. Vision: SAM2, DINOv2, Diffusers, Open3D, PyTorch3D, OpenCV, OpenGL. Infra: Python, C++, AWS, Slurm, Kubernetes, Ray, Docker, Weights and Biases.">
</picture>

## Recent

- **Nov 2026** · Released [Awesome Weight-Space Programming](https://github.com/SajjadPSavoji/awesome-weight-space-programming), a daily, agent-curated map of LLMs that read, edit and write network weights
- **Nov 2026** · Released [OpenCaP](https://forall-labs.github.io/OpenCaP/) and [CALVIN-MAX](https://forall-labs.github.io/CALVIN-MAX/), two open Forall Labs studies of robot code generation and mid-execution task changes
- **Nov 2026** · [OLGA](https://arxiv.org/abs/2611.03496), online label-free gradient matching for continual LM training, is on arXiv
- **Oct 2026** · 1st place in the NeurIPS 2026 BEHAVIOR Challenge with team The North Star

---

<p align="center"><sub>Say hello on <a href="https://www.linkedin.com/in/sajjadpsavoji">LinkedIn</a> or through <a href="https://sajjadpsavoji.github.io/contact.html">my website</a>. More work at <a href="https://sajjadpsavoji.github.io/projects.html">sajjadpsavoji.github.io</a>.</sub></p>
