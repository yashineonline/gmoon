# Humanoid RL Project

## Overview

Minimal scaffold combining Isaac Gym simulation, PyTorch deep RL (PPO), and ROS2 control bridge for a humanoid prototype.

---

# Humanoid RL Research: Irreversible and Novelty-Based Learning Architectures

This repository contains simulations and research experiments for a novel reinforcement learning framework inspired by brain plasticity, irreversible quantum walks, and causal attention. The goal is to enable agents—particularly humanoid robots—to learn adaptively without revisiting obsolete behaviors.

## 🔍 Highlights

- **MiniGrid with Novelty Reward**: Rewards shaped by trajectory novelty and irreversible memory.
- **MuJoCo Hopper**: Suppression-based continuous control with evolving policy shifts.
- **Isaac Gym Humanoid (WIP)**: Transformer policy using forward-planning memory, under irreversible reward shaping.

## 🧠 Core Concepts

- **Irreversible Policy Update**: Repeated actions in similar states are suppressed over time.
- **Trajectory Novelty**: Rewards include a penalty for trajectory similarity to prior paths.
- **Causal Planning**: Isaac Gym prototype uses transformer agents that attend to suppressed future state memories.

## 💻 Getting Started

```bash
git clone https://github.com/yourhandle/humanoid-rl-research
cd humanoid-rl-research
pip install -r requirements.txt
```

---

## ▶️ Run Experiments

```bash
python src/irreversible_rl_simulations.py  
# Runs MiniGrid
# For MuJoCo:
# Uncomment train_mujoco() in the script
```

---

## 📝 Citation
Please cite our upcoming publication or reference the repository directly:

```bibtex
@misc{irreversible_rl,
  title={Irreversible Reinforcement Learning for Adaptive Control},
  author={Goolam Hossen, Yashine},
  year={2025},
  note={https://github.com/yourhandle/humanoid-rl-research}
}
```

---


## 🧪 Acknowledgements
Developed as part of an independent doctoral-level research project combining quantum information, reinforcement learning, and humanoid robotics.



---

### Directory Tree

```
humanoid-rl-research/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
│
├── src/
│   ├── irreversible_rl_simulations.py  # All simulations
│   ├── train_isaac_humanoid.py
│   ├── ablation_experiments.py         # Simulation 4
│   ├── simulation_5_meta_curriculum.py
│   ├── simulation_6_self_supervised.py
│   ├── simulation_7_inverse_rl.py
│   ├── simulation_8_multi_agent.py
│   ├──
│   ├── 
│   ├── agent_utils.py                  # Optional modular helpers
│   ├── config.yaml                     # Configs if used
│
├── notebooks/
│   └── results_analysis.ipynb          # Plots, analysis
│
├── results/
│   └── minigrid/
│   └── mujoco/
│   └── isaac/
│
└── gifs/
    └── demo.gif
```


---

```
humanoid_rl/
├── README.md
├── requirements.txt
├── ros2_ws/
│   ├── src/
│   │   └── humanoid_control/
│   │       ├── package.xml
│   │       ├── setup.py
│   │       └── humanoid_control/
│   │           ├── __init__.py
│   │           └── control_node.py
└── python/
    ├── envs/
    │   └── humanoid_env.py
    └── train_policy.py
```

---

### requirements.txt

```text
isaacgym==0.2.3
torch>=2.1
stable-baselines3==2.3.0
gym==0.26
rclpy
numpy
```

---

### README.md (excerpt)

```markdown
# Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Build ROS2 workspace
cd ros2_ws && colcon build
source install/setup.bash
```

---

### python/envs/humanoid\_env.py (simplified)

```python
import torch
from isaacgym import gymapi
from isaacgym import gymtorch
import gym
from gym import spaces

class HumanoidEnv(gym.Env):
    def __init__(self, cfg):
        self.gym = gymapi.acquire_gym()
        # create sim, load asset, etc.
        # ...
        self.obs_space = spaces.Box(-1.0, 1.0, (cfg['obs_dim'],), dtype=float)
        self.act_space = spaces.Box(-1.0, 1.0, (cfg['act_dim'],), dtype=float)

    def step(self, action):
        # apply forces to humanoid joints
        # ...
        reward = self.compute_reward()
        done = self.check_terminate()
        return self.get_obs(), reward, done, {}

    def reset(self):
        # reset sim
        # ...
        return self.get_obs()

    def get_obs(self):
        # return concatenated joint angles, velocities, root pose
        return self.obs_buf
```

---

### python/train\_policy.py (simplified)

```python
import torch
from stable_baselines3 import PPO
from envs.humanoid_env import HumanoidEnv

cfg = dict(obs_dim=120, act_dim=28)
env = HumanoidEnv(cfg)
model = PPO("MlpPolicy", env, verbose=1, n_steps=2048, batch_size=512,
            tensorboard_log="./tb")

model.learn(total_timesteps=3_000_000)
model.save("ppo_humanoid")
```

---

### ros2\_ws/src/humanoid\_control/control\_node.py

```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import torch

class HumanoidControl(Node):
    def __init__(self):
        super().__init__('humanoid_control')
        self.pub = self.create_publisher(JointState, '/humanoid/joint_cmd', 10)
        self.model = torch.jit.load('ppo_humanoid.pt')
        self.create_timer(0.02, self.control_callback)  # 50 Hz

    def control_callback(self):
        # TODO: subscribe to /humanoid/joint_states and sensor topics
        obs = self.get_obs()
        action, _ = self.model.predict(obs, deterministic=False)
        msg = JointState()
        msg.position = action.tolist()
        self.pub.publish(msg)

    def get_obs(self):
        # TODO: assemble observation vector from sensors
        return []


def main():
    rclpy.init()
    node = HumanoidControl()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
```

---

## Quick Run

1. **Train in simulation**

   ```bash
   python python/train_policy.py
   ```
2. **Launch ROS2 control node**

   ```bash
   source ros2_ws/install/setup.bash
   ros2 run humanoid_control control_node
   ```

---

   ```bash
python train_isaac_humanoid.py
```

## 🧪 What It Does:
Loads HumanoidTask with 2048 parallel agents

Applies transformer policy on 8-step observation sequences

Injects novelty suppression based on visit frequency of state patterns

Prints reward every 100 steps

---

## ✅ Simulation 4 (Ablation Experiment) 

🧪 Purpose:
This script compares:

Baseline PPO-style agent

Irreversible suppression agent

On the same MiniGrid task, and logs comparative reward performance.

---

## ✅ Simulation 5: Meta-RL with Curriculum + Irreversibility

🧪 What it does:
Wraps 3 MiniGrid tasks in increasing difficulty

Trains an irreversible Meta-RL agent across tasks

Increases environment difficulty every 50 episodes

Tracks suppression-based policy modulation per state-action

---

## ✅ Simulation 6 added: Self-Supervised Representation Learning + Irreversible RL

🔍 What it does:
Learns compact latent states via contrastive loss (anchor, positive, negative)

Uses frozen encoder for RL with suppression-based action modulation

Entire setup done in MiniGrid

---

A novel 6-simulation suite combining:

Novelty-driven RL

Transformer policies

Curriculum learning

Self-supervision

---

## ✅ Simulation 7 added: Inverse RL for Implicit Suppression

🔍 What it does:
Uses expert trajectories to train a reward model via a discriminator

Learns a policy to match expert behavior through reward inference

No explicit suppression — learned via imitation from demos

---

## ✅ Simulation 8 added: Multi-Agent Irreversible RL

🧠 What it does:
Trains 3 agents in parallel

Uses shared policy network with agent-specific suppression memory

Encourages distributed irreversible exploration patterns

---

The 8 simulations cover the full RL research suite:

1. MiniGrid with novelty + suppression

2. MuJoCo continuous control with suppression

3. Isaac Gym humanoid transformer policy

4. Ablation experiments

5. Meta-RL curriculum learning

6. Self-supervised latent learning

7. Inverse RL for implicit suppression

8. Multi-agent irreversible RL

---

## Simulation 9 (attention-based memory embedding)





---

## Skill Tests

* **Adaptability:** Randomize terrain in env and retrain.
* **Fail‑safe:** Disable one joint mid‑episode, maintain balance.
* **Latency:** Measure ROS2 round‑trip latencies (goal <20 ms).
